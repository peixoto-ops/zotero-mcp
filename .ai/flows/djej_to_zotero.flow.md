# Fluxo: djej_to_zotero

## Objetivo
Pipeline completo para ingestão de acórdãos do Diário da Justiça Eletrônico (DJ-e) para a biblioteca Zotero, com extração de metadados e fichamento automático.

## Etapas do fluxo

### 1. Extração de conteúdo
- Download de PDF do DJ-e
- Extração de texto com `pdftotext`
- Limpeza de cabeçalhos e rodapés

### 2. Identificação de documentos
- Pattern: `classify_document_type`
- Identificação de acórdãos, decisões monocráticas, etc.

### 3. Extração de metadados
- Pattern: `extract_key_dates`
- Pattern: `extract_case_numbers`
- Pattern: `extract_tribunal_info`

### 4. Geração de BibTeX
- Pattern: `extract_bibtex`
- Formatação específica para jurisprudência

### 5. Fichamento automático
- Pattern: `firac_plus` para estruturação do conteúdo
- Pattern: `extract_key_notes` para pontos relevantes

### 6. Importação para Zotero
- Criação de item no Zotero via API
- Anexação de PDF original
- Adição de anotações estruturadas

## Validação
- Schema: `document_classification.schema.json`
- Verificação de campos obrigatórios
- Conformidade com padrões ABNT

## Saída final
- Item completo no Zotero com anotações
- Link bidirecional com Obsidian (se configurado)
- Classificação temática automática