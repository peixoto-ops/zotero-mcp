# Instalação e Configuração do Lex-OS

## Visão Geral

Este documento fornece instruções detalhadas para instalar e configurar o Sistema Operacional Jurídico (Lex-OS), um servidor MCP baseado no Model Context Protocol (MCP) que atua como middleware inteligente entre o Zotero, Obsidian e a engine de IA local (Fabric).

## Pré-requisitos

### Sistema
- Ubuntu 22.04+ (ou sistema compatível)
- Git
- Python 3.9+
- Node.js 18+ (para MCP do Obsidian)
- uv (gerenciador de pacotes Python)
- Fabric (engine de IA local)

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
sudo apt install -y python3-pip python3-venv nodejs npm poppler-utils

# Instalar uv
pip3 install uv
```

### 3. Configurar o Ambiente Python

```bash
# Navegar ao diretório do projeto
cd zotero-mcp

# Instalar dependências do projeto
uv sync

# Instalar dependências adicionais para o Lex-OS
uv pip install fastmcp pyzotero pyyaml
```

### 4. Configurar o Fabric

O Fabric já deve estar instalado no sistema. Os patterns estão organizados da seguinte forma:

- **Patterns customizados**: `/home/peixoto/peixoto-ops/costum_patterns`
- **Instalação do Fabric**: `/home/peixoto/.config/fabric`

Para usar os patterns customizados, crie links simbólicos:

```bash
# Criar diretório de patterns se não existir
mkdir -p ~/.config/fabric/patterns

# Criar links simbólicos para os patterns jurídicos
ln -sf /home/peixoto/peixoto-ops/costum_patterns/* ~/.config/fabric/patterns/
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

Siga as instruções para configurar o MCP do Obsidian:

1. **Pré-requisitos**:
   - Node.js >= 18.x
   - npm >= 9.x
   - Obsidian instalado localmente com acesso ao filesystem do vault

2. **Verificação**:
   ```bash
   node --version
   npm --version
   ```

3. **Clonar o repositório**:
   ```bash
   git clone https://github.com/bitbonsai/mcp-obsidian.git
   cd mcp-obsidian
   ```

4. **Instalar dependências**:
   ```bash
   npm install
   ```

5. **Build do servidor MCP**:
   ```bash
   npm run build
   ```

6. **Definir o caminho do Vault do Obsidian**:
   Use o caminho absoluto do seu vault do Obsidian.

### 7. Configurar os MCPs no Qwen Code

Crie ou atualize o arquivo `~/.qwen/settings.json` com:

```json
{
  "mcpServers": {
    "lex-os": {
      "command": "python",
      "args": ["/caminho/completo/para/seu/projeto/src/lex_os_server.py"],
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

### 8. Configurar o Arquivo paths.yaml

Atualize o arquivo `paths.yaml` com os caminhos corretos:

```yaml
obsidian_vault_path: "/caminho/do/seu/vault/obsidian"
zotero_library_id: ""  # Deixe vazio se usando modo local
zotero_api_key: ""     # Deixe vazio se usando modo local
zotero_local: true     # Usa a API local do Zotero
custom_patterns_path: "/home/peixoto/peixoto-ops/costum_patterns"
server_host: "localhost"
server_port: 8000
default_threshold: 0.6
max_items_per_collection: 10
```

## Executando o Servidor Lex-OS

### 1. Executar o servidor MCP

```bash
python src/lex_os_server.py --host localhost --port 8000
```

### 2. Testar as funcionalidades

As principais ferramentas disponíveis são:

- `check_local_memory`: Verifica a memória local (Obsidian) antes de buscar externamente
- `run_fabric_pipeline`: Executa pipelines do Fabric para processamento jurídico
- `process_zotero_collection`: Processa coleções específicas do Zotero

## Configuração de Equipes Paralelas

Para processamento de múltiplos casos jurídicos:

1. Importe o sistema de equipes:
```python
from src.parallel_teams_system import initialize_parallel_teams_system
```

2. Crie e configure equipes para diferentes funções:
```python
orchestrator = initialize_parallel_teams_system()

# Crie equipes para diferentes funções jurídicas
research_team = orchestrator.create_team(
    name="Research Team",
    role=TeamRole.PRECEDENTS_RESEARCH,
    members=[/* membros da equipe */]
)
```

## Configuração do Sistema de Validação

Para validação cruzada entre sistemas:

1. Importe o sistema de validação:
```python
from src.validation_system import CrossReferenceValidator
```

2. Execute validações:
```python
validator = CrossReferenceValidator()
results = validator.validate_cross_references_integrity("nome_da_colecao")
```

## Solução de problemas

### Erros comuns

- **"Caminho do vault do Obsidian não configurado"**: Verifique o arquivo `paths.yaml`
- **"Ferramenta 'fabric' não encontrada"**: Verifique se o Fabric está instalado e no PATH
- **"Credenciais do Zotero não configuradas"**: Configure as variáveis de ambiente ou habilite o modo local
- **"Permissão negada ao acessar Zotero"**: Verifique se a opção "Permitir que outros aplicativos se comuniquem com o Zotero" está ativada

### Modo Zotero Local vs API

O servidor suporta dois modos de conexão com o Zotero:

- **Modo Local**: Mais seguro, não requer credenciais, mas exige que o Zotero Desktop esteja rodando com a opção "Permitir que outros aplicativos se comuniquem com o Zotero" habilitada
- **Modo API**: Requer credenciais, mas pode ser usado remotamente

Para habilitar o modo local, defina `zotero_local: true` no `paths.yaml`.

### Verificação de funcionamento

Teste as funções básicas do servidor:

```python
# Testar conexão com o servidor MCP
# Após iniciar o servidor, as ferramentas estarão disponíveis para uso

# Testar verificação de memória local
await check_local_memory("consulta de teste")

# Testar pipeline do Fabric
await run_fabric_pipeline("texto de teste", "analise_precedente")

# Testar processamento de coleção Zotero
await process_zotero_collection("nome_da_colecao", "instrucoes")
```

## Atualização do sistema

Para atualizar para a versão mais recente:

```bash
git pull origin main
uv sync  # Atualizar dependências do projeto
```

## Desinstalação

Para remover o sistema:

1. Remova o diretório do projeto
2. Desative e remova o ambiente virtual
3. Remova as entradas do MCP do seu cliente (Claude Desktop, Qwen Coder, etc.)