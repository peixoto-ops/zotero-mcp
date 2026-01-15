# Contexto do Projeto - Lex-OS Kernel

## Visão Geral do Projeto

O projeto Lex-OS Kernel implementa um Sistema Operacional Jurídico baseado no Model Context Protocol (MCP), atuando como middleware inteligente entre o Zotero, Obsidian e a engine de IA local (Fabric). O sistema permite a automação completa de workflows jurídicos com alta eficiência e rastreabilidade, com foco em análise profunda de precedentes jurídicos, construção controlada de teses jurídicas, redação modular e verificável de peças processuais e preservação de cadeia de custódia e rastreabilidade probatória.

## Componentes Principais

### 1. Servidor MCP Lex-OS (`src/lex_os_server.py`)
- **Módulo de Memória (Obsidian First)**: `check_local_memory` - Verifica a memória local antes de buscar externamente
- **Módulo de Execução (Fabric Wrapper Async)**: `run_fabric_pipeline` - Executa pipelines do Fabric para processamento jurídico
- **Módulo de Orquestração Zotero**: `process_zotero_collection` - Processa coleções específicas do Zotero

### 2. Sistema de Validação (`src/validation_system.py`)
- Validação da integridade do link entre itens do Zotero e notas do Obsidian
- Verificação da aplicação correta dos padrões Fabric nas notas
- Sistema de auditoria para garantir consistência entre os sistemas

### 3. Sistema de Equipes Paralelas (`src/parallel_teams_system.py`)
- Criação de equipes especializadas para diferentes funções jurídicas
- Processamento paralelo de múltiplos casos
- Atribuição de tarefas com diferentes prioridades

### 4. Infraestrutura Cognitiva (`docs/governance/`)
- **Estrutura**: README, identity, rules, GOVERNANCE, agents/, flows/, patterns/, schemas/, prompts/, AGENT_PROMPT
- **Padrões**: Cada pattern segue estrutura IDENTITY, STEPS, OUTPUT INSTRUCTIONS
- **Schemas**: Validação estruturada de saídas dos agentes
- **Governança**: Princípios de separação de responsabilidades e auditabilidade
- **Identidade**: Definição do escopo do projeto e do usuário
- **Regras**: Diretrizes gerais de comportamento do sistema cognitivo

## Localização dos Componentes

### Patterns do Fabric
- **Instalados**: `/home/peixoto/.config/fabric`
- **Customizados**: `/media/peixoto/Portable/costum_patterns`

### Estrutura do Projeto
- **Código-fonte**: `src/` com os três módulos principais
- **Configuração**: `config/` com o arquivo `paths.yaml`
- **Documentação**: `docs/governance/` para infraestrutura cognitiva e `docs/legacy/` para documentação antiga

## Configurações Necessárias

### Arquivo de Configuração (`config/paths.yaml`)
```yaml
# Lex-OS Kernel Configuration

# Caminho absoluto para o seu Vault do Obsidian
obsidian_vault_path: "/media/peixoto/Portable/inv_sa_02"

# Caminho absoluto para os patterns customizados do Fabric
custom_patterns_path: "/media/peixoto/Portable/costum_patterns"

# Configurações do Zotero (Opcional se usar ENV VARS)
zotero:
  api_key_env: "ZOTERO_API_KEY"
  library_id_env: "ZOTERO_LIBRARY_ID"
```

### MCP Servers
Configuração em `~/.qwen/settings.json`:

```json
{
  "mcpServers": {
    "lex-os": {
      "command": "uv",
      "args": ["run", "lex-os-kernel"],
      "env": {
        "ZOTERO_API_KEY": "sua_chave_api_aqui",
        "ZOTERO_LIBRARY_ID": "seu_id_biblioteca_aqui"
      }
    },
    "obsidian": {
      "command": "npx",
      "args": ["-y", "obsidian-mcp", "/path/to/your/vault"]
    }
  }
}
```

### Variáveis de Ambiente para Zotero
- `ZOTERO_API_KEY`: Chave de API do Zotero
- `ZOTERO_LIBRARY_ID`: ID da biblioteca do Zotero

## Fluxo de Trabalho Típico

1. **Verificação de Memória Local**: O sistema verifica o Obsidian antes de buscar externamente
2. **Processamento com Fabric**: Execução de pipelines do Fabric para análise jurídica
3. **Consulta ao Zotero**: Processamento de coleções específicas do Zotero
4. **Validação Cruzada**: Verificação da integridade entre sistemas
5. **Persistência no Obsidian**: Resultados salvos diretamente no vault
6. **Equipes Paralelas**: Processamento concorrente de múltiplos casos
7. **Geração Final**: Produção de relatórios e peças com rastreabilidade completa

## Servidores MCP Disponíveis

### lex-os
- **Propósito**: Orquestrador jurídico com memória (Obsidian), execução (Fabric) e fonte (Zotero)
- **Recursos**: Verificação de memória local, execução de pipelines do Fabric, processamento de coleções Zotero
- **Uso típico**: Análise jurídica integrada, verificação de precedentes, processamento de documentos

### obsidian-vault
- **Propósito**: Acesso ao vault do Obsidian com informações dos processos e pesquisas jurídicas
- **Localização**: `/media/peixoto/Portable/inv_sa_02`
- **Recursos**: Leitura/escrita de notas Markdown, listagem de diretórios, busca de conteúdo
- **Uso típico**: Armazenamento de informações dos processos, persistência de TOCs, salvamento de peças

### obsidian-costum-patterns
- **Propósito**: Acesso ao diretório de patterns do Fabric para análise jurídica
- **Localização**: `/home/peixoto/.config/fabric/patterns`
- **Recursos**: Centenas de patterns jurídicos e de análise legal
- **Uso típico**: Análise de documentos jurídicos, aplicação de padrões FIRAC+, extração de informações

## Comandos Úteis

### Fabric
- Listar patterns: `fabric --list`
- Executar pattern: `echo "texto" | fabric -p nome_do_pattern`
- Atualizar patterns: `fabric --update`

### Lex-OS Kernel (após instalação)
- Executar servidor: `uv run lex-os-kernel`
- Testar conexão: Verificar logs do Qwen Code

### Obsidian-MCP
- Testar conexão: Verificar se os servidores obsidian-vault e obsidian-costum-patterns estão acessíveis
- Comandos disponíveis: list_directory, read_note, write_note, search_notes, etc.

### Git
- Verificar status: `git status`
- Atualizar projeto: `git pull origin main`
- Verificar logs: `git log --oneline -10`

## Solução de Problemas

### Problemas Comuns
1. **Erro de conexão com Zotero**: Verifique se as credenciais estão configuradas corretamente
2. **Erro de permissão no Obsidian**: Verifique se o caminho do vault está correto
3. **Pattern do Fabric não encontrado**: Verifique se os links simbólicos estão configurados

### Logs e Depuração
- Logs do MCP do Qwen Code: `~/.qwen/logs/`
- Logs do Lex-OS: Saída do terminal ao executar o servidor
- Logs do Obsidian: Console do desenvolvedor do Obsidian

## Referências

- Documentação MCP do Qwen Code: https://qwenlm.github.io/qwen-code-docs/en/users/features/mcp/
- Documentação de subagentes: https://qwenlm.github.io/qwen-code-docs/en/users/features/sub-agents/
- Repositório oficial do Fabric: https://github.com/danielmiessler/Fabric
- Repositório do Lex-OS Kernel: https://github.com/peixoto-ops/lex-os-kernel