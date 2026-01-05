# Agente: zotero_ingest

## Objetivo
Ingestão automatizada de documentos jurídicos para a biblioteca Zotero, com extração de metadados e classificação automática.

## Entradas esperadas
- Conteúdo bruto de documentos (PDF, HTML, texto)
- Metadados básicos (título, data, fonte)
- Tipo de documento (acórdão, lei, artigo, etc.)

## Saídas produzidas
- Entrada BibTeX formatada
- Anotações estruturadas em Markdown
- Classificação de tipo e tema jurídico
- Links para fontes oficiais

## Patterns do Fabric utilizados
- `extract_bibtex`
- `classify_document_type`
- `extract_key_dates`
- `generate_tags`

## Limites
- Não realiza análise substantiva do conteúdo jurídico
- Não substitui revisão humana para metadados críticos
- Depende de qualidade do texto de entrada