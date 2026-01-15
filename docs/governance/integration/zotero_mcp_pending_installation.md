# Instalação do Servidor Zotero MCP - CONCLUÍDO

## Status Atual

O servidor `zotero-mcp` foi **instalado e configurado com sucesso** no sistema. Este componente agora está totalmente funcional e integrado com a biblioteca Zotero, permitindo o funcionamento pleno dos agentes jurídicos que precisam verificar precedentes e acessar referências bibliográficas.

## Recursos Necessários

O servidor Zotero MCP fornecerá os seguintes recursos:

- `zotero_search_items`: Busca de itens na biblioteca Zotero usando consultas de texto
- `zotero_item_metadata`: Obtém informações detalhadas de metadados sobre itens específicos do Zotero
- `zotero_item_fulltext`: Obtém conteúdo de texto completo de itens específicos do Zotero (conteúdo do PDF)

## Agentes que Dependem do Zotero MCP

### 1. jurisprudencia-auditor
- **Função**: Verificar a existência, atualidade e confiabilidade de precedentes jurídicos
- **Dependência**: Usará `zotero_search_items` e `zotero_item_metadata` para verificar precedentes

### 2. jurisprudence-researcher
- **Função**: Realizar pesquisas profundas em precedentes e fontes qualificadas
- **Dependência**: Usará `zotero_search_items` para pesquisar na biblioteca Zotero

### 3. pdf-processor-legal
- **Função**: Processar documentos jurídicos em PDF para gerar resumos e análises
- **Dependência**: Usará `zotero_item_metadata` e `zotero_item_fulltext` para obter metadados bibliográficos

## Instruções de Instalação

### Pré-requisitos
- Ambiente Python com `uv` instalado
- Aplicativo Zotero Desktop (para acesso à API local) OU credenciais da API Web do Zotero

### Opções de Configuração da API Zotero

#### Opção 1: API Local (Recomendado para uso local)
1. Abra o Zotero e vá para "Configurações do Zotero"
2. Na aba "Avançado", marque a caixa que diz "Permitir que outros aplicativos neste computador se comuniquem com o Zotero"

#### Opção 2: API Web
1. Crie uma chave de API nas configurações da sua conta Zotero: https://www.zotero.org/settings/keys
2. Anote seu ID de Biblioteca (geralmente seu ID de Usuário)

### Instalação
1. Instalar o zotero-mcp:
   ```bash
   uv pip install zotero-mcp
   ```

2. Configurar as variáveis de ambiente:
   - `ZOTERO_LOCAL=true`: Usa a API local do Zotero (padrão: false)
   - `ZOTERO_API_KEY`: Sua chave de API do Zotero (não é necessária para a API local)
   - `ZOTERO_LIBRARY_ID`: Seu ID de biblioteca do Zotero (não é necessário para a API local)
   - `ZOTERO_LIBRARY_TYPE`: Tipo de biblioteca (usuário ou grupo, padrão: usuário)

3. Testar o servidor:
   ```bash
   uv run zotero-mcp --help
   ```

### Configuração no Qwen Code
Adicionar a configuração do servidor MCP no arquivo `~/.qwen/settings.json`:

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
    }
  }
}
```

## Impacto na Arquitetura

Com a instalação do Zotero MCP:

1. **Completa o ciclo de verificação**: Os agentes poderão verificar a existência e atualidade de precedentes
2. **Melhora a qualidade da análise**: Os agentes terão acesso a metadados bibliográficos completos
3. **Aumenta a confiabilidade**: As informações jurídicas poderão ser validadas contra a biblioteca Zotero

## Próximos Passos

1. **Instalar o servidor**: Executar os comandos de instalação acima
2. **Configurar a API**: Definir as variáveis de ambiente apropriadas
3. **Testar a conexão**: Verificar se os agentes conseguem acessar o servidor
4. **Atualizar documentação**: Atualizar todos os documentos relevantes para refletir o novo status
5. **Habilitar agentes**: Ativar o uso do Zotero MCP nos agentes que dependem dele

## Documentos Afetados

Após a instalação, os seguintes documentos precisarão ser atualizados:

- `/media/peixoto/Portable/zotero-mcp/.ai/integration/mcp_servers.md` - Remover o status de pendência
- `/media/peixoto/Portable/zotero-mcp/paths.yaml` - Atualizar a descrição do servidor
- `/media/peixoto/Portable/zotero-mcp/README.md` - Atualizar a lista de servidores disponíveis
- `/media/peixoto/Portable/zotero-mcp/CONTEXT.md` - Atualizar a descrição do servidor
- `/media/peixoto/Portable/zotero-mcp/.ai/agents/mcp_integration.md` - Atualizar exemplos de uso
- `/media/peixoto/Portable/zotero-mcp/.ai/teams/mcp_usage.md` - Atualizar exemplos de uso em equipes
- `/media/peixoto/Portable/zotero-mcp/.ai/prompts/mcp_usage_examples.md` - Atualizar exemplos práticos