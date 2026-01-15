# Orquestrador Fabric-aware

## Propósito
O orquestrador Fabric-aware é responsável por escolher os patterns do Fabric adequados para cada fase do fluxo jurídico, definir parâmetros do modelo e encadear patterns em pipelines cognitivos.

## Responsabilidades
- Escolher qual pattern Fabric usar
- Definir parâmetros do modelo:
  - Temperatura
  - Top_p
  - Idioma
  - Formato de saída
- Encadear patterns (pipeline cognitivo)
- Produzir metadados rastreáveis (frontmatter YAML)
- Facilitar o trabalho do orquestrador maior, entregando tarefas já "cognitivamente compiladas"

## Não é responsável por
- Pesquisar diretamente
- Escrever peças finais
- Usar MCPs diretamente (exceto para auditoria)

## Fases do Fluxo Jurídico e Patterns Associados

### Fase 0 — Ingestão
- **Entrada**: Documentos brutos (DJe, decisões, peças, PDFs)
- **Possíveis patterns**: Nenhum (esta fase é pré-cognitiva)

### Fase 1 — Classificação Inicial
- **Entrada**: Documento jurídico
- **Possíveis patterns**:
  - `classify_document_type` - Classificar tipo de documento
  - `extract_key_notes` - Extrair notas e pontos chaves
  - `generate_tags` - Gerar tags semânticas
- **Saída esperada**: Metadados estruturados do documento

### Fase 2 — Formulação de Problemas Jurídicos
- **Entrada**: Documento com metadados
- **Possíveis patterns**:
  - `legal_problem_formulation` - Formular problemas jurídicos
  - `extract_key_notes` - Extrair pontos chaves relevantes
- **Saída esperada**: Problemas jurídicos explícitos

### Fase 3 — Pesquisa Profunda (Jurisprudência)
- **Entrada**: Problemas jurídicos formulados
- **Possíveis patterns**:
  - `web_search` - Pesquisa na web
  - `technical_search` - Pesquisa técnica
  - `research-topic` - Pesquisa guiada por tópico
- **Saída esperada**: Coleção de precedentes e doutrina relevantes

### Fase 4 — Análise de Pesquisa / Teses
- **Entrada**: Material coletado (precedentes, doutrina)
- **Possíveis patterns**:
  - `make_firac+` - Análise estruturada de decisões
  - `tese_classification` - Classificação de teses
  - `extract_key_notes` - Extração de pontos chaves
- **Saída esperada**: Teses classificadas e analisadas

### Fase 5 — Auditoria / Validador
- **Entrada**: Teses e precedentes analisados
- **Possíveis patterns**:
  - `fact-check` - Verificação de fatos
  - `compare-sources` - Comparação entre fontes
  - `extract_bibtex` - Geração de referências
- **Saída esperada**: Confirmação e validação de jurisprudência

### Fase 6 — Aquisição e Processamento de PDFs
- **Entrada**: Links para PDFs
- **Possíveis patterns**:
  - `summarize` - Geração de resumos
  - `make_firac+` - Análise estruturada
  - `extract_bibtex` - Geração de referências
- **Saída esperada**: Conteúdo estruturado dos PDFs

### Fase 7 — Organização Estratégica
- **Entrada**: Teses validadas e conteúdo estruturado
- **Possíveis patterns**:
  - `jurisprudence_weight_assessment` - Avaliação de peso argumentativo
  - `generate_tags` - Geração de tags para organização
- **Saída esperada**: TOC da petição e mapa argumentativo

### Fase 8 — Redação (Longform)
- **Entrada**: TOC e blocos argumentativos estruturados
- **Possíveis patterns**: Nenhum (esta fase é de redação, não de análise)
- **Saída esperada**: Texto contínuo da petição

## Parâmetros de Modelo por Fase

### Fase 1 (Classificação Inicial)
- **Temperatura**: 0.1 (baixa para consistência)
- **Top_p**: 0.8
- **Idioma**: Português
- **Formato de saída**: JSON estruturado

### Fase 2 (Formulação de Problemas)
- **Temperatura**: 0.3
- **Top_p**: 0.85
- **Idioma**: Português
- **Formato de saída**: Markdown com YAML frontmatter

### Fase 3 (Pesquisa Profunda)
- **Temperatura**: 0.5
- **Top_p**: 0.9
- **Idioma**: Português
- **Formato de saída**: Markdown com referências

### Fase 4 (Análise de Teses)
- **Temperatura**: 0.2
- **Top_p**: 0.8
- **Idioma**: Português
- **Formato de saída**: JSON com classificação

### Fase 5 (Auditoria)
- **Temperatura**: 0.1
- **Top_p**: 0.7
- **Idioma**: Português
- **Formato de saída**: JSON com verificação

### Fase 6 (Processamento de PDFs)
- **Temperatura**: 0.3
- **Top_p**: 0.85
- **Idioma**: Português
- **Formato de saída**: Combinação de JSON e Markdown

### Fase 7 (Organização Estratégica)
- **Temperatura**: 0.4
- **Top_p**: 0.85
- **Idioma**: Português
- **Formato de saída**: JSON com estrutura de petição

## Pipeline de Exemplo: Análise de Precedente

1. **Entrada**: Decisão judicial bruta
2. **Fase 1**: `classify_document_type` → Tipo: Acórdão
3. **Fase 2**: `extract_key_notes` → Pontos chaves identificados
4. **Fase 4**: `make_firac+` → Análise estruturada
5. **Fase 4**: `tese_classification` → Tese classificada como "leading case"
6. **Fase 5**: `fact-check` → Validação da existência
7. **Fase 6**: `extract_bibtex` → Geração de referência
8. **Saída**: Precedente analisado, validado e referenciado

## Integração com MCPs

O orquestrador Fabric-aware pode usar MCPs para:
- Verificação de informações (via `fact-check`)
- Comparação de fontes (via `compare-sources`)
- Pesquisa complementar (via `web_search`)

Mas NÃO para:
- Tomada de decisões jurídicas
- Análise substantiva de mérito
- Geração de conteúdo argumentativo

## Metadados de Execução

Cada execução do orquestrador deve gerar metadados contendo:
- Pattern(s) utilizado(s)
- Parâmetros do modelo
- Fase do fluxo
- Entrada recebida
- Saída produzida
- Timestamp
- Confiança estimada