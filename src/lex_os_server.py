"""
Servidor MCP Lex-OS - Sistema Operacional Jurídico
Implementação do servidor MCP com os três módulos especificados:
1. Módulo de Memória (Obsidian First)
2. Módulo de Execução (Fabric Wrapper)
3. Módulo de Orquestração Zotero
"""

import asyncio
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml
from fastmcp import FastMCP, Tool
from pyzotero import zotero

# Configuração do servidor
CONFIG_FILE = "paths.yaml"
OBSIDIAN_VAULT_PATH = ""  # Será carregado do paths.yaml
ZOTERO_LIBRARY_ID = os.getenv("ZOTERO_LIBRARY_ID", "")
ZOTERO_API_KEY = os.getenv("ZOTERO_API_KEY", "")
ZOTERO_LOCAL = os.getenv("ZOTERO_LOCAL", "false").lower() == "true"
CUSTOM_PATTERNS_PATH = "/home/peixoto/peixoto-ops/costum_patterns"


def load_config():
    """Carrega a configuração do paths.yaml"""
    global OBSIDIAN_VAULT_PATH
    
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config = yaml.safe_load(f)
            OBSIDIAN_VAULT_PATH = config.get('obsidian_vault_path', '')
    else:
        print(f"Arquivo de configuração {CONFIG_FILE} não encontrado")


class LexOSServer:
    def __init__(self):
        load_config()
        self.app = FastMCP(
            name="Lex-OS Kernel",
            description="Sistema Operacional Jurídico - Middleware entre Zotero, Obsidian e Fabric"
        )
        self.setup_tools()

    def setup_tools(self):
        """Configura as ferramentas do servidor MCP"""
        self.app.add_tool(Tool(
            name="check_local_memory",
            description="Verifica a memória local (Obsidian) antes de buscar externamente",
            parameters={
                "query": {"type": "string", "description": "Consulta para buscar na memória local"},
                "threshold": {"type": "number", "description": "Limiar de similaridade (padrão: 0.6)", "default": 0.6}
            },
            handler=self.check_local_memory
        ))

        self.app.add_tool(Tool(
            name="run_fabric_pipeline",
            description="Executa pipelines do Fabric para processamento de texto jurídico",
            parameters={
                "text": {"type": "string", "description": "Texto para processar"},
                "pipeline_type": {
                    "type": "string",
                    "description": "Tipo de pipeline: 'analise_precedente', 'fichamento_simples', 'verificacao_tese'",
                    "enum": ["analise_precedente", "fichamento_simples", "verificacao_tese"]
                }
            },
            handler=self.run_fabric_pipeline
        ))

        self.app.add_tool(Tool(
            name="process_zotero_collection",
            description="Processa uma coleção específica do Zotero com pipeline do Fabric",
            parameters={
                "collection_name": {"type": "string", "description": "Nome da coleção Zotero para processar"},
                "instruction": {"type": "string", "description": "Instrução para o processamento"}
            },
            handler=self.process_zotero_collection
        ))

    async def check_local_memory(self, query: str, threshold: float = 0.6) -> Dict:
        """
        Verifica a memória local (Obsidian) antes de buscar externamente
        
        Args:
            query: Consulta para buscar na memória local
            threshold: Limiar de similaridade (padrão: 0.6)
        
        Returns:
            Dict com o status da busca e os resultados relevantes
        """
        if not OBSIDIAN_VAULT_PATH:
            return {
                "status": "ERROR",
                "message": "Caminho do vault do Obsidian não configurado"
            }

        vault_path = Path(OBSIDIAN_VAULT_PATH)
        if not vault_path.exists():
            return {
                "status": "ERROR",
                "message": f"Caminho do vault do Obsidian não encontrado: {OBSIDIAN_VAULT_PATH}"
            }

        # Busca por arquivos Markdown no vault
        relevant_notes = []
        query_lower = query.lower()
        
        for md_file in vault_path.rglob("*.md"):
            try:
                content = md_file.read_text(encoding='utf-8')
                # Verifica se o conteúdo contém a consulta (busca simples por enquanto)
                if query_lower in content.lower():
                    # Calcula uma pontuação básica baseada na frequência da consulta
                    score = content.lower().count(query_lower) / len(content.split())
                    
                    if score >= threshold:
                        relevant_notes.append({
                            "path": str(md_file.relative_to(vault_path)),
                            "score": score,
                            "preview": content[:200] + "..." if len(content) > 200 else content
                        })
            except Exception as e:
                print(f"Erro ao ler arquivo {md_file}: {e}")
                continue

        if relevant_notes:
            # Ordena por pontuação
            relevant_notes.sort(key=lambda x: x['score'], reverse=True)
            return {
                "status": "INFORMACAO_ENCONTRADA_LOCALMENTE",
                "notes_found": len(relevant_notes),
                "notes": relevant_notes[:5]  # Retorna no máximo 5 notas
            }
        else:
            return {
                "status": "NECESSARIO_BUSCA_EXTERNA",
                "notes_found": 0,
                "notes": []
            }

    async def run_fabric_pipeline(self, text: str, pipeline_type: str) -> Dict:
        """
        Executa pipelines do Fabric para processamento de texto jurídico
        
        Args:
            text: Texto para processar
            pipeline_type: Tipo de pipeline a executar
        
        Returns:
            Dict com o resultado do processamento
        """
        try:
            # Mapeia o tipo de pipeline para os patterns correspondentes
            pipeline_map = {
                "analise_precedente": ["make_firac+", "extract_key_notes"],
                "fichamento_simples": ["summarize", "fichamento_processo_autos"],
                "verificacao_tese": ["fact-check", "check_agreement"]
            }

            if pipeline_type not in pipeline_map:
                return {
                    "status": "ERROR",
                    "message": f"Tipo de pipeline desconhecido: {pipeline_type}",
                    "supported_types": list(pipeline_map.keys())
                }

            patterns = pipeline_map[pipeline_type]
            result = text  # Começa com o texto original

            # Executa cada pattern na sequência
            for pattern in patterns:
                try:
                    # Tenta executar o pattern do diretório customizado primeiro
                    custom_pattern_path = os.path.join(CUSTOM_PATTERNS_PATH, f"{pattern}.yaml")
                    
                    cmd = ["fabric", "-p", pattern]
                    if os.path.exists(custom_pattern_path):
                        # Se o pattern customizado existir, usa o caminho completo
                        cmd = ["fabric", "-p", custom_pattern_path]
                    
                    # Executa o comando do fabric com o texto como stdin
                    process = subprocess.run(
                        cmd,
                        input=result,
                        text=True,
                        capture_output=True,
                        check=True
                    )
                    
                    # O resultado do pattern se torna a entrada para o próximo
                    result = process.stdout
                except subprocess.CalledProcessError as e:
                    return {
                        "status": "ERROR",
                        "message": f"Erro ao executar o pattern '{pattern}': {e.stderr.decode()}",
                        "partial_result": result
                    }
                except FileNotFoundError:
                    return {
                        "status": "ERROR",
                        "message": f"Ferramenta 'fabric' não encontrada. Verifique se está instalada.",
                        "partial_result": result
                    }

            return {
                "status": "SUCCESS",
                "pipeline_type": pipeline_type,
                "result": result,
                "patterns_used": patterns
            }
        except Exception as e:
            return {
                "status": "ERROR",
                "message": f"Erro inesperado ao executar pipeline: {str(e)}"
            }

    async def process_zotero_collection(self, collection_name: str, instruction: str) -> Dict:
        """
        Processa uma coleção específica do Zotero com pipeline do Fabric
        
        Args:
            collection_name: Nome da coleção Zotero para processar
            instruction: Instrução para o processamento
        
        Returns:
            Dict com o relatório do processamento
        """
        try:
            # Configuração do Zotero
            if ZOTERO_LOCAL:
                # Modo local
                zot = zotero.Zotero(library_type='user', library_id=None)
            else:
                # Modo API
                if not ZOTERO_LIBRARY_ID or not ZOTERO_API_KEY:
                    return {
                        "status": "ERROR",
                        "message": "Credenciais do Zotero não configuradas"
                    }
                zot = zotero.Zotero(
                    library_id=ZOTERO_LIBRARY_ID,
                    library_type='user',
                    api_key=ZOTERO_API_KEY
                )

            # Busca a coleção pelo nome (fuzzy match)
            collections = zot.collections()
            target_collection = None
            
            for collection in collections:
                if collection_name.lower() in collection['data']['name'].lower():
                    target_collection = collection
                    break

            if not target_collection:
                # Tenta encontrar com fuzzy matching mais flexível
                for collection in collections:
                    if collection_name.lower() in collection['data']['name'].lower() or \
                       collection['data']['name'].lower() in collection_name.lower():
                        target_collection = collection
                        break

            if not target_collection:
                return {
                    "status": "ERROR",
                    "message": f"Coleção '{collection_name}' não encontrada",
                    "available_collections": [c['data']['name'] for c in collections]
                }

            collection_key = target_collection['key']
            
            # Recupera os itens da coleção (limitado a 10 por padrão)
            items = zot.collection_items(collection_key, limit=10)
            
            processed_count = 0
            results = []

            for item in items:
                try:
                    item_key = item['key']
                    item_title = item['data'].get('title', 'Sem título')
                    
                    # Tenta obter o conteúdo do item (fulltext ou metadata)
                    try:
                        fulltext = zot.item_fulltext(item_key)
                        content = fulltext.get('content', '') if fulltext else ''
                    except:
                        # Se não conseguir o fulltext, tenta obter metadata como markdown
                        try:
                            metadata = zot.item(item_key)
                            content = json.dumps(metadata, indent=2, ensure_ascii=False)
                        except:
                            content = f"Title: {item_title}\n\nContent not available."

                    if content.strip():
                        # Processa o conteúdo com o pipeline do Fabric
                        pipeline_result = await self.run_fabric_pipeline(
                            text=content,
                            pipeline_type="analise_precedente"  # Padrão para análise de precedentes
                        )

                        if pipeline_result['status'] == 'SUCCESS':
                            # Salva o resultado no Obsidian
                            obsidian_path = Path(OBSIDIAN_VAULT_PATH) if OBSIDIAN_VAULT_PATH else Path.home()
                            
                            # Cria o diretório de processamento se não existir
                            proc_dir = obsidian_path / "02 - Processamento" / "Zotero_Inbox"
                            proc_dir.mkdir(parents=True, exist_ok=True)
                            
                            # Cria o nome do arquivo baseado no título do item
                            safe_title = "".join(c for c in item_title if c.isalnum() or c in (' ', '-', '_')).rstrip()
                            if not safe_title:
                                safe_title = f"item_{item_key}"
                            
                            file_path = proc_dir / f"{safe_title}.md"
                            
                            # Escreve o resultado no arquivo
                            with open(file_path, 'w', encoding='utf-8') as f:
                                f.write(f"# {item_title}\n\n")
                                f.write(f"**Coleção:** {collection_name}\n\n")
                                f.write(f"**Chave Zotero:** {item_key}\n\n")
                                f.write("---\n\n")
                                f.write(pipeline_result['result'])

                            results.append({
                                "item_key": item_key,
                                "title": item_title,
                                "status": "SUCCESS",
                                "output_path": str(file_path.relative_to(obsidian_path))
                            })
                            processed_count += 1
                        else:
                            results.append({
                                "item_key": item_key,
                                "title": item_title,
                                "status": "FAILED",
                                "error": pipeline_result.get('message', 'Unknown error')
                            })
                    else:
                        results.append({
                            "item_key": item_key,
                            "title": item_title,
                            "status": "SKIPPED",
                            "reason": "No content available"
                        })

                except Exception as e:
                    results.append({
                        "item_key": item.get('key', 'unknown'),
                        "title": item.get('data', {}).get('title', 'Unknown'),
                        "status": "ERROR",
                        "error": str(e)
                    })

            return {
                "status": "SUCCESS",
                "collection_processed": collection_name,
                "items_found": len(items),
                "items_processed": processed_count,
                "total_results": len(results),
                "results": results
            }

        except Exception as e:
            return {
                "status": "ERROR",
                "message": f"Erro ao processar coleção Zotero: {str(e)}"
            }

    def run(self, host: str = "localhost", port: int = 8000):
        """Inicia o servidor MCP"""
        print(f"Iniciando servidor Lex-OS na {host}:{port}")
        print(f"Vault do Obsidian: {OBSIDIAN_VAULT_PATH}")
        print(f"Biblioteca Zotero: {ZOTERO_LIBRARY_ID}")
        print(f"Modo Zotero Local: {ZOTERO_LOCAL}")
        
        self.app.run(host=host, port=port)


def main():
    """Função principal para executar o servidor"""
    server = LexOSServer()
    
    import argparse
    parser = argparse.ArgumentParser(description="Servidor MCP Lex-OS")
    parser.add_argument("--host", default="localhost", help="Host para o servidor")
    parser.add_argument("--port", type=int, default=8000, help="Porta para o servidor")
    
    args = parser.parse_args()
    
    server.run(host=args.host, port=args.port)


if __name__ == "__main__":
    main()