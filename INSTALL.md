# Plano de Instalação e Configuração - zotero-mcp

## Visão Geral

Este documento fornece instruções detalhadas para instalar e configurar o sistema de orquestração jurídica com Model Context Protocol (MCP), incluindo integração com Zotero, Obsidian e Fabric.

## Pré-requisitos

### Sistema
- Ubuntu 22.04+ (ou sistema compatível)
- Git
- Python 3.9+
- Node.js 18+ (para MCP do Obsidian)
- uv (gerenciador de pacotes Python)

### Contas e Acessos
- Conta no GitHub
- Conta no Zotero (para API Web, se for usar esse método)

## Etapas de Instalação

### 1. Clonar o Repositório

```bash
git clone git@github.com:peixoto-ops/zotero-mcp.git
cd zotero-mcp
```

### 2. Instalar Dependências do Sistema

```bash
# Atualizar pacotes
sudo apt update

# Instalar dependências básicas
sudo apt install -y python3-pip python3-venv nodejs npm

# Instalar uv
pip3 install uv
```

### 3. Configurar a Infraestrutura Cognitiva

Após a instalação, familiarize-se com a estrutura de arquivos:

- `.ai/` - Infraestrutura cognitiva do projeto
  - `.ai/README.md` - Documentação geral da infraestrutura cognitiva
  - `.ai/identity.md` - Identidade e escopo do projeto e do usuário
  - `.ai/rules.md` - Regras gerais de comportamento do sistema cognitivo
  - `.ai/GOVERNANCE.md` - Princípios e processos de governança cognitiva
  - `.ai/agents/` - Especificações funcionais de agentes
  - `.ai/flows/` - Pipelines documentais completos
  - `.ai/patterns/` - Padrões cognitivos reutilizáveis (Fabric)
  - `.ai/schemas/` - Esquemas JSON para validação formal de saídas
  - `.ai/prompts/` - Prompts especializados (ex: orquestrador MCP)
  - `.ai/AGENT_PROMPT.md` - Prompt-base comum a todos os agentes

### 3. Configurar o Ambiente Python

```bash
# Navegar ao diretório do projeto
cd zotero-mcp

# Instalar dependências do zotero-mcp
uv sync
```

### 4. Configurar o Fabric

O Fabric já está instalado no sistema. Os patterns estão organizados da seguinte forma:

- **Patterns customizados**: `/media/peixoto/Portable/custom_patterns`
- **Instalação do Fabric**: `/home/peixoto/.config/fabric`

Para usar os patterns customizados, você pode:

1. **Link simbólico** (recomendado):
```bash
ln -s /media/peixoto/Portable/custom_patterns/* ~/.config/fabric/patterns/
```

2. **Cópia direta**:
```bash
cp -r /media/peixoto/Portable/custom_patterns/* ~/.config/fabric/patterns/
```

### 5. Configurar o Zotero MCP

#### Opção A: API Local (Recomendada)
1. Abra o Zotero
2. Vá para "Editar" > "Preferências" > "Avançado" > "Geral"
3. Marque a opção "Permitir que outros aplicativos neste computador se comuniquem com o Zotero"

#### Opção B: API Web
1. Acesse https://www.zotero.org/settings/keys
2. Crie uma nova chave de API
3. Anote seu ID de usuário e a chave da API

### 6. Configurar o Obsidian MCP

```bash
# Instalar o Obsidian MCP Server
npx @smithery/cli install obsidian-mcp --client qwen

# Ou instalar manualmente
npm install -g obsidian-mcp
```

#### Configuração do Plugin do Obsidian
1. No Obsidian, vá para Configurações > Plugins da Comunidade
2. Clique em "Procurar" e pesquise por "Local REST API" de `coddingtonbear`
3. Clique em "Instalar" e ative o plugin

### 7. Configurar os MCPs no Qwen Code

Crie ou atualize o arquivo `~/.qwen/settings.json` com:

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

### 8. Configurar os Patterns do Fabric

Copie os patterns personalizados para o diretório do Fabric:

```bash
# Criar diretórios para patterns jurídicos
mkdir -p ~/.config/fabric/patterns/juridico
mkdir -p ~/.config/fabric/patterns/meta

# Os patterns específicos devem estar em .ai/patterns/ do projeto
# Copiar os patterns relevantes para ~/.config/fabric/patterns/
```

### 9. Configurar os Schemas de Validação

Os schemas JSON para validação estão localizados em `.ai/schemas/` e devem ser referenciados pelos agentes conforme necessário.

### 10. Testar a Configuração

```bash
# Testar o zotero-mcp
uv run zotero-mcp --help

# Testar o Fabric com um pattern de exemplo
echo "teste" | fabric -p summarize
```

## Configurações Adicionais

### Configuração do Ambiente

Crie um arquivo `.env` na raiz do projeto com as variáveis necessárias:

```env
ZOTERO_LOCAL=true
ZOTERO_API_KEY=sua_chave_api
ZOTERO_LIBRARY_ID=seu_id_biblioteca
ZOTERO_LIBRARY_TYPE=user
```

### Configuração de Segurança

- Revogue chaves de API antigas regularmente
- Não compartilhe credenciais em repositórios públicos
- Use variáveis de ambiente para informações sensíveis

## Solução de Problemas

### Problemas Comuns

1. **Erro de conexão com Zotero**: Verifique se a opção de comunicação com outros aplicativos está ativada
2. **Erro de permissão no Obsidian**: Verifique se o caminho do vault está correto e acessível
3. **Pattern do Fabric não encontrado**: Verifique se o diretório de patterns está configurado corretamente

### Logs e Depuração

- Logs do MCP do Qwen Code: `~/.qwen/logs/`
- Logs do Zotero: Verifique a saída do terminal ao executar o zotero-mcp
- Logs do Obsidian: Verifique o console do desenvolvedor do Obsidian

## Atualização do Sistema

```bash
# Atualizar o repositório
git pull origin main

# Atualizar dependências
uv sync

# Atualizar o Fabric (se instalado via script)
curl -fsSL https://get.fabric.pub | bash

# Atualizar MCPs conforme necessário
```