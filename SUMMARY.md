# Sumário do Projeto - Lex-OS Kernel

## Visão Geral

O projeto Lex-OS Kernel implementa um Sistema Operacional Jurídico baseado no Model Context Protocol (MCP), atuando como middleware inteligente entre o Zotero, Obsidian e a engine de IA local (Fabric). O sistema permite a automação completa de workflows jurídicos com alta eficiência e rastreabilidade, com foco em análise profunda de precedentes jurídicos, construção controlada de teses jurídicas, redação modular e verificável de peças processuais e preservação de cadeia de custódia e rastreabilidade probatória.

## Componentes Principais

### 1. Servidor MCP Lex-OS (`src/lex_os_server.py`)

#### 1.1. Módulo de Memória (Obsidian First)
- `check_local_memory`: Verifica a memória local (Obsidian) antes de buscar externamente
- Implementa lógica "Memory First" para evitar buscas redundantes
- Usa fuzzy matching para encontrar notas relevantes no vault do Obsidian

#### 1.2. Módulo de Execução (Fabric Wrapper Async)
- `run_fabric_pipeline`: Executa pipelines do Fabric para processamento de texto jurídico
- Tipos de pipeline suportados:
  - `analise_precedente`: Análise FIRAC+ e extração de notas
  - `fichamento`: Sumarização e fichamento de processos
  - `tese_check`: Verificação de fatos e acordo

#### 1.3. Módulo de Orquestração Zotero
- `process_zotero_collection`: Processa coleções específicas do Zotero
- Requer credenciais da API Web do Zotero
- Aplica pipelines do Fabric e salva resultados diretamente no Obsidian

### 2. Sistema de Validação (`src/validation_system.py`)
- Validação da integridade do link entre itens do Zotero e notas do Obsidian
- Verificação da aplicação correta dos padrões Fabric nas notas
- Sistema de auditoria para garantir consistência entre os sistemas
- Geração de relatórios de validação em Markdown

### 3. Sistema de Equipes Paralelas (`src/parallel_teams_system.py`)
- Criação de equipes especializadas para diferentes funções jurídicas
- Processamento paralelo de múltiplos casos
- Atribuição de tarefas com diferentes prioridades
- Monitoramento de status e progresso das equipes
- Validação cruzada dos resultados

### 4. Infraestrutura Cognitiva (`docs/governance/`)

#### 4.1. Estrutura de Diretórios
- `docs/governance/`: Infraestrutura cognitiva (README, identity, rules, GOVERNANCE, agentes, fluxos, patterns, schemas, prompts, AGENT_PROMPT)
- `docs/governance/agents/`: Especificações funcionais de agentes
- `docs/governance/flows/`: Pipelines documentais completos
- `docs/governance/patterns/`: Padrões cognitivos reutilizáveis (Fabric)
- `docs/governance/schemas/`: Esquemas JSON para validação formal de saídas
- `docs/governance/prompts/`: Prompts especializados (ex: orquestrador MCP)
- `docs/governance/AGENT_PROMPT.md`: Prompt-base comum a todos os agentes

#### 4.2. Padrões do Fabric
- Cada pattern segue a estrutura: IDENTITY and PURPOSE, STEPS, OUTPUT INSTRUCTIONS, INPUT
- Princípios de atomicidade e statelessness
- Uso de CLI e piping para encadeamento de operações

#### 4.3. Schemas de Validação
- Controle de qualidade e prevenção de alucinações
- Validação estruturada de saídas dos agentes
- Conformidade com padrões jurídicos e técnicos

### 5. Agentes Especializados

#### 5.1. Agente de Precedentes
- **FIRAC+**: Estruturação lógica de decisões judiciais
- **NER Jurídico**: Identificação de entidades específicas em textos jurídicos
- **Classificação de precedentes**: Leading case, julgado de consolidação, tese emergente, distinguishing
- **Geração automática de BibTeX**: Criação de entradas bibliográficas
- **Fichamento em Markdown**: Criação de notas estruturadas

#### 5.2. Agente de Contexto
- Consulta à base de conhecimento no Obsidian
- Recuperação de histórico do caso e teses trabalhadas
- Produção de contexto sintético e operacional

#### 5.3. Agente de Estratégia
- Análise de precedentes validados e contexto do caso
- Definição da estratégia jurídica central
- Validação da existência real dos precedentes
- Utilização de ferramentas MCP para verificação em tempo real

#### 5.4. Agente de TOC (Índice de Tópicos)
- Geração de esqueleto argumentativo da peça processual
- Criação de estrutura lógica e hierárquica de argumentos
- Produção de mapa lógico da petição

#### 5.5. Agente de Redação Jurídica
- Desenvolvimento dos tópicos em três dimensões complementares:
  - Direito (lei e doutrina)
  - Jurisprudência
  - Questões de fato e prova
- Integração com resultados dos agentes de precedentes e prova

#### 5.6. Agente de Prova e Cadeia de Custódia
- Extração de fatos de documentos, imagens e vídeos
- Vinculação explícita entre fato, prova e tese jurídica
- Geração de hashes criptográficos e carimbos de tempo
- Utilização de ferramentas MCP para investigação OSINT

#### 5.7. Agente Zotero
- Sincronização bidirecional com a biblioteca Zotero
- Criação automática de itens bibliográficos
- Integração com as ferramentas do Lex-OS Kernel

### 6. Integração com MCPs (Model Context Protocols)

#### 6.1. Lex-OS MCP
- Conexão com o servidor Lex-OS Kernel
- Ferramentas disponíveis: `check_local_memory`, `run_fabric_pipeline`, `process_zotero_collection`
- Suporte a API Web do Zotero

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

## Estrutura do Projeto

```
lex-os-kernel/
├── config/                 # Arquivos de configuração do sistema
│   └── paths.yaml         # Configuração de caminhos e variáveis do sistema
├── src/                   # Código-fonte do servidor e sistemas auxiliares
│   ├── lex_os_server.py   # Servidor MCP com os três módulos principais
│   ├── validation_system.py # Sistema de validação de referências cruzadas
│   └── parallel_teams_system.py # Sistema de equipes paralelas
├── docs/                  # Documentação do projeto
│   ├── governance/        # Infraestrutura cognitiva
│   └── legacy/            # Documentação antiga e arquivos migrados
├── .github/               # Configurações de CI/CD
├── pyproject.toml         # Configuração de dependências do projeto
├── README.md             # Visão geral do projeto
├── README_LEX_OS.md      # Documentação completa do sistema Lex-OS
├── INSTALL.md            # Instruções de instalação e configuração
├── CONTEXT.md            # Contexto para sessões futuras
├── SUMMARY.md            # Sumário do projeto (este arquivo)
└── .qwen/                # Configurações do projeto
```

## Fluxo de Trabalho Típico

1. **Verificação de Memória Local**: O sistema verifica o Obsidian antes de buscar externamente
2. **Processamento com Fabric**: Execução de pipelines do Fabric para análise jurídica
3. **Consulta ao Zotero**: Processamento de coleções específicas do Zotero
4. **Validação Cruzada**: Verificação da integridade entre sistemas
5. **Persistência no Obsidian**: Resultados salvos diretamente no vault
6. **Equipes Paralelas**: Processamento concorrente de múltiplos casos
7. **Geração Final**: Produção de relatórios e peças com rastreabilidade completa

## Documentação Adicional

- **QWEN.md**: Detalhes técnicos sobre cada componente e fase do projeto
- **docs/governance/README.md**: Especificação da infraestrutura cognitiva
- **Arquivos de exemplo**: Em cada subdiretório de `docs/governance/`