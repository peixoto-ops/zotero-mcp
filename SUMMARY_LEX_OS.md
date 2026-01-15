# Sumário do Projeto - Lex-OS

## Visão Geral

O projeto Lex-OS (Legal Operating System) implementa um Sistema Operacional Jurídico baseado no Model Context Protocol (MCP). O sistema atua como middleware inteligente entre o Zotero, Obsidian e a engine de IA local (Fabric), permitindo a automação completa de workflows jurídicos com alta eficiência e rastreabilidade.

## Componentes Principais

### 1. Servidor MCP Lex-OS (`src/lex_os_server.py`)

Implementa três módulos principais:

#### Módulo de Memória (Obsidian First)
- `check_local_memory`: Verifica a memória local (Obsidian) antes de buscar externamente
- Implementa lógica "Memory First" para evitar buscas redundantes
- Usa fuzzy matching para encontrar notas relevantes no vault do Obsidian

#### Módulo de Execução (Fabric Wrapper)
- `run_fabric_pipeline`: Executa pipelines do Fabric para processamento de texto jurídico
- Tipos de pipeline suportados:
  - `analise_precedente`: Análise FIRAC+ e extração de notas
  - `fichamento_simples`: Sumarização e fichamento de processos
  - `verificacao_tese`: Verificação de fatos e acordo

#### Módulo de Orquestração Zotero
- `process_zotero_collection`: Processa coleções específicas do Zotero
- Restringe operações por coleção (não permite leitura da biblioteca inteira)
- Aplica pipelines do Fabric e salva resultados diretamente no Obsidian
- Implementa persistência desacoplada da conversação com o LLM

### 2. Sistema de Validação (`src/validation_system.py`)

Implementa mecanismos de validação para referência cruzada:

- Validação da integridade do link entre itens do Zotero e notas do Obsidian
- Verificação da aplicação correta dos padrões Fabric nas notas
- Sistema de auditoria para garantir consistência entre os sistemas
- Geração de relatórios de validação em Markdown

### 3. Sistema de Equipes Paralelas (`src/parallel_teams_system.py`)

Dimensiona o sistema para lidar com múltiplos casos jurídicos concorrentes:

- Criação de equipes especializadas para diferentes funções jurídicas
- Processamento paralelo de múltiplos casos
- Atribuição de tarefas com diferentes prioridades
- Monitoramento de status e progresso das equipes
- Validação cruzada dos resultados

### 4. Agentes Especializados

#### 4.1. Agente de Precedentes
- **FIRAC+**: Estruturação lógica de decisões judiciais
- **NER Jurídico**: Identificação de entidades específicas em textos jurídicos
- **Classificação de precedentes**: Leading case, julgado de consolidação, tese emergente, distinguishing
- **Geração automática de BibTeX**: Criação de entradas bibliográficas
- **Fichamento em Markdown**: Criação de notas estruturadas

#### 4.2. Agente de Contexto
- Consulta à base de conhecimento no Obsidian
- Recuperação de histórico do caso e teses trabalhadas
- Produção de contexto sintético e operacional

#### 4.3. Agente de Estratégia
- Análise de precedentes validados e contexto do caso
- Definição da estratégia jurídica central
- Validação da existência real dos precedentes
- Utilização de ferramentas MCP para verificação em tempo real

#### 4.4. Agente de TOC (Índice de Tópicos)
- Geração de esqueleto argumentativo da peça processual
- Criação de estrutura lógica e hierárquica de argumentos
- Produção de mapa lógico da petição

#### 4.5. Agente de Redação Jurídica
- Desenvolvimento dos tópicos em três dimensões complementares:
  - Direito (lei e doutrina)
  - Jurisprudência
  - Questões de fato e prova
- Integração com resultados dos agentes de precedentes e prova

#### 4.6. Agente de Prova e Cadeia de Custódia
- Extração de fatos de documentos, imagens e vídeos
- Vinculação explícita entre fato, prova e tese jurídica
- Geração de hashes criptográficos e carimbos de tempo
- Utilização de ferramentas MCP para investigação OSINT

#### 4.7. Agente Zotero
- Sincronização bidirecional com a biblioteca Zotero
- Criação automática de itens bibliográficos
- Integração com as ferramentas do zotero-mcp

### 5. Infraestrutura Cognitiva (.ai/)

#### 5.1. Estrutura de Diretórios
- `.ai/`: Infraestrutura cognitiva (README, identity, rules, GOVERNANCE, agentes, fluxos, patterns, schemas, prompts, AGENT_PROMPT)
- `.ai/agents/`: Especificações funcionais de agentes
- `.ai/flows/`: Pipelines documentais completos
- `.ai/patterns/`: Padrões cognitivos reutilizáveis (Fabric)
- `.ai/schemas/`: Esquemas JSON para validação formal de saídas
- `.ai/prompts/`: Prompts especializados (ex: orquestrador MCP)
- `.ai/AGENT_PROMPT.md`: Prompt-base comum a todos os agentes

#### 5.2. Padrões do Fabric
- Cada pattern segue a estrutura: IDENTITY and PURPOSE, STEPS, OUTPUT INSTRUCTIONS, INPUT
- Princípios de atomicidade e statelessness
- Uso de CLI e piping para encadeamento de operações

#### 5.3. Schemas de Validação
- Controle de qualidade e prevenção de alucinações
- Validação estruturada de saídas dos agentes
- Conformidade com padrões jurídicos e técnicos

### 6. Integração com MCPs (Model Context Protocols)

#### 6.1. Servidor Lex-OS MCP
- Conexão com o sistema de orquestração jurídica
- Ferramentas disponíveis: `check_local_memory`, `run_fabric_pipeline`, `process_zotero_collection`
- Sistema de persistência desacoplada

#### 6.2. Obsidian MCP
- Conexão com o vault do Obsidian
- Acesso a conteúdo, criação e edição de notas
- Integração com o plugin Local REST API

#### 6.3. Outras Ferramentas MCP
- Integração com `serper`, `tavily-search`, `brave-search` para investigação
- Uso de ferramentas para validação e verificação de informações

### 7. Orquestração com Subagentes

#### 7.1. Subagente Orquestrador
- Conhecimento das subrotinas do fluxo jurídico
- Capacidade de identificar o ponto específico do fluxo
- Mecanismo de delegação para subagentes pré-configurados

#### 7.2. Arquitetura de Subagentes
- Cada subagente é configurado como arquivo Markdown com YAML frontmatter
- Definição de ferramentas específicas e prompts de sistema
- Configuração de níveis de confiança e permissões

#### 7.3. Processamento Paralelo
- Sistema para organizar as saídas dos subagentes
- Mecanismos para usar saídas em outros processos paralelamente
- Filas de processamento e sincronização

### 8. Pipeline Completo

#### 8.1. Integração dos Componentes
- Conexão de todos os agentes especializados no fluxo jurídico contínuo
- Interfaces de comunicação entre diferentes agentes
- Mecanismos de validação entre etapas do pipeline

#### 8.2. Automação do Fluxo
- Pipeline desde a ingestão de documentos até geração da petição final
- Gatilhos automáticos para ativação de agentes específicos
- Filas de tarefas para processamento contínuo

#### 8.3. Rastreabilidade e Cadeia de Custódia
- Sistema de rastreabilidade em todas as etapas
- Logs detalhados de todas as operações
- Carimbos de tempo criptograficamente seguros

## Estrutura do Projeto

```
zotero-mcp/
├── src/                   # Código-fonte do servidor e sistemas auxiliares
│   ├── lex_os_server.py  # Servidor MCP com os três módulos principais
│   ├── validation_system.py # Sistema de validação de referências cruzadas
│   └── parallel_teams_system.py # Sistema de equipes paralelas
├── .ai/                  # Infraestrutura cognitiva
│   ├── agents/           # Especificações de agentes
│   ├── flows/            # Pipelines de processamento
│   ├── patterns/         # Padrões do Fabric
│   ├── schemas/          # Esquemas de validação
│   └── prompts/          # Prompts de agentes
├── .github/              # Configurações de CI/CD
├── README.md             # Visão geral do projeto
├── README_LEX_OS.md      # Documentação completa do sistema Lex-OS
├── MCP_SERVER_SETUP.md   # Instruções de configuração do servidor MCP
├── CONTEXT_LEX_OS.md     # Contexto completo do sistema Lex-OS
├── QWEN.md               # Documentação técnica detalhada
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

- **README_LEX_OS.md**: Documentação completa do sistema Lex-OS
- **MCP_SERVER_SETUP.md**: Instruções de configuração do servidor MCP
- **CONTEXT_LEX_OS.md**: Contexto completo do sistema Lex-OS
- **QWEN.md**: Detalhes técnicos sobre cada componente e fase do projeto
- **.ai/README.md**: Especificação da infraestrutura cognitiva
- Arquivos de exemplo: Em cada subdiretório de `.ai/`