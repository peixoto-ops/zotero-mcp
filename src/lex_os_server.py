import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional
import yaml
from fastmcp import FastMCP
from pyzotero import zotero

# --- Configuração Dinâmica ---
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR / "config" / "paths.yaml"

def load_config():
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, 'r') as f:
            return yaml.safe_load(f)
    return {}

config = load_config()
OBSIDIAN_VAULT = Path(config.get('obsidian_vault_path', ''))
PATTERNS_DIR = Path(config.get('custom_patterns_path', ''))

# --- Inicialização do Servidor ---
mcp = FastMCP(
    name="Lex-OS Kernel",
    description="Orquestrador Jurídico: Memória (Obsidian) + Execução (Fabric) + Fonte (Zotero)",
)

# --- Módulo 1: Memória (Obsidian First) ---
@mcp.tool()
async def check_local_memory(query: str) -> str:
    """
    [CRÍTICO] Verifica se o assunto já existe no Obsidian antes de buscar fora.
    Retorna snippets das notas encontradas ou autorização para busca externa.
    """
    if not OBSIDIAN_VAULT.exists():
        return f"ERRO DE CONFIGURAÇÃO: Vault não encontrado em {OBSIDIAN_VAULT}"
    
    # Busca otimizada nas pastas de processamento e output
    target_dirs = [
        OBSIDIAN_VAULT / "02 - Processamento",
        OBSIDIAN_VAULT / "03 - Saída" # Ajuste conforme sua estrutura real
    ]
    
    matches = []
    query_lower = query.lower()

    for directory in target_dirs:
        if not directory.exists(): continue
        
        # Varredura rápida (limitada a md)
        for md_file in directory.rglob("*.md"):
            try:
                # Leitura segura ignorando erros de encoding
                content = md_file.read_text(encoding='utf-8', errors='ignore')
                if query_lower in content.lower():
                    snippet = content[:200].replace('\n', ' ')
                    matches.append(f"- [{md_file.name}]: {snippet}...")
                    if len(matches) >= 5: break # Limite de 5 resultados
            except Exception:
                continue
        if len(matches) >= 5: break

    if matches:
        return (
            "⚠️ MEMÓRIA ATIVADA: Informação encontrada localmente.\n"
            "NÃO faça buscas web. Use o contexto abaixo:\n\n" + 
            "\n".join(matches)
        )
    
    return "✅ MEMÓRIA VAZIA: Autorizado a prosseguir com busca externa (Zotero/Web)."

# --- Módulo 2: Execução (Fabric Wrapper Async) ---
@mcp.tool()
async def run_fabric_pipeline(text: str, pipeline_type: str) -> str:
    """
    Executa patterns do Fabric via CLI de forma assíncrona.
    pipeline_type: 'analise_precedente' | 'fichamento' | 'tese_check'
    """
    
    # Definição dos Pipelines (Sequência de Patterns)
    pipelines = {
        "analise_precedente": ["make_firac+", "extract_key_notes"],
        "fichamento": ["summarize", "fichamento_processo_autos"],
        "tese_check": ["fact-check", "check_agreement"]
    }
    
    patterns_to_run = pipelines.get(pipeline_type)
    if not patterns_to_run:
        return f"ERRO: Pipeline '{pipeline_type}' inválido. Use: {list(pipelines.keys())}"

    current_text = text
    execution_log = []

    for pattern in patterns_to_run:
        try:
            # Tenta achar o pattern customizado
            pattern_cmd = pattern
            if PATTERNS_DIR.exists():
                 # Verifica se existe como pasta ou arquivo yaml
                 if (PATTERNS_DIR / pattern).exists() or (PATTERNS_DIR / f"{pattern}.yaml").exists():
                     # O Fabric detecta automaticamente se passarmos o caminho relativo ou nome se estiver na config
                     # Mas para garantir, podemos passar o nome simples por enquanto.
                     pass 

            # Execução não-bloqueante (A Mágica do Async)
            process = await asyncio.create_subprocess_exec(
                "fabric", "-p", pattern,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            stdout, stderr = await process.communicate(input=current_text.encode())
            
            if process.returncode != 0:
                return f"FALHA NO FABRIC ({pattern}): {stderr.decode()}"
            
            current_text = stdout.decode()
            execution_log.append(f"✓ {pattern}")
            
        except Exception as e:
            return f"ERRO DE SISTEMA ({pattern}): {str(e)}"

    return f"--- RELATÓRIO LEX-OS ---\nPipeline: {pipeline_type}\nStatus: {', '.join(execution_log)}\n\n{current_text}"

# --- Módulo 3: Zotero (API Cloud) ---
@mcp.tool()
def process_zotero_collection(collection_name: str) -> str:
    """
    Busca os 5 itens mais recentes de uma coleção no Zotero.
    Requer ZOTERO_API_KEY e ZOTERO_LIBRARY_ID no ambiente.
    """
    api_key = os.getenv("ZOTERO_API_KEY")
    library_id = os.getenv("ZOTERO_LIBRARY_ID")
    
    if not api_key or not library_id:
        return "ERRO: Credenciais do Zotero não configuradas (ENV VARS missing)."

    try:
        zot = zotero.Zotero(library_id, 'user', api_key)
        
        # 1. Buscar a coleção (Fuzzy search simples)
        col_results = zot.collections(q=collection_name)
        if not col_results:
            return f"Coleção '{collection_name}' não encontrada no Zotero."
        
        target_col = col_results[0]
        
        # 2. Buscar itens
        items = zot.collection_items(target_col['key'], limit=5)
        
        report = []
        for item in items:
            title = item['data'].get('title', 'Sem Título')
            key = item['key']
            # Aqui poderíamos chamar o run_fabric_pipeline internamente se quiséssemos automação total
            report.append(f"- ID: {key} | Título: {title}")
            
        return f"Itens encontrados na coleção '{target_col['data']['name']}':\n" + "\n".join(report)
        
    except Exception as e:
        return f"ERRO ZOTERO API: {str(e)}"

if __name__ == "__main__":
    mcp.run()