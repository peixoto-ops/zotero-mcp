"""
Sistema de Validação para Referência Cruzada
Entre Zotero, Obsidian e Padrões Fabric
"""

import hashlib
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml
from pyzotero import zotero


class CrossReferenceValidator:
    """
    Classe para validar a integridade e consistência das referências
    entre Zotero, Obsidian e os padrões Fabric
    """
    
    def __init__(self, config_path: str = "paths.yaml"):
        self.config = self.load_config(config_path)
        self.zotero_client = self.setup_zotero()
        
    def load_config(self, config_path: str) -> Dict:
        """Carrega a configuração do sistema"""
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return yaml.safe_load(f)
        else:
            raise FileNotFoundError(f"Arquivo de configuração {config_path} não encontrado")
    
    def setup_zotero(self):
        """Configura o cliente Zotero"""
        if self.config.get('zotero_local', False):
            return zotero.Zotero(library_type='user', library_id=None)
        else:
            library_id = self.config.get('zotero_library_id')
            api_key = self.config.get('zotero_api_key')
            if not library_id or not api_key:
                raise ValueError("Credenciais do Zotero não configuradas")
            return zotero.Zotero(
                library_id=library_id,
                library_type='user',
                api_key=api_key
            )
    
    def calculate_content_hash(self, content: str) -> str:
        """Calcula o hash SHA-256 do conteúdo para verificação de integridade"""
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    
    def validate_zotero_obsidian_link(self, item_key: str, note_path: str) -> Dict:
        """
        Valida a integridade do link entre um item do Zotero e uma nota do Obsidian
        
        Args:
            item_key: Chave do item no Zotero
            note_path: Caminho da nota no Obsidian
            
        Returns:
            Dict com o resultado da validação
        """
        try:
            # Obtém o item do Zotero
            zotero_item = self.zotero_client.item(item_key)
            
            # Lê a nota do Obsidian
            note_file_path = Path(self.config['obsidian_vault_path']) / note_path
            if not note_file_path.exists():
                return {
                    "status": "ERROR",
                    "message": f"Nota do Obsidian não encontrada: {note_path}",
                    "zotero_item_exists": True,
                    "obsidian_note_exists": False
                }
            
            note_content = note_file_path.read_text(encoding='utf-8')
            
            # Verifica se a nota contém referência ao item do Zotero
            zotero_ref_found = item_key in note_content
            
            # Calcula hashes para verificação de integridade
            zotero_content = json.dumps(zotero_item, sort_keys=True, ensure_ascii=False)
            zotero_hash = self.calculate_content_hash(zotero_content)
            note_hash = self.calculate_content_hash(note_content)
            
            # Verifica se há metadados de integração
            integration_metadata = self.extract_integration_metadata(note_content)
            
            return {
                "status": "VALIDATED",
                "zotero_item_exists": True,
                "obsidian_note_exists": True,
                "zotero_reference_found": zotero_ref_found,
                "zotero_content_hash": zotero_hash,
                "note_content_hash": note_hash,
                "integration_metadata": integration_metadata,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                "status": "ERROR",
                "message": f"Erro ao validar link entre Zotero e Obsidian: {str(e)}",
                "zotero_item_exists": False,
                "obsidian_note_exists": False
            }
    
    def extract_integration_metadata(self, content: str) -> Dict:
        """Extrai metadados de integração do conteúdo da nota"""
        metadata = {}
        
        # Procura por metadados YAML no início da nota
        if content.startswith('---'):
            try:
                end_yaml = content.find('---', 3)
                if end_yaml != -1:
                    yaml_content = content[3:end_yaml].strip()
                    yaml_data = yaml.safe_load(yaml_content)
                    if yaml_data:
                        metadata.update(yaml_data)
            except:
                pass
        
        # Procura por links ou referências específicas
        if 'zotero://' in content:
            metadata['has_zotero_links'] = True
        if '[[Zotero]]' in content or '[Zotero]' in content:
            metadata['has_zotero_brackets'] = True
            
        return metadata
    
    def validate_fabric_pattern_application(self, note_path: str, expected_patterns: List[str]) -> Dict:
        """
        Valida se os padrões Fabric foram aplicados corretamente à nota
        
        Args:
            note_path: Caminho da nota no Obsidian
            expected_patterns: Lista de padrões esperados
            
        Returns:
            Dict com o resultado da validação
        """
        try:
            note_file_path = Path(self.config['obsidian_vault_path']) / note_path
            if not note_file_path.exists():
                return {
                    "status": "ERROR",
                    "message": f"Nota do Obsidian não encontrada: {note_path}"
                }
            
            note_content = note_file_path.read_text(encoding='utf-8')
            
            applied_patterns = []
            missing_patterns = []
            
            # Verifica a presença de cada padrão esperado
            for pattern in expected_patterns:
                if pattern.lower() in note_content.lower():
                    applied_patterns.append(pattern)
                else:
                    missing_patterns.append(pattern)
            
            # Verifica se a nota contém estruturas típicas de padrões Fabric
            has_fabric_structure = any([
                '# FIRAC+' in note_content,
                '## Facts' in note_content,
                '## Issue' in note_content,
                '## Rule' in note_content,
                '## Analysis' in note_content,
                '## Conclusion' in note_content,
                '**Fatos**:' in note_content,
                '**Questão**:' in note_content,
                '**Regra**:' in note_content,
                '### Análise' in note_content,
                '### Conclusão' in note_content
            ])
            
            return {
                "status": "VALIDATED",
                "note_path": note_path,
                "expected_patterns": expected_patterns,
                "applied_patterns": applied_patterns,
                "missing_patterns": missing_patterns,
                "has_fabric_structure": has_fabric_structure,
                "pattern_compliance_rate": len(applied_patterns) / len(expected_patterns) if expected_patterns else 0,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                "status": "ERROR",
                "message": f"Erro ao validar aplicação de padrões Fabric: {str(e)}"
            }
    
    def validate_cross_references_integrity(self, collection_name: str = None) -> Dict:
        """
        Valida a integridade das referências cruzadas em uma coleção
        
        Args:
            collection_name: Nome da coleção para validar (None para todas)
            
        Returns:
            Dict com o resultado da validação
        """
        try:
            # Obtém as coleções
            if collection_name:
                collections = self.zotero_client.collections()
                target_collection = None
                for collection in collections:
                    if collection_name.lower() in collection['data']['name'].lower():
                        target_collection = collection
                        break
                
                if not target_collection:
                    return {
                        "status": "ERROR",
                        "message": f"Coleção '{collection_name}' não encontrada"
                    }
                
                items = self.zotero_client.collection_items(target_collection['key'])
            else:
                # Valida todas as coleções
                items = self.zotero_client.items(limit=50)  # Limita para evitar sobrecarga
            
            validation_results = []
            total_items = len(items)
            valid_items = 0
            
            for item in items:
                item_key = item['key']
                item_title = item['data'].get('title', 'Sem título')
                
                # Tenta encontrar a nota correspondente no Obsidian
                # Baseia-se no título do item para encontrar o arquivo correspondente
                safe_title = "".join(c for c in item_title if c.isalnum() or c in (' ', '-', '_')).rstrip()
                if not safe_title:
                    safe_title = f"item_{item_key}"
                
                possible_note_paths = [
                    f"02 - Processamento/Zotero_Inbox/{safe_title}.md",
                    f"Zotero_Inbox/{safe_title}.md",
                    f"{safe_title}.md",
                    f"01 - Entrada/{safe_title}.md"
                ]
                
                note_found = False
                for note_path in possible_note_paths:
                    note_file_path = Path(self.config['obsidian_vault_path']) / note_path
                    if note_file_path.exists():
                        # Valida o link entre Zotero e Obsidian
                        validation_result = self.validate_zotero_obsidian_link(item_key, note_path)
                        
                        # Verifica se padrões Fabric foram aplicados
                        if validation_result['status'] == 'VALIDATED':
                            fabric_validation = self.validate_fabric_pattern_application(
                                note_path, 
                                ['make_firac+', 'extract_key_notes', 'summarize']
                            )
                            validation_result['fabric_validation'] = fabric_validation
                        
                        validation_result['item_key'] = item_key
                        validation_result['item_title'] = item_title
                        validation_result['note_path'] = note_path
                        
                        validation_results.append(validation_result)
                        
                        if validation_result['status'] == 'VALIDATED':
                            valid_items += 1
                        
                        note_found = True
                        break
                
                if not note_found:
                    validation_results.append({
                        "status": "MISSING_NOTE",
                        "item_key": item_key,
                        "item_title": item_title,
                        "note_path": None,
                        "message": f"Nota correspondente não encontrada para o item {item_title}"
                    })
            
            return {
                "status": "VALIDATED",
                "collection_name": collection_name,
                "total_items": total_items,
                "items_with_notes": len([r for r in validation_results if r.get('note_path')]),
                "valid_items": valid_items,
                "validation_rate": valid_items / total_items if total_items > 0 else 0,
                "results": validation_results,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                "status": "ERROR",
                "message": f"Erro ao validar integridade das referências cruzadas: {str(e)}"
            }
    
    def generate_validation_report(self, validation_results: Dict, output_path: str = None) -> str:
        """
        Gera um relatório de validação em formato Markdown
        
        Args:
            validation_results: Resultados da validação
            output_path: Caminho para salvar o relatório (opcional)
            
        Returns:
            String com o conteúdo do relatório
        """
        report_lines = [
            "# Relatório de Validação de Referências Cruzadas",
            "",
            f"**Data/Hora:** {validation_results.get('timestamp', datetime.now().isoformat())}",
            f"**Coleção:** {validation_results.get('collection_name', 'Todas')}",
            "",
            "## Resumo",
            f"- **Itens totais:** {validation_results.get('total_items', 0)}",
            f"- **Itens com notas:** {validation_results.get('items_with_notes', 0)}",
            f"- **Itens válidos:** {validation_results.get('valid_items', 0)}",
            f"- **Taxa de validação:** {validation_results.get('validation_rate', 0):.2%}",
            "",
            "## Detalhes da Validação",
            "| Status | Item | Nota | Zotero Ref | Fabric |",
            "|--------|------|------|------------|--------|"
        ]
        
        for result in validation_results.get('results', []):
            status = result.get('status', 'UNKNOWN')
            item_title = result.get('item_title', 'Desconhecido')[:30] + "..." if len(result.get('item_title', '')) > 30 else result.get('item_title', 'Desconhecido')
            note_path = result.get('note_path', 'N/A')
            
            zotero_ref = "✓" if result.get('zotero_reference_found', False) else "✗"
            fabric_valid = "✓" if result.get('fabric_validation', {}).get('has_fabric_structure', False) else "✗"
            
            report_lines.append(f"| {status} | {item_title} | {note_path} | {zotero_ref} | {fabric_valid} |")
        
        report_content = "\n".join(report_lines)
        
        if output_path:
            report_file_path = Path(self.config['obsidian_vault_path']) / output_path
            report_file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(report_file_path, 'w', encoding='utf-8') as f:
                f.write(report_content)
        
        return report_content


# Função auxiliar para uso direto
def run_cross_reference_validation(collection_name: str = None, output_report: str = "Relatórios/validacao_referencias_cruzadas.md"):
    """
    Função auxiliar para executar a validação de referências cruzadas
    
    Args:
        collection_name: Nome da coleção para validar (None para todas)
        output_report: Caminho para salvar o relatório de validação
    """
    validator = CrossReferenceValidator()
    results = validator.validate_cross_references_integrity(collection_name)
    report = validator.generate_validation_report(results, output_report)
    
    print(f"Validação concluída. Taxa de validação: {results.get('validation_rate', 0):.2%}")
    print(f"Relatório salvo em: {output_report}")
    
    return results