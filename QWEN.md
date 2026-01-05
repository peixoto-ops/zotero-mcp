# Contexto do Projeto zotero-mcp

## Visão Geral do Projeto
zotero-mcp é um servidor Python que implementa o Model Context Protocol (MCP) para o Zotero, fornecendo acesso à sua biblioteca Zotero dentro de assistentes de IA. O projeto permite que ferramentas de IA como o Claude Desktop interajam com sua biblioteca Zotero, permitindo fluxos de trabalho de pesquisa aprimorados ao conectar seu sistema de gerenciamento de referências com capacidades de IA.

## Propósito
O projeto zotero-mcp fornece uma ponte entre assistentes de IA e sua biblioteca Zotero, permitindo que ferramentas de IA:
- Pesquisem sua biblioteca Zotero
- Acessem metadados detalhados sobre suas referências
- Recuperem conteúdo de texto completo de seus PDFs

## Recursos Principais
- **zotero_search_items**: Pesquisa itens na sua biblioteca Zotero usando consultas de texto
- **zotero_item_metadata**: Obtém informações detalhadas de metadados sobre itens específicos do Zotero
- **zotero_item_fulltext**: Obtém conteúdo de texto completo de itens específicos do Zotero (conteúdo do PDF)

## Instalação e Configuração

### Pré-requisitos
- Ambiente Python
- Aplicativo Zotero Desktop (para acesso à API local) OU credenciais da API Web do Zotero

### Opções de Configuração da API Zotero

#### Opção 1: API Local (Recomendado para uso local)
1. Abra o Zotero e vá para "Configurações do Zotero"
2. Na aba "Avançado", marque a caixa que diz "Permitir que outros aplicativos neste computador se comuniquem com o Zotero"

#### Opção 2: API Web
1. Crie uma chave de API nas configurações da sua conta Zotero: https://www.zotero.org/settings/keys
2. Anote seu ID de Biblioteca (geralmente seu ID de Usuário)

### Variáveis de Ambiente
- `ZOTERO_LOCAL=true`: Usa a API local do Zotero (padrão: false)
- `ZOTERO_API_KEY`: Sua chave de API do Zotero (não é necessária para a API local)
- `ZOTERO_LIBRARY_ID`: Seu ID de biblioteca do Zotero (seu ID de usuário para bibliotecas de usuário, não é necessário para a API local)
- `ZOTERO_LIBRARY_TYPE`: Tipo de biblioteca (usuário ou grupo, padrão: usuário)

### Integração com Claude Desktop
Para usar com Claude Desktop e uvx, adicione o seguinte à sua configuração mcpServers:

```json
{
  "mcpServers": {
    "zotero": {
      "command": "uvx",
      "args": ["--upgrade", "zotero-mcp"],
      "env": {
        "ZOTERO_LOCAL": "true",
        "ZOTERO_API_KEY": "",
        "ZOTERO_LIBRARY_ID": ""
      }
    }
  }
}
```

### Uso com Docker
Para implantação com Docker usando a API Web do Zotero:

```json
{
  "mcpServers": {
    "zotero": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "-e", "ZOTERO_API_KEY=SUA_CHAVE_API",
        "-e", "ZOTERO_LIBRARY_ID=SEU_ID_BIBLIOTECA",
        "ghcr.io/kujenga/zotero-mcp:main"
      ],
    }
  }
}
```

## Configuração de Desenvolvimento
1. Clone este repositório
2. Instale as dependências com uv: `uv sync`
3. Crie um arquivo .env na raiz do projeto com as variáveis de ambiente mencionadas acima

## Testes
Para executar a suíte de testes:
```
uv run pytest
```

## Ferramentas de Desenvolvimento
Para desenvolvimento e testes locais, você pode usar o MCP Inspector:
```
npx @modelcontextprotocol/inspector uv run zotero-mcp
```

## Contexto do Projeto para Qwen Code
Este diretório é especificamente para configurar e usar o zotero-mcp com o Qwen Code. O objetivo é integrar a funcionalidade do Zotero com o Qwen Code para permitir fluxos de trabalho de pesquisa que aproveitem tanto o gerenciamento de referências quanto as capacidades de IA.

## Integração com MCP e Subagentes do Qwen Code
Será necessário adaptar a instalação às instruções contidas nas seguintes documentações:

- Documentação para MCP do Qwen Code: https://qwenlm.github.io/qwen-code-docs/en/users/features/mcp/
- Documentação para subagentes: https://qwenlm.github.io/qwen-code-docs/en/users/features/sub-agents/

A ideia é verificar se é possível atribuir as ações aos subagentes que estivessem organizadas em MCPs. Assim poderíamos ter um subagente orquestrador que tivesse conhecimentos das subrotinas do fluxo, identificasse o ponto específico e delegasse as funções para os subagentes pré-configurados, apenas os organizando diante do contexto específico.

As saídas dos subagentes poderiam também ser organizadas para aproveitarmos o potencial de usar cada uma delas em outros processos paralelamente.

## Licença
Licença MIT