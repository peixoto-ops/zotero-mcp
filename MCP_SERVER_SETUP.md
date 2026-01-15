# Servidor MCP Lex-OS

O servidor MCP Lex-OS é um Sistema Operacional Jurídico que atua como middleware inteligente entre o Zotero, o Obsidian e a engine de IA local (Fabric).

## Instalação

### Dependências

Antes de executar o servidor, certifique-se de ter instalado:

1. **Python 3.8+**
2. **Fabric**: `pip install fabric`
3. **FastMCP**: `pip install fastmcp`
4. **PyZotero**: `pip install pyzotero`
5. **PyYAML**: `pip install pyyaml`

### Configuração

1. Configure o caminho do seu vault do Obsidian no arquivo `paths.yaml`
2. Configure as credenciais do Zotero (ou habilite o modo local)
3. Verifique se o caminho para os patterns customizados está correto

## Configuração do Qwen Coder

Para configurar o servidor MCP no Qwen Coder, adicione a seguinte configuração ao seu arquivo de configuração do MCP:

```json
{
  "mcpServers": {
    "lex-os": {
      "command": "python",
      "args": ["/caminho/para/seu/projeto/src/lex_os_server.py"],
      "env": {
        "ZOTERO_LOCAL": "true",
        "ZOTERO_API_KEY": "",
        "ZOTERO_LIBRARY_ID": ""
      }
    }
  }
}
```

Alternativamente, se estiver usando uv (como no projeto original), você pode executar:

```bash
uv run python src/lex_os_server.py
```

## Ferramentas Disponíveis

### 1. check_local_memory

Verifica a memória local (Obsidian) antes de buscar externamente.

Parâmetros:
- `query`: Consulta para buscar na memória local
- `threshold`: Limiar de similaridade (padrão: 0.6)

### 2. run_fabric_pipeline

Executa pipelines do Fabric para processamento de texto jurídico.

Parâmetros:
- `text`: Texto para processar
- `pipeline_type`: Tipo de pipeline
  - `analise_precedente`: Executa análise FIRAC+ e extração de notas
  - `fichamento_simples`: Executa sumarização e fichamento de processos
  - `verificacao_tese`: Executa verificação de fatos e acordo

### 3. process_zotero_collection

Processa uma coleção específica do Zotero com pipeline do Fabric.

Parâmetros:
- `collection_name`: Nome da coleção Zotero para processar
- `instruction`: Instrução para o processamento

## Uso

Execute o servidor com:

```bash
python src/lex_os_server.py --host localhost --port 8000
```

O servidor estará disponível em `http://localhost:8000`

## Funcionalidades

### Memory First
O servidor implementa uma lógica "Memory First" que verifica primeiro se a informação já está disponível localmente no Obsidian antes de buscar externamente.

### Processamento em Lote
O servidor processa coleções inteiras do Zotero, aplicando pipelines do Fabric e salvando os resultados diretamente no Obsidian.

### Persistência Desacoplada
Os resultados são salvos diretamente no Obsidian, garantindo persistência mesmo que a conversação com o LLM seja interrompida.

## Arquitetura

O servidor implementa três módulos principais:

1. **Módulo de Memória (Obsidian First)**: Verifica informações localmente antes de buscar externamente
2. **Módulo de Execução (Fabric Wrapper)**: Processa textos usando patterns do Fabric via subprocessos
3. **Módulo de Orquestração Zotero**: Processa coleções específicas do Zotero com escopo definido

## Solução de Problemas

### Erros Comuns

- **"Caminho do vault do Obsidian não configurado"**: Verifique o arquivo `paths.yaml`
- **"Ferramenta 'fabric' não encontrada"**: Verifique se o Fabric está instalado e no PATH
- **"Credenciais do Zotero não configuradas"**: Configure as variáveis de ambiente ou habilite o modo local

### Modo Zotero Local vs API

O servidor suporta dois modos de conexão com o Zotero:

- **Modo Local**: Mais seguro, não requer credenciais, mas exige que o Zotero Desktop esteja rodando com a opção "Permitir que outros aplicativos se comuniquem com o Zotero" habilitada
- **Modo API**: Requer credenciais, mas pode ser usado remotamente

Para habilitar o modo local, defina `zotero_local: true` no `paths.yaml` e configure as variáveis de ambiente:

```
ZOTERO_LOCAL=true
ZOTERO_API_KEY=
ZOTERO_LIBRARY_ID=
```