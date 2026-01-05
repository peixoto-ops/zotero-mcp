# Sumário do Projeto - zotero-mcp

## Visão Geral

O projeto zotero-mcp implementa um sistema completo de orquestração jurídica assistida por múltiplos agentes, integrado ao Zotero, Obsidian e Fabric, com foco em análise profunda de precedentes jurídicos, construção controlada de teses jurídicas, redação modular e verificável de peças processuais e preservação de cadeia de custódia e rastreabilidade probatória.

## Componentes Principais

### 1. Agentes Especializados

#### 1.1. Agente de Precedentes
- **FIRAC+**: Estruturação lógica de decisões judiciais
- **NER Jurídico**: Identificação de entidades específicas em textos jurídicos
- **Classificação de precedentes**: Leading case, julgado de consolidação, tese emergente, distinguishing
- **Geração automática de BibTeX**: Criação de entradas bibliográficas
- **Fichamento em Markdown**: Criação de notas estruturadas

#### 1.2. Agente de Contexto
- Consulta à base de conhecimento no Obsidian
- Recuperação de histórico do caso e teses trabalhadas
- Produção de contexto sintético e operacional

#### 1.3. Agente de Estratégia
- Análise de precedentes validados e contexto do caso
- Definição da estratégia jurídica central
- Validação da existência real dos precedentes
- Utilização de ferramentas MCP para verificação em tempo real

#### 1.4. Agente de TOC (Índice de Tópicos)
- Geração de esqueleto argumentativo da peça processual
- Criação de estrutura lógica e hierárquica de argumentos
- Produção de mapa lógico da petição

#### 1.5. Agente de Redação Jurídica
- Desenvolvimento dos tópicos em três dimensões complementares:
  - Direito (lei e doutrina)
  - Jurisprudência
  - Questões de fato e prova
- Integração com resultados dos agentes de precedentes e prova

#### 1.6. Agente de Prova e Cadeia de Custódia
- Extração de fatos de documentos, imagens e vídeos
- Vinculação explícita entre fato, prova e tese jurídica
- Geração de hashes criptográficos e carimbos de tempo
- Utilização de ferramentas MCP para investigação OSINT

#### 1.7. Agente Zotero
- Sincronização bidirecional com a biblioteca Zotero
- Criação automática de itens bibliográficos
- Integração com as ferramentas do zotero-mcp

### 2. Infraestrutura Cognitiva (.ai/)

#### 2.1. Estrutura de Diretórios
- `.ai/agents/`: Especificações funcionais de agentes
- `.ai/flows/`: Pipelines completos de processamento
- `.ai/patterns/`: Padrões do Fabric para raciocínio jurídico
- `.ai/schemas/`: Esquemas JSON para validação
- `.ai/prompts/`: Prompts de alto nível para agentes

#### 2.2. Padrões do Fabric
- Cada pattern segue a estrutura: IDENTITY and PURPOSE, STEPS, OUTPUT INSTRUCTIONS, INPUT
- Princípios de atomicidade e statelessness
- Uso de CLI e piping para encadeamento de operações

#### 2.3. Schemas de Validação
- Controle de qualidade e prevenção de alucinações
- Validação estruturada de saídas dos agentes
- Conformidade com padrões jurídicos e técnicos

### 3. Integração com MCPs (Model Context Protocols)

#### 3.1. Zotero MCP
- Conexão com a biblioteca Zotero
- Ferramentas disponíveis: `zotero_search_items`, `zotero_item_metadata`, `zotero_item_fulltext`
- Suporte a API local e API Web

#### 3.2. Obsidian MCP
- Conexão com o vault do Obsidian
- Acesso a conteúdo, criação e edição de notas
- Integração com o plugin Local REST API

#### 3.3. Outras Ferramentas MCP
- Integração com `serper`, `tavily-search`, `brave-search` para investigação
- Uso de ferramentas para validação e verificação de informações

### 4. Orquestração com Subagentes

#### 4.1. Subagente Orquestrador
- Conhecimento das subrotinas do fluxo jurídico
- Capacidade de identificar o ponto específico do fluxo
- Mecanismo de delegação para subagentes pré-configurados

#### 4.2. Arquitetura de Subagentes
- Cada subagente é configurado como arquivo Markdown com YAML frontmatter
- Definição de ferramentas específicas e prompts de sistema
- Configuração de níveis de confiança e permissões

#### 4.3. Processamento Paralelo
- Sistema para organizar as saídas dos subagentes
- Mecanismos para usar saídas em outros processos paralelamente
- Filas de processamento e sincronização

### 5. Pipeline Completo

#### 5.1. Integração dos Componentes
- Conexão de todos os agentes especializados no fluxo jurídico contínuo
- Interfaces de comunicação entre diferentes agentes
- Mecanismos de validação entre etapas do pipeline

#### 5.2. Automação do Fluxo
- Pipeline desde a ingestão de documentos até geração da petição final
- Gatilhos automáticos para ativação de agentes específicos
- Filas de tarefas para processamento contínuo

#### 5.3. Rastreabilidade e Cadeia de Custódia
- Sistema de rastreabilidade em todas as etapas
- Logs detalhados de todas as operações
- Carimbos de tempo criptograficamente seguros

## Estrutura do Projeto

```
zotero-mcp/
├── .ai/                    # Infraestrutura cognitiva
│   ├── agents/            # Especificações de agentes
│   ├── flows/             # Pipelines de processamento
│   ├── patterns/          # Padrões do Fabric
│   ├── schemas/           # Esquemas de validação
│   └── prompts/           # Prompts de agentes
├── .github/               # Configurações de CI/CD
├── QWEN.md               # Documentação técnica detalhada
├── README.md             # Visão geral do projeto
├── INSTALL.md            # Instruções de instalação e configuração
├── CONTEXT.md            # Contexto para sessões futuras
├── SUMMARY.md            # Sumário do projeto (este arquivo)
└── paths.yaml            # Configuração de caminhos
```

## Fluxo de Trabalho Típico

1. **Ingestão de Documentos**: Processamento de acórdãos, leis e outros documentos jurídicos
2. **Análise por Agentes**: Cada agente especializado processa sua parte do documento
3. **Validação e Estratégia**: Agente de estratégia define a linha argumentativa
4. **Geração de TOC**: Criação do esqueleto da petição
5. **Redação Jurídica**: Desenvolvimento dos tópicos com base nas três dimensões
6. **Provas e Cadeia de Custódia**: Integração de elementos probatórios
7. **Sincronização com Zotero/Obsidian**: Armazenamento e organização do conhecimento
8. **Geração Final**: Produção da petição com rastreabilidade completa

## Documentação Adicional

- **QWEN.md**: Detalhes técnicos sobre cada componente e fase do projeto
- **.ai/README.md**: Especificação da infraestrutura cognitiva
- **Arquivos de exemplo**: Em cada subdiretório de `.ai/`