# Integração dos MCPs com Subagentes

## Visão Geral

Este documento descreve como os diferentes servidores MCP (Model Context Protocol) podem ser utilizados pelos subagentes especializados no fluxo de trabalho jurídico automatizado.

## Subagentes e Seus Usos dos MCPs

### 1. jurisprudencia-auditor

**Função**: Verificar a existência, atualidade e confiabilidade de precedentes jurídicos.

**MCPs Utilizados**:
- **zotero-mcp**: Para verificar a existência e atualidade de precedentes na biblioteca Zotero
  - `zotero_search_items`: Buscar precedentes específicos
  - `zotero_item_metadata`: Obter metadados detalhados
  - `zotero_item_fulltext`: Acessar conteúdo completo quando necessário

**Exemplo de Uso**:
```
Quando receber um precedente para auditoria, o jurisprudencia-auditor
poderá usar o zotero-mcp para confirmar a existência do precedente,
verificar se ainda está vigente e obter detalhes adicionais.
```

### 2. strategic-organization-agent

**Função**: Organizar teses, evidências e argumentos em planos estratégicos, gerar TOCs e criar mapas argumentativos.

**MCPs Utilizados**:
- **obsidian-vault**: Para salvar TOCs e mapas argumentativos gerados
  - `write_note`: Salvar TOC da petição
  - `read_note`: Recuperar informações de tópicos anteriores
  - `search_notes`: Encontrar tópicos relacionados

**Exemplo de Uso**:
```
Após gerar um TOC, o strategic-organization-agent pode usar o
obsidian-vault para salvá-lo como uma nota Markdown no vault,
facilitando o acesso futuro e a continuidade do trabalho.
```

### 3. juridical-longform-writer

**Função**: Compor documentos jurídicos completos a partir de TOCs e blocos argumentativos pré-estruturados.

**MCPs Utilizados**:
- **obsidian-vault**: Para salvar peças processuais prontas
  - `write_note`: Salvar a petição final
  - `read_note`: Recuperar informações contextuais
  - `update_frontmatter`: Atualizar metadados da nota

**Exemplo de Uso**:
```
Após completar uma petição, o juridical-longform-writer pode
usar o obsidian-vault para salvá-la no vault com metadados
apropriados para futura referência e organização.
```

### 4. pdf-processor-legal

**Função**: Processar documentos jurídicos em PDF para gerar resumos, análises FIRAC+ e metadados bibliográficos.

**MCPs Utilizados**:
- **obsidian-costum-patterns**: Para aplicar patterns de análise jurídica
  - `read_note`: Acessar patterns de análise
  - `list_directory`: Encontrar patterns relevantes
- **zotero-mcp (futuro)**: Para obter metadados bibliográficos
  - `zotero_item_metadata`: Obter informações bibliográficas

**Exemplo de Uso**:
```
Ao processar um PDF de decisão judicial, o pdf-processor-legal
pode usar o obsidian-costum-patterns para aplicar o pattern
make_firac+ e estruturar a análise da decisão.
```

### 5. jurisprudence-researcher

**Função**: Realizar pesquisas profundas em precedentes e fontes qualificadas.

**MCPs Utilizados**:
- **obsidian-costum-patterns**: Para aplicar patterns de pesquisa e análise
  - `read_note`: Acessar patterns de pesquisa
  - `list_directory`: Encontrar patterns relevantes
- **zotero-mcp**: Para pesquisar na biblioteca Zotero
  - `zotero_search_items`: Buscar precedentes relevantes

**Exemplo de Uso**:
```
Durante uma pesquisa de precedentes, o jurisprudence-researcher
pode usar o obsidian-costum-patterns para aplicar o pattern
research-topic e estruturar a pesquisa de forma sistemática.
```

### 6. teses-analyst

**Função**: Analisar material de pesquisa (especialmente jurisprudência) e classificar teses jurídicas.

**MCPs Utilizados**:
- **obsidian-costum-patterns**: Para aplicar patterns de análise de teses
  - `read_note`: Acessar patterns de classificação de teses
  - `list_directory`: Encontrar patterns relevantes

**Exemplo de Uso**:
```
Ao analisar uma tese jurídica, o teses-analyst pode usar o
obsidian-costum-patterns para aplicar o pattern tese_classification
e categorizar a tese de acordo com critérios estabelecidos.
```

### 7. process-classification-agent

**Função**: Identificar rapidamente a área do direito, temas centrais e tipo de ato processual.

**MCPs Utilizados**:
- **obsidian-vault**: Para armazenar classificações de processos
  - `write_note`: Salvar informações de classificação
  - `search_notes`: Encontrar processos similares

**Exemplo de Uso**:
```
Após classificar um processo, o process-classification-agent
pode usar o obsidian-vault para salvar as informações de
classificação para referência futura e análise estatística.
```

### 8. legal-problem-formulator

**Função**: Transformar fatos, decisões e contexto processual em problemas jurídicos formulados.

**MCPs Utilizados**:
- **obsidian-costum-patterns**: Para aplicar patterns de formulação de problemas
  - `read_note`: Acessar patterns de formulação de problemas
  - `list_directory`: Encontrar patterns relevantes

**Exemplo de Uso**:
```
Ao formular um problema jurídico, o legal-problem-formulator
pode usar o obsidian-costum-patterns para aplicar o pattern
legal_problem_formulation e estruturar o problema de forma clara.
```

## Padrões de Integração

### 1. Padrão de Persistência
- Subagentes que geram artefatos devem usar o `obsidian-vault` para persistência
- Subagentes que realizam análises devem usar o `obsidian-costum-patterns` para aplicar padrões de análise
- Subagentes que verificam informações devem usar o `zotero-mcp` (quando disponível) para validação

### 2. Padrão de Contexto
- Subagentes devem buscar contexto adicional usando os MCPs apropriados
- O contexto deve ser mantido mínimo e relevante para a tarefa específica
- A proveniência do contexto deve ser rastreável

### 3. Padrão de Validação
- Subagentes devem validar informações críticas usando os MCPs disponíveis
- A confiabilidade das fontes deve ser verificada quando possível
- As validações devem ser registradas para auditoria futura

## Exemplos de Workflows com MCPs

### Workflow de Análise de Precedente
1. `jurisprudence-researcher` encontra precedente
2. `pdf-processor-legal` aplica pattern FIRAC+ via `obsidian-costum-patterns`
3. `teses-analyst` classifica tese via `obsidian-costum-patterns`
4. `jurisprudencia-auditor` verificará via `zotero-mcp` (futuro)
5. `strategic-organization-agent` organiza insights

### Workflow de Geração de Petição
1. `strategic-organization-agent` gera TOC
2. `obsidian-vault` armazena TOC
3. `juridical-longform-writer` acessa TOC e gera conteúdo
4. `obsidian-vault` armazena petição final
5. `process-classification-agent` classifica e armazena metadados

## Considerações de Segurança e Governança

1. **Acesso Controlado**: Apenas subagentes autorizados devem acessar cada MCP
2. **Registro de Atividades**: Todas as interações com MCPs devem ser registradas
3. **Validação de Entradas**: Dados recebidos dos MCPs devem ser validados antes do uso
4. **Tratamento de Erros**: Subagentes devem lidar adequadamente com falhas de MCP