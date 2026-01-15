# Servidores MCP (Model Context Protocol)

## Visão Geral

Este documento descreve os servidores MCP disponíveis no projeto zotero-mcp e como eles podem ser utilizados pelos diferentes agentes e equipes no fluxo de trabalho jurídico automatizado.

## Servidores Disponíveis

### 1. obsidian-vault

**Propósito**: Acesso ao vault do Obsidian com informações dos processos e pesquisas jurídicas.

**Localização**: `/media/peixoto/Portable/inv_sa_02`

**Recursos Disponíveis**:
- Leitura e escrita de notas Markdown
- Listagem de diretórios e arquivos
- Busca de conteúdo em notas
- Criação e edição de arquivos

**Uso Recomendado**:
- Armazenamento de informações dos processos
- Persistência de TOCs (tabelas de conteúdo) geradas
- Salvamento de peças processuais
- Armazenamento de anotações e pesquisas jurídicas

**Agentes que utilizam**:
- `strategic-organization-agent`: para salvar TOCs e mapas argumentativos
- `juridical-longform-writer`: para salvar peças prontas
- `process-classification-agent`: para armazenar classificações de processos

### 2. obsidian-costum-patterns

**Propósito**: Acesso ao diretório de patterns do Fabric para análise jurídica e processamento de documentos.

**Localização**: `/home/peixoto/.config/fabric/patterns`

**Recursos Disponíveis**:
- Centenas de patterns jurídicos e de análise legal
- Acesso a patterns de jurisprudência, análise de precedentes, fichamento, etc.
- Leitura e escrita de arquivos de patterns

**Uso Recomendado**:
- Análise de documentos jurídicos
- Aplicação de padrões de análise FIRAC+
- Extração de informações de decisões judiciais
- Geração de resumos e fichamentos

**Agentes que utilizam**:
- `pdf-processor-legal`: para processar documentos jurídicos
- `jurisprudence-researcher`: para análise de precedentes
- `teses-analyst`: para classificação de teses jurídicas

### 3. zotero-mcp

**Propósito**: Integração com a biblioteca Zotero para gerenciamento de referências jurídicas.

**Status**: Instalado e configurado (funcionando)

**Recursos Disponíveis**:
- Busca de itens na biblioteca Zotero (`zotero_search_items`)
- Obtenção de metadados detalhados (`zotero_item_metadata`)
- Recuperação de conteúdo de texto completo (`zotero_item_fulltext`)
- Sincronização de anotações

**Uso Recomendado**:
- Verificação de precedentes jurídicos
- Acesso a bibliografia jurídica
- Consulta a documentos e artigos acadêmicos
- Validação de referências bibliográficas

**Agentes que utilizam**:
- `jurisprudencia-auditor`: para verificar existência e atualidade de precedentes
- `jurisprudence-researcher`: para pesquisa em bibliografia jurídica
- `pdf-processor-legal`: para obter metadados de documentos

**Configuração**:
- API local do Zotero habilitada
- Banco de dados indexado com 440 itens
- Funcionando via `/home/peixoto/.mcp/zotero/venv/bin/zotero-mcp`

## Integração com o Orquestrador

O orquestrador MCP pode direcionar tarefas para os diferentes servidores MCP com base nas necessidades do fluxo jurídico:

1. **Fase de Organização Estratégica**: O `strategic-organization-agent` pode usar o `obsidian-vault` para salvar TOCs gerados
2. **Fase de Análise de Precedentes**: O `jurisprudence-researcher` pode usar o `obsidian-costum-patterns` para aplicar patterns de análise
3. **Fase de Auditoria**: O `jurisprudencia-auditor` poderá usar o `zotero-mcp` para verificar precedentes (quando instalado)

## Boas Práticas de Uso

1. **Segurança**: Sempre validar os caminhos e permissões antes de acessar os servidores MCP
2. **Rastreabilidade**: Manter registro de todas as interações com os servidores MCP
3. **Consistência**: Usar os mesmos formatos e convenções ao salvar dados nos servidores
4. **Documentação**: Atualizar este documento quando novos servidores MCP forem adicionados

## Configuração do Servidor Zotero (Instruções Futuras)

Quando for hora de instalar o servidor Zotero MCP, siga estas etapas:

1. Verificar se o Python e o uv estão instalados
2. Instalar o zotero-mcp: `uv pip install zotero-mcp`
3. Configurar as variáveis de ambiente:
   - `ZOTERO_LOCAL=true` (para API local) ou
   - `ZOTERO_API_KEY` e `ZOTERO_LIBRARY_ID` (para API web)
4. Testar o servidor: `uv run zotero-mcp --help`
5. Adicionar a configuração ao arquivo de configuração do cliente MCP