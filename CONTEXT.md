# Contexto do Projeto - zotero-mcp

## Visão Geral do Projeto

O projeto zotero-mcp implementa um sistema completo de orquestração jurídica assistida por múltiplos agentes, integrado ao Zotero, Obsidian e Fabric, com foco em análise profunda de precedentes jurídicos, construção controlada de teses jurídicas, redação modular e verificável de peças processuais e preservação de cadeia de custódia e rastreabilidade probatória.

## Componentes Principais

### 1. Agentes Especializados
- **Agente de Precedentes**: FIRAC+, NER Jurídico, classificação de precedentes, geração de BibTeX
- **Agente de Contexto**: Consulta à base de conhecimento no Obsidian
- **Agente de Estratégia**: Análise de precedentes e definição de estratégia jurídica
- **Agente de TOC**: Geração de esqueleto argumentativo
- **Agente de Redação Jurídica**: Desenvolvimento em três dimensões (direito, jurisprudência, provas)
- **Agente de Prova e Cadeia de Custódia**: Extração de fatos e preservação de provas
- **Agente Zotero**: Sincronização com biblioteca Zotero

### 2. Infraestrutura Cognitiva (.ai/)
- **Estrutura**: agents/, flows/, patterns/, schemas/, prompts/
- **Padrões**: Cada pattern segue estrutura IDENTITY, STEPS, OUTPUT INSTRUCTIONS
- **Schemas**: Validação estruturada de saídas dos agentes

### 3. Integração com MCPs
- **Zotero MCP**: Conexão com biblioteca Zotero
- **Obsidian MCP**: Conexão com vault do Obsidian
- **Outras ferramentas**: serper, tavily-search, brave-search

### 4. Orquestração com Subagentes
- **Subagente Orquestrador**: Coordenação do fluxo jurídico
- **Arquitetura**: Subagentes com responsabilidades bem definidas
- **Processamento Paralelo**: Organização de saídas para uso em outros processos

## Localização dos Componentes

### Patterns do Fabric
- **Instalados**: `/home/peixoto/.config/fabric`
- **Customizados**: `/media/peixoto/Portable/custom_patterns`

### Estrutura do Projeto
- **Infra cognitiva**: `.ai/` na raiz do projeto
- **Documentação**: `QWEN.md`, `README.md`, `INSTALL.md`, `SUMMARY.md`

## Configurações Necessárias

### MCP Servers
Configuração em `~/.qwen/settings.json`:

```json
{
  "mcpServers": {
    "zotero": {
      "command": "uv",
      "args": ["run", "zotero-mcp"],
      "env": {
        "ZOTERO_LOCAL": "true",
        "ZOTERO_API_KEY": "",
        "ZOTERO_LIBRARY_ID": ""
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
- `ZOTERO_LOCAL`: Usa API local (padrão: false)
- `ZOTERO_API_KEY`: Chave de API do Zotero
- `ZOTERO_LIBRARY_ID`: ID da biblioteca do Zotero
- `ZOTERO_LIBRARY_TYPE`: Tipo de biblioteca (usuário/grupo)

## Fluxo de Trabalho Típico

1. **Ingestão de Documentos**: Processamento de acórdãos e documentos jurídicos
2. **Análise por Agentes**: Cada agente especializado processa sua parte
3. **Validação e Estratégia**: Definição da linha argumentativa
4. **Geração de TOC**: Criação do esqueleto da petição
5. **Redação Jurídica**: Desenvolvimento dos tópicos
6. **Provas e Cadeia de Custódia**: Integração de elementos probatórios
7. **Sincronização com Zotero/Obsidian**: Armazenamento e organização
8. **Geração Final**: Produção da petição com rastreabilidade

## Comandos Úteis

### Fabric
- Listar patterns: `fabric --list`
- Executar pattern: `echo "texto" | fabric -p nome_do_pattern`
- Atualizar patterns: `fabric --update`

### Zotero-MCP
- Executar servidor: `uv run zotero-mcp`
- Testar conexão: Verificar logs do Qwen Code

### Git
- Verificar status: `git status`
- Atualizar projeto: `git pull origin main`
- Verificar logs: `git log --oneline -10`

## Solução de Problemas

### Problemas Comuns
1. **Erro de conexão com Zotero**: Verifique se a opção de comunicação com outros aplicativos está ativada
2. **Erro de permissão no Obsidian**: Verifique se o caminho do vault está correto
3. **Pattern do Fabric não encontrado**: Verifique se os links simbólicos estão configurados

### Logs e Depuração
- Logs do MCP do Qwen Code: `~/.qwen/logs/`
- Logs do Zotero: Saída do terminal ao executar o zotero-mcp
- Logs do Obsidian: Console do desenvolvedor do Obsidian

## Referências

- Documentação MCP do Qwen Code: https://qwenlm.github.io/qwen-code-docs/en/users/features/mcp/
- Documentação de subagentes: https://qwenlm.github.io/qwen-code-docs/en/users/features/sub-agents/
- Repositório oficial do Fabric: https://github.com/danielmiessler/Fabric
- Repositório do zotero-mcp: https://github.com/kujenga/zotero-mcp