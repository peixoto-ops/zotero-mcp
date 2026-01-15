# Configuração do Servidor MCP - Lex-OS Kernel

## Visão Geral

Este documento fornece instruções detalhadas para configurar o servidor MCP do Lex-OS Kernel, que implementa um Sistema Operacional Jurídico baseado no Model Context Protocol (MCP), atuando como middleware inteligente entre o Zotero, Obsidian e a engine de IA local (Fabric).

## Componentes do Servidor

O servidor Lex-OS Kernel implementa três módulos principais:

### 1. Módulo de Memória (Obsidian First)
- `check_local_memory`: Verifica a memória local (Obsidian) antes de buscar externamente
- Implementa lógica "Memory First" para evitar buscas redundantes
- Usa fuzzy matching para encontrar notas relevantes no vault do Obsidian

### 2. Módulo de Execução (Fabric Wrapper Async)
- `run_fabric_pipeline`: Executa pipelines do Fabric para processamento de texto jurídico
- Tipos de pipeline suportados:
  - `analise_precedente`: Executa `make_firac+` e `extract_key_notes`
  - `fichamento`: Executa `summarize` e `fichamento_processo_autos`
  - `tese_check`: Executa `fact-check` e `check_agreement`

### 3. Módulo de Orquestração Zotero
- `process_zotero_collection`: Processa coleções específicas do Zotero
- Requer credenciais da API Web do Zotero
- Aplica pipelines do Fabric e salva resultados diretamente no Obsidian

## Configuração do Servidor

### 1. Configuração do paths.yaml

O arquivo `config/paths.yaml` contém as configurações principais do sistema:

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

### 2. Variáveis de Ambiente

Configure as seguintes variáveis de ambiente:

- `ZOTERO_API_KEY`: Sua chave de API do Zotero
- `ZOTERO_LIBRARY_ID`: Seu ID de biblioteca do Zotero

### 3. Instalação das Dependências

Certifique-se de ter instalado:

```bash
# Instalar uv se ainda não estiver instalado
pip install uv

# Instalar dependências do projeto
uv sync
```

## Configuração no Qwen Code

### 1. Configuração do MCP Server

Adicione a seguinte configuração ao seu arquivo `~/.qwen/settings.json`:

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

### 2. Alternativamente, usando o comando do Qwen Code

Você também pode adicionar o servidor MCP usando o comando CLI do Qwen Code:

```bash
qwen mcp add lex-os --command uv --args "run,lex-os-kernel" --env "ZOTERO_API_KEY=sua_chave_api_aqui,ZOTERO_LIBRARY_ID=seu_id_biblioteca_aqui"
```

## Execução do Servidor

### 1. Execução Manual

Para executar o servidor manualmente:

```bash
# Navegue até o diretório do projeto
cd /path/to/lex-os-kernel

# Execute o servidor
uv run src/lex_os_server.py
```

### 2. Execução com Parâmetros Personalizados

Você pode especificar host e porta personalizados:

```bash
uv run src/lex_os_server.py --host localhost --port 8000
```

## Testando a Configuração

### 1. Verificação de Conectividade

Depois de configurar o servidor, você pode testar sua conectividade:

1. Inicie o servidor MCP
2. No Qwen Code, execute um comando simples para testar as ferramentas:
   - `check_local_memory` com uma consulta de teste
   - `run_fabric_pipeline` com um pequeno texto
   - `process_zotero_collection` com uma coleção existente

### 2. Verificação de Logs

Verifique os logs do servidor para garantir que tudo esteja funcionando corretamente:

- Logs do MCP do Qwen Code: `~/.qwen/logs/`
- Saída do terminal onde o servidor está rodando

## Solução de Problemas

### 1. Problemas Comuns

#### Erro: "Caminho do vault do Obsidian não configurado"
- Verifique se o caminho em `config/paths.yaml` está correto
- Certifique-se de que o diretório do vault existe e tem permissões de leitura

#### Erro: "Ferramenta 'fabric' não encontrada"
- Verifique se o Fabric está instalado: `fabric --version`
- Certifique-se de que o diretório de patterns está configurado corretamente

#### Erro: "Credenciais do Zotero não configuradas"
- Verifique se as variáveis de ambiente estão definidas
- Confirme que a chave de API e o ID da biblioteca estão corretos

#### Erro: "Falha na comunicação MCP"
- Verifique se o servidor está rodando
- Confirme que as configurações no `~/.qwen/settings.json` estão corretas

### 2. Depuração

Para depuração mais detalhada, você pode:

1. Executar o servidor com nível de log mais verboso
2. Verificar os logs do Qwen Code
3. Testar cada ferramenta individualmente

## Segurança

### 1. Gerenciamento de Credenciais

- Nunca compartilhe suas credenciais do Zotero
- Use variáveis de ambiente em vez de hardcoding
- Considere usar um gerenciador de segredos para credenciais sensíveis

### 2. Permissões de Acesso

- O servidor tem acesso ao seu vault do Obsidian - configure permissões adequadamente
- Monitore o acesso às ferramentas MCP
- Revogue credenciais periodicamente

## Integração com Outros Sistemas

### 1. Compatibilidade com Outros MCPs

O Lex-OS Kernel pode ser usado em conjunto com outros servidores MCP, como:

- Obsidian MCP para acesso ao vault
- Outros servidores de análise de dados
- Sistemas de gerenciamento de documentos

### 2. Extensibilidade

O sistema é projetado para ser extensível, permitindo:

- Adição de novas ferramentas MCP
- Integração com outros sistemas de gerenciamento de referências
- Expansão dos pipelines do Fabric

## Boas Práticas

### 1. Monitoramento

- Monitore o desempenho do servidor
- Verifique regularmente os logs
- Teste periodicamente a conectividade

### 2. Atualizações

- Mantenha o servidor atualizado com as últimas versões
- Atualize regularmente as dependências
- Verifique a compatibilidade após atualizações

## Referências

- Documentação MCP do Qwen Code: https://qwenlm.github.io/qwen-code-docs/en/users/features/mcp/
- Documentação de subagentes: https://qwenlm.github.io/qwen-code-docs/en/users/features/sub-agents/
- Repositório oficial do Lex-OS Kernel: https://github.com/peixoto-ops/lex-os-kernel