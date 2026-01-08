# Catálogo Fabril - Metadados dos Patterns

## Visão Geral

Este catálogo contém os metadados dos patterns do Fabric utilizados no sistema jurídico automatizado. Cada pattern é descrito com informações sobre seu propósito, quando usar, com quais outros patterns costuma aparecer e em que fase do fluxo jurídico.

## Estrutura do Catálogo

Cada entry no catálogo contém:

- **Nome**: Nome do pattern
- **Propósito**: Descrição do que o pattern faz
- **Quando usar**: Situações em que o pattern é útil
- **Combinável com**: Outros patterns que costumam ser usados em conjunto
- **Fase do fluxo**: Em que fase do fluxo jurídico o pattern é mais útil
- **Tipo de saída**: Formato esperado da saída

---

## Patterns de Análise Jurídica

### FIRAC+

**Nome**: `make_firac+`

**Propósito**: Estruturar decisões judiciais usando o formato FIRAC+ (Facts, Issues, Rules, Application, Conclusion + Critical Review)

**Quando usar**: Ao analisar decisões judiciais para extrair elementos estruturais

**Combinável com**: `extract_key_notes`, `classify_document_type`, `generate_tags`

**Fase do fluxo**: Análise Jurídica Estruturada (Fase 4)

**Tipo de saída**: Markdown com frontmatter YAML

---

### Extract Key Notes

**Nome**: `extract_key_notes`

**Propósito**: Extrair notas e pontos chaves de textos jurídicos

**Quando usar**: Ao processar documentos jurídicos para identificar pontos importantes

**Combinável com**: `make_firac+`, `classify_document_type`, `generate_tags`

**Fase do fluxo**: Análise Jurídica Estruturada (Fase 4)

**Tipo de saída**: Markdown com frontmatter YAML

---

### Classify Document Type

**Nome**: `classify_document_type`

**Propósito**: Classificar o tipo de documento jurídico

**Quando usar**: Na classificação inicial de documentos

**Combinável com**: `extract_key_notes`, `make_firac+`, `generate_tags`

**Fase do fluxo**: Classificação Inicial (Fase 1)

**Tipo de saída**: JSON com tipo de documento

---

### Generate Tags

**Nome**: `generate_tags`

**Propósito**: Gerar tags semânticas para documentos jurídicos

**Quando usar**: Após classificação para indexação e recuperação

**Combinável com**: `classify_document_type`, `extract_key_notes`, `make_firac+`

**Fase do fluxo**: Classificação Inicial (Fase 1) e Análise (Fase 4)

**Tipo de saída**: JSON com lista de tags

---

## Patterns de Extração e Processamento

### Extract Key Dates

**Nome**: `extract_key_dates`

**Propósito**: Extrair datas importantes de documentos jurídicos

**Quando usar**: Ao analisar cronologia de eventos em processos

**Combinável com**: `extract_case_numbers`, `extract_tribunal_info`

**Fase do fluxo**: Análise Jurídica Estruturada (Fase 4)

**Tipo de saída**: JSON com datas e contexto

---

### Extract Case Numbers

**Nome**: `extract_case_numbers`

**Propósito**: Extrair números de processos de documentos jurídicos

**Quando usar**: Ao identificar e rastrear processos específicos

**Combinável com**: `extract_key_dates`, `extract_tribunal_info`

**Fase do fluxo**: Análise Jurídica Estruturada (Fase 4)

**Tipo de saída**: JSON com números de processos

---

### Extract Tribunal Info

**Nome**: `extract_tribunal_info`

**Propósito**: Extrair informações sobre tribunais e órgãos julgadores

**Quando usar**: Ao identificar jurisdição e competência

**Combinável com**: `extract_case_numbers`, `extract_key_dates`

**Fase do fluxo**: Análise Jurídica Estruturada (Fase 4)

**Tipo de saída**: JSON com informações do tribunal

---

## Patterns de Geração de Referências

### Extract BibTeX

**Nome**: `extract_bibtex`

**Propósito**: Gerar entradas BibTeX a partir de documentos jurídicos

**Quando usar**: Ao criar referências bibliográficas para jurisprudência

**Combinável com**: `make_firac+`, `extract_key_notes`

**Fase do fluxo**: Organização Estratégica (Fase 6)

**Tipo de saída**: Texto formatado BibTeX

---

### Generate Summary

**Nome**: `summarize`

**Propósito**: Criar resumos concisos de documentos jurídicos

**Quando usar**: Ao precisar de visão geral rápida de documentos longos

**Combinável com**: `extract_key_notes`, `make_firac+`

**Fase do fluxo**: Análise Jurídica Estruturada (Fase 4)

**Tipo de saída**: Markdown com resumo

---

## Patterns de Pesquisa Profunda

### Web Search

**Nome**: `web_search`

**Propósito**: Realizar pesquisas na web para complementar análise jurídica

**Quando usar**: Ao precisar de informações adicionais sobre jurisprudência ou doutrina

**Combinável com**: `summarize`, `extract_key_notes`

**Fase do fluxo**: Pesquisa Profunda (Fase 3)

**Tipo de saída**: Markdown com resultados da pesquisa

---

### Technical Search

**Nome**: `technical_search`

**Propósito**: Realizar pesquisas técnicas e de programação

**Quando usar**: Ao precisar de informações técnicas para desenvolvimento

**Combinável com**: `research-topic`, `fact-check`

**Fase do fluxo**: Pesquisa Profunda (Fase 3)

**Tipo de saída**: Markdown com resultados técnicos

---

## Patterns de Validação e Auditoria

### Fact Check

**Nome**: `fact-check`

**Propósito**: Verificar a veracidade de alegações em documentos jurídicos

**Quando usar**: Ao auditar informações e precedentes citados

**Combinável com**: `compare-sources`, `research-topic`

**Fase do fluxo**: Auditoria e Validação (Fase 5)

**Tipo de saída**: Markdown com verificação de fatos

---

### Compare Sources

**Nome**: `compare-sources`

**Propósito**: Comparar informações de múltiplas fontes

**Quando usar**: Ao verificar consistência entre diferentes precedentes

**Combinável com**: `fact-check`, `research-topic`

**Fase do fluxo**: Auditoria e Validação (Fase 5)

**Tipo de saída**: Markdown com comparação

---

## Patterns Personalizados Jurídicos

### Legal Problem Formulation

**Nome**: `legal_problem_formulation`

**Propósito**: Formular problemas jurídicos a partir de fatos e decisões

**Quando usar**: Na fase de formulação de problemas jurídicos

**Combinável com**: `make_firac+`, `extract_key_notes`

**Fase do fluxo**: Formulação de Problemas (Fase 2)

**Tipo de saída**: Markdown com problemas jurídicos formulados

---

### Tese Classification

**Nome**: `tese_classification`

**Propósito**: Classificar teses jurídicas por tipo e aplicabilidade

**Quando usar**: Ao analisar e categorizar teses para uso em argumentação

**Combinável com**: `make_firac+`, `generate_tags`

**Fase do fluxo**: Análise Jurídica Estruturada (Fase 4)

**Tipo de saída**: JSON com classificação da tese

---

### Jurisprudence Weight Assessment

**Nome**: `jurisprudence_weight_assessment`

**Propósito**: Avaliar o peso argumentativo de precedentes

**Quando usar**: Ao determinar força de precedentes para argumentação

**Combinável com**: `fact-check`, `compare-sources`

**Fase do fluxo**: Organização Estratégica (Fase 6)

**Tipo de saída**: JSON com avaliação de peso

---

## Padrões de Uso

### Sequências Comuns

#### Sequência de Classificação Inicial
1. `classify_document_type`
2. `extract_key_notes`
3. `generate_tags`

#### Sequência de Análise FIRAC+
1. `extract_key_notes`
2. `make_firac+`
3. `generate_tags`

#### Sequência de Auditoria
1. `fact-check`
2. `compare-sources`
3. `extract_bibtex`

---

## Notas de Implementação

Este catálogo é gerado automaticamente a partir dos patterns existentes e serve como referência para o orquestrador Fabric-aware escolher os patterns apropriados em cada fase do fluxo jurídico.