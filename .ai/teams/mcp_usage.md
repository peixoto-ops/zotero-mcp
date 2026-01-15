# Uso dos MCPs pelas Equipes

## Visão Geral

Este documento descreve como as equipes de agentes podem utilizar os servidores MCP (Model Context Protocol) para executar tarefas em paralelo e consolidar resultados de forma eficiente no fluxo de trabalho jurídico automatizado.

## Estrutura de Equipes com MCPs

### 1. Equipe de Análise de Precedentes

**Objetivo**: Analisar um precedente em profundidade com múltiplos agentes especializados.

**Composição**:
- `pdf-processor-legal`: Análise FIRAC+ do precedente
- `teses-analyst`: Classificação da tese jurídica
- `jurisprudencia-auditor`: Verificação de existência e atualidade
- `pdf-processor-legal`: Geração de BibTeX

**Uso de MCPs**:
- `obsidian-costum-patterns`: Para aplicar patterns de análise FIRAC+ e classificação de teses
- `zotero-mcp`: Para verificar existência e obter metadados bibliográficos

**Exemplo de Workflow**:
```
1. Equipe recebe um precedente para análise
2. pdf-processor-legal aplica pattern FIRAC+ via obsidian-costum-patterns
3. teses-analyst aplica pattern de classificação via obsidian-costum-patterns
4. jurisprudencia-auditor verifica via zotero-mcp (quando disponível)
5. pdf-processor-legal gera BibTeX via zotero-mcp (quando disponível)
6. Resultados são consolidados em um formato estruturado
```

### 2. Equipe de Elaboração de Tese

**Objetivo**: Desenvolver uma tese jurídica completa com análise de jurisprudência, doutrina e aplicabilidade.

**Composição**:
- `jurisprudence-researcher`: Pesquisa de jurisprudência
- `teses-analyst`: Análise e classificação da tese
- `legal-problem-formulator`: Formulação de problemas jurídicos
- `pdf-processor-legal`: Análise de documentos suporte

**Uso de MCPs**:
- `obsidian-costum-patterns`: Para aplicar patterns de pesquisa e análise de teses
- `zotero-mcp (futuro)`: Para pesquisa na biblioteca Zotero e obtenção de referências

**Exemplo de Workflow**:
```
1. Equipe recebe uma tese para desenvolvimento
2. jurisprudence-researcher pesquisa precedentes via zotero-mcp (futuro)
3. teses-analyst aplica pattern de classificação via obsidian-costum-patterns
4. legal-problem-formulator formula problemas via obsidian-costum-patterns
5. pdf-processor-legal analisa documentos via obsidian-costum-patterns
6. Resultados são consolidados com classificação e referências
```

### 3. Equipe de Organização de Petição

**Objetivo**: Organizar e estruturar uma petição com base em pesquisa e análise prévias.

**Composição**:
- `strategic-organization-agent`: Geração de TOC e mapa argumentativo
- `process-classification-agent`: Classificação do tipo processual
- `legal-problem-formulator`: Formulação de problemas jurídicos
- `teses-analyst`: Análise de teses aplicáveis

**Uso de MCPs**:
- `obsidian-vault`: Para salvar e recuperar TOCs e informações processuais
- `obsidian-costum-patterns`: Para aplicar patterns de formulação e análise

**Exemplo de Workflow**:
```
1. Equipe recebe informações para organizar uma petição
2. strategic-organization-agent gera TOC e salva no obsidian-vault
3. process-classification-agent classifica o processo
4. legal-problem-formulator formula problemas via obsidian-costum-patterns
5. teses-analyst analisa teses aplicáveis via obsidian-costum-patterns
6. TOC consolidado é salvo no obsidian-vault
```

## Padrões de Uso de MCPs por Equipes

### 1. Padrão de Persistência em Equipe
- As equipes devem usar o `obsidian-vault` para persistência de artefatos coletivos
- Cada resultado parcial deve ser identificado com a origem do agente responsável
- Os artefatos consolidados devem ser salvos com metadados de equipe e contexto

### 2. Padrão de Análise Paralela
- Cada agente da equipe pode usar o `obsidian-costum-patterns` para aplicar patterns de análise específicos
- As análises devem ser realizadas em paralelo para maximizar eficiência
- Os resultados devem ser estruturados de forma compatível com o processo de consolidação

### 3. Padrão de Verificação Cruzada
- Quando disponível, o `zotero-mcp` deve ser usado por múltiplos agentes da equipe para verificação cruzada
- As verificações devem ser registradas com nível de confiança e fonte
- Conflitos de informação devem ser destacados para revisão humana

## Exemplos de Implementação de Equipes com MCPs

### Exemplo de Equipe: Análise de Precedente STJ

```yaml
nome: "Equipe de Análise de Precedente STJ"
descricao: "Analisa profundamente um precedente do STJ"
contexto_compartilhado:
  tipo: "precedente_STJ"
  entrada: "acordao_STJ_bruto"
  objetivo: "analisar_tese_jurisprudencial"
tarefas:
  - nome: "analise_firac"
    agente: "pdf-processor-legal"
    pattern: "make_firac+"
    entrada: "acordao_STJ_bruto"
    mcp_usado: "obsidian-costum-patterns"
    saida_formato: "markdown_com_yaml"
  - nome: "classificacao_tese"
    agente: "teses-analyst"
    pattern: "tese_classification"
    entrada: "teses_extraidas"
    mcp_usado: "obsidian-costum-patterns"
    saida_formato: "json"
  - nome: "verificacao_existencia"
    agente: "jurisprudencia-auditor"
    pattern: "fact-check"
    entrada: "referencias_juridicas"
    mcp_usado: "zotero-mcp"  # atualmente disponível
    saida_formato: "json"
  - nome: "geracao_bibtex"
    agente: "pdf-processor-legal"
    pattern: "extract_bibtex"
    entrada: "referencias_juridicas"
    mcp_usado: "zotero-mcp"  # atualmente disponível
    saida_formato: "text"
consolidacao:
  estrategia: "combinacao_estruturada"
  saida_final: "precedente_STJ_analisado_completo"
  persistencia: "obsidian-vault"
```

### Exemplo de Equipe: Elaboração de Tese para Apelação

```yaml
nome: "Equipe de Elaboração de Tese para Apelação"
descricao: "Desenvolve uma tese jurídica para uso em apelação"
contexto_compartilhado:
  tipo: "tese_apelacao"
  entrada: "base_juridica_documento"
  objetivo: "desenvolver_tese_juridica_apelacao"
tarefas:
  - nome: "pesquisa_jurisprudencia"
    agente: "jurisprudence-researcher"
    pattern: "research-topic"
    entrada: "base_juridica_documento"
    mcp_usado: "zotero-mcp"  # atualmente disponível
    saida_formato: "json_lista_precedentes"
  - nome: "analise_doutrina"
    agente: "jurisprudence-researcher"
    pattern: "web_search"
    entrada: "base_juridica_documento"
    mcp_usado: "obsidian-costum-patterns"
    saida_formato: "markdown_pesquisa"
  - nome: "classificacao_tese"
    agente: "teses-analyst"
    pattern: "tese_classification"
    entrada: "tese_bruta"
    mcp_usado: "obsidian-costum-patterns"
    saida_formato: "json"
  - nome: "avaliacao_aplicabilidade"
    agente: "teses-analyst"
    pattern: "jurisprudence_weight_assessment"
    entrada: "tese_classificada"
    mcp_usado: "obsidian-costum-patterns"
    saida_formato: "json"
consolidacao:
  estrategia: "síntese_hierárquica"
  saida_final: "tese_apelacao_completa"
  persistencia: "obsidian-vault"
```

## Considerações de Coordenação

### 1. Sincronização de Contexto
- O contexto compartilhado deve ser atualizado e distribuído para todos os agentes da equipe
- Mudanças no contexto devem ser propagadas imediatamente a todos os membros
- O histórico de alterações de contexto deve ser mantido para auditoria

### 2. Gestão de Dependências
- As tarefas que dependem de resultados de outras tarefas devem aguardar a conclusão
- As dependências devem ser declaradas explicitamente na definição da equipe
- Estratégias de processamento paralelo devem maximizar a independência das tarefas

### 3. Tratamento de Falhas
- Se um agente falhar ao acessar um MCP, a equipe deve ter estratégias de fallback
- Resultados parciais devem ser preservados mesmo em caso de falha parcial
- A equipe deve ser capaz de continuar com funcionalidades reduzidas se necessário

## Boas Práticas para Equipes com MCPs

1. **Especialização**: Cada agente da equipe deve usar os MCPs mais apropriados para sua especialidade
2. **Eficiência**: Planejar o uso de MCPs para maximizar o paralelismo e minimizar dependências
3. **Rastreabilidade**: Manter registro de quais MCPs foram usados por quais agentes e quando
4. **Resiliência**: Projetar equipes que possam operar mesmo com alguns MCPs indisponíveis
5. **Escalabilidade**: Estruturar o uso de MCPs para permitir fácil adição de novos agentes ou MCPs