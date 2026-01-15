# Plano de Instalação e Configuração - Lex-OS Kernel

## Visão Geral

Este documento fornece instruções detalhadas para instalar e configurar o Lex-OS Kernel, o sistema de orquestração jurídica com Model Context Protocol (MCP), incluindo integração com Zotero, Obsidian e Fabric.

## Pré-requisitos

### Sistema
- Ubuntu 22.04+ (ou sistema compatível)
- Git
- Python 3.10+
- Node.js 18+ (para MCP do Obsidian)
- uv (gerenciador de pacotes Python)

### Contas e Acessos
- Conta no GitHub
- Conta no Zotero (para API Web, se for usar esse método)

## Etapas de Instalação

### 1. Clonar o Repositório

```bash
git clone git@github.com:peixoto-ops/lex-os-kernel.git
cd lex-os-kernel
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

### 3. Configurar a Nova Estrutura de Diretórios

Após a instalação, familiarize-se com a nova estrutura de arquivos:

- `config/` - Arquivos de configuração do sistema
  - `config/paths.yaml` - Configuração de caminhos e variáveis do sistema
- `src/` - Código-fonte do servidor e sistemas auxiliares
  - `src/lex_os_server.py` - Servidor MCP com os três módulos principais
  - `src/validation_system.py` - Sistema de validação de referências cruzadas
  - `src/parallel_teams_system.py` - Sistema de equipes paralelas
- `docs/` - Documentação do projeto
  - `docs/governance/` - Infraestrutura cognitiva (README, identity, rules, GOVERNANCE, agentes, fluxos, patterns, schemas, prompts, AGENT_PROMPT, catalog, orchestrators, teams, consolidation, integration)
  - `docs/legacy/` - Documentação antiga e arquivos migrados
- `pyproject.toml` - Configuração de dependências do projeto

### 3. Configurar o Ambiente Python

```bash
# Navegar ao diretório do projeto
cd lex-os-kernel

# Instalar dependências do projeto
uv sync
```

### 4. Configurar o Fabric

O Fabric já está instalado no sistema. Os patterns estão organizados da seguinte forma:

- **Patterns customizados**: `/media/peixoto/Portable/costum_patterns`
- **Instalação do Fabric**: `/home/peixoto/.config/fabric`

Para usar os patterns customizados, você pode:

1. **Link simbólico** (recomendado):
```bash
ln -s /media/peixoto/Portable/costum_patterns/* ~/.config/fabric/patterns/
```

2. **Cópia direta**:
```bash
cp -r /media/peixoto/Portable/costum_patterns/* ~/.config/fabric/patterns/
```

### 5. Configurar o Lex-OS Kernel

#### 5.1 Configurar o paths.yaml

Atualize o arquivo `config/paths.yaml` com os caminhos corretos para seu sistema:

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

#### 5.2 Configurar as variáveis de ambiente do Zotero

Crie um arquivo `.env` na raiz do projeto com as credenciais do Zotero:

```env
ZOTERO_API_KEY=sua_chave_api_aqui
ZOTERO_LIBRARY_ID=seu_id_biblioteca_aqui
```

### 6. Configurar o Obsidian MCP (bitbonsai/mcp-obsidian)

#### 6.1 Pré-requisitos
- **Sistema Operacional**: Linux / macOS / Windows (WSL ok)
- **Node.js**: >= 18.x
- **npm**: >= 9.x
- **Obsidian**: instalado localmente com acesso ao filesystem do vault

Verificação:
```bash
node --version
npm --version
```

#### 6.2 Clonar o repositório
```bash
git clone https://github.com/bitbonsai/mcp-obsidian.git
cd mcp-obsidian
```

#### 6.3 Instalar dependências
```bash
npm install
```

#### 6.4 Build do servidor MCP
```bash
npm run build
```

Artefato esperado: `dist/index.js`

Se `dist/index.js` não existir → build falhou.

#### 6.5 Estrutura esperada após build
```
mcp-obsidian/
├── dist/
│   └── index.js        # ENTRYPOINT MCP
├── src/
├── package.json
├── README.md
└── node_modules/
```

#### 6.6 Definir o caminho do Vault do Obsidian
Defina o caminho absoluto do vault.

Exemplo Linux:
````
/home/luiz/ObsidianVault
```

⚠️ O MCP opera diretamente no filesystem, não via API do Obsidian.

#### 6.7 Configuração no cliente MCP (Claude / ChatGPT Desktop / outro)

Arquivo de configuração MCP (exemplo genérico):
```json
{
  "mcpServers": {
    "obsidian": {
      "command": "node",
      "args": [
        "/ABSOLUTE/PATH/mcp-obsidian/dist/index.js",
        "/ABSOLUTE/PATH/DO/VAULT"
      ]
    }
  }
}
```

Exemplo concreto (Linux):
```json
{
  "mcpServers": {
    "obsidian": {
      "command": "node",
      "args": [
        "/home/luiz/tools/mcp-obsidian/dist/index.js",
        "/home/luiz/ObsidianVault"
      ]
    }
  }
}
```

#### 6.8 Ferramentas MCP disponíveis (core)
O servidor expõe ferramentas MCP do tipo:
- `read_note`
- `write_note`
- `append_note`
- `prepend_note`
- `delete_note`
- `move_note`
- `list_directory`
- `search_notes`
- `get_frontmatter`
- `update_frontmatter`

Todas operam sobre arquivos .md dentro do vault.

#### 6.9 Modos de escrita suportados
- overwrite
- append
- prepend

Exemplo lógico (não JSON MCP, apenas semântico):
````
write_note(path="Notas/Teste.md", mode="append", content="texto")
```

#### 6.10 Regras de segurança implementadas
- Restrição ao diretório do vault
- Sanitização de path traversal
- Parsing seguro de frontmatter YAML
- Respostas curtas (LLM-optimized)

#### 6.11 Problemas comuns
- **Erro: node não encontrado**: `sudo apt install nodejs npm`
- **Erro: caminho do vault inválido**: Use caminho absoluto e verifique permissões de leitura/escrita
- **Erro: dist/index.js não existe**: Execute `npm run build`

#### 6.12 Estado do projeto
- Status: ativo
- Compatibilidade: MCP padrão
- Dependência do Obsidian: nenhuma em runtime
- Plugin Obsidian: NÃO obrigatório

#### 6.13 Recomendação para automação (seu caso)
Para integração com Fabric, Zotero e Obsidian como base de conhecimento jurídico, use este MCP como camada de persistência final, controlada por um agente orquestrador, nunca diretamente pelo LLM principal.

### 7. Configurar os Patterns do Fabric

O Fabric já está instalado no sistema. Os patterns estão organizados da seguinte forma:

- **Patterns customizados**: `/media/peixoto/Portable/costum_patterns`
- **Instalação do Fabric**: `/home/peixoto/.config/fabric`

Para usar os patterns customizados, você pode:

1. **Link simbólico** (recomendado):
```bash
ln -s /media/peixoto/Portable/costum_patterns/* ~/.config/fabric/patterns/
```

2. **Cópia direta**:
```bash
cp -r /media/peixoto/Portable/costum_patterns/* ~/.config/fabric/patterns/
```

Os patterns do Fabric seguem a estrutura:
- Cada pattern é uma pasta com nome descritivo
- Dentro de cada pasta, existe um arquivo `system.md` com a definição do pattern
- A estrutura do arquivo `system.md` segue o formato:
  - `# IDENTITY and PURPOSE` - Identidade e propósito do pattern
  - `# STEPS` - Etapas do processo de pensamento
  - `# OUTPUT INSTRUCTIONS` - Instruções de saída
  - `# INPUT` - Indicação do input

### 8. Configurar os MCPs no Qwen Code

Crie ou atualize o arquivo `~/.qwen/settings.json` com:

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

### 9. Configurar os Schemas de Validação

Os schemas JSON para validação estão localizados em `docs/governance/schemas/` e devem ser referenciados pelos agentes conforme necessário.

### 10. Testar a Configuração

```bash
# Testar o lex-os-kernel
uv run lex-os-kernel --help

# Testar o Fabric com um pattern de exemplo
echo "teste" | fabric -p summarize
```

## Configurações Adicionais

### Configuração de Segurança

- Revogue chaves de API antigas regularmente
- Não compartilhe credenciais em repositórios públicos
- Use variáveis de ambiente para informações sensíveis

## Solução de Problemas

### Problemas Comuns

1. **Erro de conexão com Zotero**: Verifique se as credenciais estão configuradas corretamente
2. **Erro de permissão no Obsidian**: Verifique se o caminho do vault está correto e acessível
3. **Pattern do Fabric não encontrado**: Verifique se o diretório de patterns está configurado corretamente

### Logs e Depuração

- Logs do MCP do Qwen Code: `~/.qwen/logs/`
- Logs do Lex-OS: Verifique a saída do terminal ao executar o servidor
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