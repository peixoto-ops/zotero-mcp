# Lex-OS - Sistema Operacional Jurídico

O Lex-OS (Legal Operating System) é um servidor Python que implementa um Sistema Operacional Jurídico baseado no Model Context Protocol (MCP). O sistema atua como middleware inteligente entre o Zotero, Obsidian e a engine de IA local (Fabric), permitindo a automação completa de workflows jurídicos com alta eficiência e rastreabilidade.

## Recursos

- **Sistema de Memória (Obsidian First)**: Verifica a memória local antes de buscar externamente
- **Sistema de Execução (Fabric Wrapper Async)**: Executa pipelines do Fabric para processamento jurídico
- **Sistema de Orquestração Zotero**: Processa coleções específicas do Zotero com escopo definido
- **Sistema de Validação**: Verifica integridade das referências cruzadas entre sistemas
- **Sistema de Equipes Paralelas**: Processa múltiplos casos jurídicos concorrentemente
- **Padrões de Análise Jurídica**: Implementação de FIRAC+ e matrizes de comparação de precedentes
- **Persistência Desacoplada**: Resultados salvos diretamente no Obsidian, garantindo integridade
- **Redução de Alucinações**: Lógica "Memory First" evita busca desnecessária

## Arquitetura do Sistema

### 1. Servidor MCP Lex-OS (`src/lex_os_server.py`)
Implementa três módulos principais:

#### Módulo de Memória (Obsidian First)
- `check_local_memory`: Verifica a memória local (Obsidian) antes de buscar externamente
- Implementa lógica "Memory First" para evitar buscas redundantes
- Usa fuzzy matching para encontrar notas relevantes no vault do Obsidian

#### Módulo de Execução (Fabric Wrapper Async)
- `run_fabric_pipeline`: Executa pipelines do Fabric para processamento de texto jurídico
- Tipos de pipeline suportados:
  - `analise_precedente`: Análise FIRAC+ e extração de notas
  - `fichamento`: Sumarização e fichamento de processos
  - `tese_check`: Verificação de fatos e acordo

#### Módulo de Orquestração Zotero
- `process_zotero_collection`: Processa coleções específicas do Zotero
- Requer credenciais da API Web do Zotero
- Aplica pipelines do Fabric e salva resultados diretamente no Obsidian
- Implementa persistência desacoplada da conversação com o LLM

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

## Componentes Principais

- **Servidor MCP Lex-OS**: Middleware entre Zotero, Obsidian e Fabric
- **Sistema de Validação**: Verificação cruzada entre sistemas
- **Sistema de Equipes Paralelas**: Processamento concorrente de casos
- **Padrões de Análise Jurídica**: Estruturas FIRAC+, matrizes de comparação
- **Especificação Cognitiva**: Pasta `docs/governance/` com contratos formais de análise
- **Fluxos Automatizados**: Pipelines completos de processamento jurídico

## Estrutura do Projeto

- `src/` - Código-fonte do servidor e sistemas auxiliares
  - `lex_os_server.py` - Servidor MCP com os três módulos principais
  - `validation_system.py` - Sistema de validação de referências cruzadas
  - `parallel_teams_system.py` - Sistema de equipes paralelas
- `config/` - Arquivos de configuração do sistema
  - `paths.yaml` - Configuração de caminhos e variáveis do sistema
- `docs/` - Documentação do projeto
  - `governance/` - Infraestrutura cognitiva (README, identity, rules, GOVERNANCE, agentes, fluxos, patterns, schemas, prompts, AGENT_PROMPT, catalog, orchestrators, teams, consolidation, integration)
  - `legacy/` - Documentação antiga e arquivos migrados
- `pyproject.toml` - Configuração de dependências do projeto
- `.github/` - Configurações de CI/CD e templates de contribuição
- `README.md` - Visão geral do sistema
- `INSTALL.md` - Instruções detalhadas de instalação e configuração
- `CONTEXT.md` - Contexto completo para sessões futuras
- `SUMMARY.md` - Sumário dos componentes principais
- `.qwen/` - Configurações do projeto

## Objetivo

Criar um sistema de engenharia jurídica com:
- separação clara de responsabilidades
- auditabilidade completa
- rastreabilidade de decisões
- redução de risco de erro ou alucinação
- integração fluida entre ferramentas de IA e conhecimento jurídico
- processamento paralelo de múltiplos casos
- validação cruzada entre sistemas

## Configuração

Para detalhes de configuração dos caminhos e variáveis do sistema, consulte o arquivo `config/paths.yaml`.

Para instruções de configuração do servidor MCP, consulte este mesmo arquivo ou `INSTALL.md`.

Para detalhes técnicos, consulte `QWEN.md` e `SUMMARY.md`.