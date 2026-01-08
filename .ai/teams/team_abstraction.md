# Abstração de Equipes

## Visão Geral
Uma equipe é um agrupamento temporário de subagentes especializados, criado para atuar sobre um mesmo artefato cognitivo (ex.: um tópico do TOC, uma tese, um conjunto de julgados). As equipes permitem execução paralela de tarefas independentes com consolidação posterior.

## Princípios de Design

### 1. Equipe ≠ Agente
- Equipes **não têm inteligência própria**
- Equipes **não decidem objetivos**
- Equipes **executam tarefas paralelas sobre o mesmo contexto mínimo**

### 2. Quando usar equipes
Use equipes quando:
- Há **um mesmo insumo comum**
- Tarefas são **independentes entre si**
- Resultados precisam ser **consolidados depois**

### 3. Contexto mínimo
Cada agente da equipe recebe **apenas o contexto necessário** para sua tarefa específica, evitando sobrecarga.

## Estrutura de uma Equipe

### Definição de Equipe
```
Equipe: [Nome da Equipe]
Contexto Compartilhado: [Dados mínimos comuns]
Tarefas:
  - Tarefa 1: [Descrição] → [Agente Responsável] → [Pattern(s)]
  - Tarefa 2: [Descrição] → [Agente Responsável] → [Pattern(s)]
  - ...
Consolidação: [Como os resultados serão combinados]
```

## Exemplo Canônico: Equipe por Tópico do TOC

### Contexto Compartilhado
- Tópico do TOC: "Nulidade da prisão preventiva"
- Base jurídica: [Artigos relevantes]
- Fatos principais: [Resumo factual]

### Tarefas da Equipe

#### 1. Checagem da Fonte
- **Agente**: `agente_auditoria_jurisprudencia`
- **Pattern**: `fact-check`
- **Entrada**: Referências jurídicas do tópico
- **Saída**: Validação de existência e atualidade

#### 2. Classificação da Tese
- **Agente**: `agente_analise_teses`
- **Pattern**: `tese_classification`
- **Entrada**: Teses jurídicas do tópico
- **Saída**: Classificação por tipo e aplicabilidade

#### 3. FIRAC+
- **Agente**: `agente_firac`
- **Pattern**: `make_firac+`
- **Entrada**: Decisões relevantes para o tópico
- **Saída**: Análise estruturada (Facts, Issues, Rules, Application, Conclusion)

#### 4. Seleção de Trechos Representativos
- **Agente**: `agente_selecao_trechos`
- **Pattern**: `extract_key_notes`
- **Entrada**: Decisões e textos relevantes
- **Saída**: Excertos com justificativa de representatividade

#### 5. Parágrafos de Ligação
- **Agente**: `agente_paragrafos_ligacao`
- **Pattern**: `generate_summary`
- **Entrada**: Teses e argumentos adjacentes
- **Saída**: Transições argumentativas

#### 6. Conferência da Citação (ABNT)
- **Agente**: `agente_formatacao_abnt`
- **Pattern**: `extract_bibtex`
- **Entrada**: Referências bibliográficas
- **Saída**: Citações formatadas ABNT

## Tipos de Equipes Comuns

### Equipe de Análise de Precedentes
- **Objetivo**: Analisar um precedente em profundidade
- **Tarefas**:
  - Extração FIRAC+
  - Classificação da tese
  - Validação da existência
  - Geração de BibTeX
  - Identificação de distinções possíveis

### Equipe de Elaboração de Tese
- **Objetivo**: Desenvolver uma tese jurídica completa
- **Tarefas**:
  - Análise de jurisprudência
  - Revisão doutrinária
  - Avaliação de aplicabilidade
  - Formulação de argumentos
  - Verificação de atualidade

### Equipe de Revisão de Petição
- **Objetivo**: Revisar uma petição em preparação
- **Tarefas**:
  - Verificação de prequestionamento
  - Análise de fundamentos
  - Confirmação de citações
  - Revisão de estilo
  - Checagem de conformidade

## Implementação Técnica

### Representação de Equipe
Uma equipe pode ser representada como um arquivo YAML ou JSON contendo:

```yaml
nome: "Equipe de Análise de Precedentes"
descricao: "Analisa um precedente em profundidade"
contexto_compartilhado:
  tipo: "precedente"
  entrada: "decisao_juridica_bruta"
tarefas:
  - nome: "extracao_firac"
    agente: "agente_firac"
    pattern: "make_firac+"
    entrada: "decisao_juridica_bruta"
    saida_formato: "markdown_com_yaml"
  - nome: "classificacao_tese"
    agente: "agente_analise_teses"
    pattern: "tese_classification"
    entrada: "teses_extraidas"
    saida_formato: "json"
  - nome: "validacao_existencia"
    agente: "agente_auditoria"
    pattern: "fact-check"
    entrada: "referencias_juridicas"
    saida_formato: "json"
consolidacao:
  estrategia: "combinacao_estruturada"
  saida_final: "precedente_analisado_completo"
```

## Benefícios da Abstração de Equipes

1. **Paralelismo real**: Tarefas independentes executadas simultaneamente
2. **Contexto controlado**: Cada agente recebe apenas o necessário
3. **Rastreabilidade total**: Caminho completo de cada tarefa
4. **Facilidade de escalabilidade**: Mais equipes, mesmos contratos
5. **Revisão humana facilitada**: Resultados organizados por tarefa

## Integração com Orquestrador

O orquestrador Fabric-aware pode:
- Criar equipes dinamicamente com base na fase do fluxo
- Distribuir tarefas entre agentes da equipe
- Aguardar conclusão de todas as tarefas
- Consolidar resultados segundo regras definidas
- Passar resultados para a próxima fase do fluxo

## Exemplo de Workflow com Equipes

1. **Orquestrador** identifica tópico do TOC para análise
2. **Orquestrador** cria equipe "Análise de Tese" com contexto do tópico
3. **Equipe** executa tarefas em paralelo:
   - Agente A: FIRAC+ da tese
   - Agente B: Classificação da tese
   - Agente C: Validação de jurisprudência
   - Agente D: Geração de BibTeX
4. **Consolidador** junta resultados em formato estruturado
5. **Orquestrador** recebe resultado consolidado para próxima fase

## Limitações e Considerações

- Equipes devem ter duração limitada (temporárias)
- Contexto compartilhado deve ser mínimo e bem definido
- Tarefas devem ser verdadeiramente independentes
- Consolidação deve ser definida antes da execução
- Monitoramento de progresso individual é importante