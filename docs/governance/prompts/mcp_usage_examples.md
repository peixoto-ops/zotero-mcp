# Exemplos Práticos de Uso dos MCPs pelos Agentes

## Visão Geral

Este documento fornece exemplos práticos de como os diferentes agentes utilizam os servidores MCP em situações reais do fluxo de trabalho jurídico automatizado.

## Exemplos por Agente

### 1. strategic-organization-agent

**Cenário**: Geração de TOC para uma petição de nulidade de prisão preventiva

**Uso do MCP**: obsidian-vault para salvar o TOC gerado

**Exemplo de Código/Instrução**:
```
Quando o strategic-organization-agent completar a geração do TOC,
ele deve usar o obsidian-vault para salvar o resultado como uma
nota Markdown no vault, com metadados apropriados para futura
referência e continuidade do trabalho.

Exemplo de operação:
- Título da nota: "TOC_Pedido_Nulidade_Prisao_Preventiva_[data]"
- Conteúdo: TOC estruturado em Markdown
- Frontmatter YAML: 
  ```
  tipo_documento: "toc"
  processo_relacionado: "1000000-00.2023.8.26.0000"
  data_geracao: "2026-01-08"
  status: "em_elaboracao"
  tags: ["peticao", "nulidade", "prisao", "preventiva"]
  ```
```

### 2. jurisprudencia-auditor

**Cenário**: Verificação da atualidade de um precedente do STJ

**Uso do MCP**: zotero-mcp para verificar existência e status do precedente

**Exemplo de Código/Instrução**:
```
Quando receber um precedente para auditoria (ex: REsp 1234567/SP),
o jurisprudencia-auditor deve usar o zotero-mcp para:

1. Buscar o precedente: zotero_search_items("REsp 1234567/SP")
2. Obter metadados: zotero_item_metadata(item_id)
3. Verificar se ainda está vigente comparando com decisões recentes
4. Registrar a confirmação de atualidade ou qualquer mudança de status

Exemplo de verificação:
- Buscar o precedente no Zotero: zotero_search_items("REsp 1234567/SP")
- Obter metadados: zotero_item_metadata(item_id)
- Verificar se ainda está vigente comparando com decisões recentes
- Registrar a confirmação de atualidade ou qualquer mudança de status

Exemplo de verificação:
- Precedente ainda é válido?
- Foi superado por decisão posterior?
- Ainda é aplicável à situação concreta?
```

### 3. juridical-longform-writer

**Cenário**: Salvamento da petição final no sistema de conhecimento

**Uso do MCP**: obsidian-vault para persistência da petição completa

**Exemplo de Código/Instrução**:
```
Após completar a redação da petição, o juridical-longform-writer
deve usar o obsidian-vault para:

1. Criar uma nova nota com o conteúdo da petição
2. Aplicar frontmatter YAML com metadados relevantes
3. Vincular a nota ao processo e ao TOC original

Exemplo de frontmatter:
```
tipo_documento: "peticao"
titulo: "Petição Inicial - Ação de Nulidade de Prisão"
processo: "1000000-00.2023.8.26.0000"
data_elaboracao: "2026-01-08"
status: "concluida"
fase_processo: "contestado"
tags: ["inicial", "nulidade", "prisao", "preventiva"]
toc_referencia: "TOC_Pedido_Nulidade_Prisao_Preventiva_2026-01-08"
jurisprudencia_usada: ["REsp 1234567/SP", "RE 9876543/SP"]
```
```

### 4. pdf-processor-legal

**Cenário**: Análise FIRAC+ de um acórdão do STJ

**Uso do MCP**: obsidian-costum-patterns para aplicar o pattern de análise

**Exemplo de Código/Instrução**:
```
Ao receber um PDF de acórdão para análise, o pdf-processor-legal
deve usar o obsidian-costum-patterns para aplicar o pattern FIRAC+:

1. Acessar o pattern make_firac+: read_note("make_firac+/system.md")
2. Aplicar a análise FIRAC+ ao conteúdo do acórdão
3. Estruturar a saída conforme o formato definido no pattern

Exemplo de operação:
- Ler o pattern FIRAC+ do diretório de patterns
- Aplicar os passos definidos no pattern ao acórdão
- Gerar saída estruturada com Facts, Issues, Rules, Application, Conclusion
```

### 5. jurisprudence-researcher

**Cenário**: Pesquisa de jurisprudência sobre prisão preventiva

**Uso do MCP**: obsidian-costum-patterns para aplicar patterns de pesquisa e zotero-mcp para busca na biblioteca

**Exemplo de Código/Instrução**:
```
Durante uma pesquisa sobre prisão preventiva, o jurisprudence-researcher
deve usar:

1. obsidian-costum-patterns para aplicar research-topic:
   - Acessar o pattern research-topic
   - Estruturar a pesquisa de forma sistemática
   - Aplicar critérios de inclusão e exclusão

2. zotero-mcp (futuro) para buscar precedentes:
   - Executar zotero_search_items("prisão preventiva")
   - Filtrar resultados por tribunal e data
   - Obter metadados completos dos precedentes relevantes

Exemplo de workflow:
- Aplicar pattern de pesquisa para definir os critérios
- Buscar precedentes relevantes na biblioteca Zotero
- Classificar e organizar os resultados
- Preparar sumário para análise mais profunda
```

### 6. teses-analyst

**Cenário**: Classificação de teses jurídicas de acórdãos sobre prisão preventiva

**Uso do MCP**: obsidian-costum-patterns para aplicar pattern de classificação

**Exemplo de Código/Instrução**:
```
Ao analisar teses jurídicas de acórdãos, o teses-analyst
deve usar o obsidian-costum-patterns para aplicar o pattern
de classificação de teses:

1. Acessar o pattern tese_classification: read_note("tese_classification/system.md")
2. Aplicar critérios de classificação às teses identificadas
3. Determinar o tipo da tese (leading case, julgado de consolidação, etc.)

Exemplo de classificação:
- Tese: "A prisão preventiva não pode ser decretada apenas com base na gravidade do crime"
- Classificação: "leading_case" 
- Nível de autoridade: "alto"
- Aplicabilidade: "direta"
- Órgão julgador: "STJ"
- Data: "2023-05-15"
```

### 7. process-classification-agent

**Cenário**: Classificação de um novo processo recebido

**Uso do MCP**: obsidian-vault para armazenar informações de classificação

**Exemplo de Código/Instrução**:
```
Após classificar um processo, o process-classification-agent
deve usar o obsidian-vault para:

1. Criar ou atualizar uma nota com as informações de classificação
2. Vincular o processo a categorias e temas jurídicos
3. Registrar metadados para futura recuperação

Exemplo de conteúdo da nota:
```
---
tipo_documento: "classificacao_processo"
numero_processo: "1000000-00.2023.8.26.0000"
classe: "Ação Penal"
area_direito: "Direito Penal"
assunto_principal: "Prisão Preventiva"
tribunal: "TJRJ"
data_distribuicao: "2023-01-15"
status: "em_julgamento"
tags: ["penal", "prisao", "preventiva", "acao"]
---

# Classificação do Processo

## Dados Básicos
- Número: 1000000-00.2023.8.26.0000
- Classe: Ação Penal
- Assunto: Prisão Preventiva

## Análise Inicial
[Resumo da análise inicial do processo]
```
```

## Exemplos de Integração entre Agentes e MCPs

### Exemplo 1: Workflow Completo de Análise de Precedente

1. **jurisprudence-researcher** encontra precedente e usa `zotero-mcp` para obter metadados
2. **pdf-processor-legal** aplica pattern FIRAC+ via `obsidian-costum-patterns`
3. **teses-analyst** classifica tese via `obsidian-costum-patterns`
4. **jurisprudencia-auditor** verifica atualidade via `zotero-mcp` (futuro)
5. **strategic-organization-agent** organiza insights e salva no `obsidian-vault`

### Exemplo 2: Workflow de Geração de Petição

1. **strategic-organization-agent** gera TOC e salva no `obsidian-vault`
2. **jurisprudence-researcher** pesquisa jurisprudência usando `zotero-mcp` e `obsidian-costum-patterns`
3. **teses-analyst** analisa teses usando `obsidian-costum-patterns`
4. **juridical-longform-writer** acessa TOC e gera conteúdo
5. **juridical-longform-writer** salva petição final no `obsidian-vault`

## Verificação do Funcionamento do Zotero MCP

### Comandos para Verificar o Servidor
- Verificar status do banco de dados: `/home/peixoto/.mcp/zotero/venv/bin/zotero-mcp db-status`
- Inspeccionar documentos indexados: `/home/peixoto/.mcp/zotero/venv/bin/zotero-mcp db-inspect`
- Atualizar o banco de dados: `/home/peixoto/.mcp/zotero/venv/bin/zotero-mcp update-db`
- Verificar configuração: `/home/peixoto/.mcp/zotero/venv/bin/zotero-mcp setup-info`

### Status Atual
- Total de itens indexados: 440
- Banco de dados funcional e atualizado
- API local do Zotero habilitada e conectada
- Servidor pronto para uso pelos agentes

## Boas Práticas de Uso

### 1. Consistência na Persistência
- Sempre usar metadados YAML consistentes ao salvar no `obsidian-vault`
- Seguir convenções de nomenclatura para facilitar a recuperação
- Manter estrutura de diretórios organizada

### 2. Validação de Resultados
- Verificar a qualidade dos dados antes de persistir
- Validar a integridade das informações recebidas dos MCPs
- Registrar eventuais inconsistências para revisão

### 3. Rastreabilidade
- Manter registro de quais MCPs foram usados em cada operação
- Documentar o nível de confiança das informações obtidas
- Registrar eventuais falhas ou limitações encontradas

### 4. Eficiência
- Agrupar operações quando possível para reduzir chamadas aos MCPs
- Usar caches apropriados para informações frequentemente acessadas
- Planejar operações para maximizar o uso paralelo dos recursos