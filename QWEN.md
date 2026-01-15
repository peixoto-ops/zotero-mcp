# Contexto do Projeto Lex-OS Kernel

## Visão Geral do Projeto
Lex-OS Kernel é um servidor Python que implementa o Model Context Protocol (MCP) para orquestração jurídica avançada, integrando Zotero, Obsidian e Fabric patterns. O projeto permite que ferramentas de IA como o Claude Desktop interajam com múltiplas fontes de conhecimento jurídico, permitindo fluxos de trabalho de pesquisa e produção jurídica altamente eficientes ao conectar sistemas de gerenciamento de referências, bases de conhecimento pessoal e engines de IA.

## Propósito
O projeto Lex-OS Kernel fornece uma plataforma de orquestração jurídica que integra múltiplas fontes de conhecimento, permitindo que ferramentas de IA:
- Verifiquem a memória local no Obsidian antes de buscar externamente
- Executem pipelines do Fabric para processamento jurídico especializado
- Acessem coleções específicas do Zotero com escopo definido
- Realizem validação cruzada entre sistemas de conhecimento

## Recursos Principais
- **check_local_memory**: Verifica a memória local (Obsidian) antes de buscar externamente
- **run_fabric_pipeline**: Executa pipelines do Fabric para processamento de texto jurídico
- **process_zotero_collection**: Processa coleções específicas do Zotero com pipeline do Fabric

## Instalação e Configuração

### Pré-requisitos
- Ambiente Python 3.10+
- Zotero com API Web configurada OU acesso local
- Obsidian Vault configurado
- Fabric patterns instalados

### Configuração do paths.yaml
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

### Variáveis de Ambiente
- `ZOTERO_API_KEY`: Sua chave de API do Zotero
- `ZOTERO_LIBRARY_ID`: Seu ID de biblioteca do Zotero

### Integração com Claude Desktop
Para usar com Claude Desktop e uv, adicione o seguinte à sua configuração mcpServers:

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
    }
  }
}
```

## Configuração de Desenvolvimento
1. Clone este repositório
2. Instale as dependências com uv: `uv sync`
3. Configure o arquivo `config/paths.yaml` com os caminhos corretos
4. Crie um arquivo .env na raiz do projeto com as variáveis de ambiente

## Testes
Para executar a suíte de testes:
```
uv run pytest
```

## Estrutura do Projeto

- `src/` - Código-fonte do servidor e sistemas auxiliares
  - `lex_os_server.py` - Servidor MCP com os três módulos principais
  - `validation_system.py` - Sistema de validação de referências cruzadas
  - `parallel_teams_system.py` - Sistema de equipes paralelas
- `config/` - Arquivos de configuração do sistema
  - `paths.yaml` - Configuração de caminhos e variáveis do sistema
- `docs/` - Documentação do projeto
  - `governance/` - Infraestrutura cognitiva
  - `legacy/` - Documentação antiga e arquivos migrados
- `pyproject.toml` - Configuração de dependências do projeto

## Arquitetura do Sistema

### 1. Servidor MCP Lex-OS (`src/lex_os_server.py`)
Implementa três módulos principais:

#### Módulo de Memória (Obsidian First)
- `check_local_memory`: Verifica a memória local (Obsidian) antes de buscar externamente
- Implementa lógica "Memory First" para evitar buscas redundantes
- Usa fuzzy matching para encontrar notas relevantes no vault do Obsidian

#### Módulo de Execução (Fabric Wrapper Async)
- `run_fabric_pipeline`: Executa pipelines do Fabric para processamento de texto jurídico
- Tipos de pipeline suportados:
  - `analise_precedente`: Análise FIRAC+ e extração de notas
  - `fichamento`: Sumarização e fichamento de processos
  - `tese_check`: Verificação de fatos e acordo

#### Módulo de Orquestração Zotero
- `process_zotero_collection`: Processa coleções específicas do Zotero
- Requer credenciais da API Web do Zotero
- Aplica pipelines do Fabric e salva resultados diretamente no Obsidian

### 2. Sistema de Validação (`src/validation_system.py`)
- Validação da integridade do link entre itens do Zotero e notas do Obsidian
- Verificação da aplicação correta dos padrões Fabric nas notas
- Sistema de auditoria para garantir consistência entre os sistemas
- Geração de relatórios de validação em Markdown

### 3. Sistema de Equipes Paralelas (`src/parallel_teams_system.py`)
- Criação de equipes especializadas para diferentes funções jurídicas
- Processamento paralelo de múltiplos casos
- Atribuição de tarefas com diferentes prioridades
- Monitoramento de status e progresso das equipes
- Validação cruzada dos resultados

## Infraestrutura Cognitiva

A pasta `docs/governance/` define a **infraestrutura cognitiva do projeto Lex-OS**.

Ela descreve **como os agentes pensam, classificam, extraem e estruturam
informação jurídica**, servindo como contrato formal entre:

- código MCP
- agentes de IA
- fluxos documentais
- integrações com Zotero e Obsidian

Nenhum conteúdo aqui é código executável.
Tudo aqui é **especificação, governança e reprodutibilidade**.

### Estrutura e Componentes

- `docs/governance/README.md` - Documentação geral da infraestrutura cognitiva
- `docs/governance/identity.md` - Identidade e escopo do projeto e do usuário
- `docs/governance/rules.md` - Regras gerais de comportamento do sistema cognitivo
- `docs/governance/GOVERNANCE.md` - Princípios e processos de governança cognitiva
- `docs/governance/agents/` - Especificações funcionais de agentes
- `docs/governance/flows/` - Pipelines documentais completos
- `docs/governance/patterns/` - Padrões cognitivos reutilizáveis (Fabric)
- `docs/governance/schemas/` - Esquemas JSON para validação formal de saídas
- `docs/governance/prompts/` - Prompts especializados (ex: orquestrador MCP)
- `docs/governance/AGENT_PROMPT.md` - Prompt-base comum a todos os agentes

### Princípios Fundamentais

A infraestrutura cognitiva segue estes princípios:

1. **Separação Estrita de Responsabilidades**: A pasta `docs/governance/` contém exclusivamente lógica cognitiva e especificações; o código do MCP contém exclusivamente lógica de execução.

2. **Transparência e Auditabilidade Total**: Toda decisão cognitiva relevante deve estar documentada em `docs/governance/`.

3. **Reprodutibilidade e Determinismo Cognitivo**: Fluxos descritos em `docs/governance/flows/` devem ser completos, ordenados e reproduzíveis.

4. **Saídas Estruturadas e Validáveis**: Nenhum agente pode produzir saída livre sem formato definido; toda saída relevante deve obedecer a um schema JSON ou seguir um formato formal documentado.

5. **Patterns como Unidades Mínimas de Raciocínio**: Patterns representam unidades cognitivas reutilizáveis, com intenção clara, definindo entrada e saída.

### Governança Cognitiva

A governança cognitiva existe para garantir que:
- o raciocínio do sistema seja explícito,
- os agentes sejam auditáveis,
- os fluxos sejam reproduzíveis,
- e nenhuma lógica cognitiva fique implícita no código executável.

## Integração com MCP e Subagentes do Qwen Code
A integração com o Qwen Code permite a utilização do Lex-OS Kernel como um servidor MCP completo, com suporte a subagentes especializados em tarefas jurídicas.

## Fase 1: Módulo de Memória (Obsidian First)
- Verifica a memória local antes de buscar externamente
- Implementa fuzzy matching para encontrar notas relevantes
- Usa a estrutura do Obsidian Vault para recuperação de informações

## Fase 2: Módulo de Execução (Fabric Wrapper Async)
- Executa pipelines do Fabric de forma assíncrona
- Suporta diferentes tipos de análise jurídica
- Integração com patterns customizados do Fabric

## Fase 3: Módulo de Orquestração Zotero
- Processa coleções específicas do Zotero
- Requer credenciais da API Web do Zotero
- Aplica pipelines do Fabric e salva resultados no Obsidian

## Fase 4: Sistema de Validação
- Verifica integridade das referências cruzadas entre sistemas
- Garante consistência entre Zotero, Obsidian e Fabric
- Gera relatórios de validação

## Fase 5: Sistema de Equipes Paralelas
- Processa múltiplos casos jurídicos concorrentemente
- Implementa diferentes especializações de agentes
- Coordenação entre diferentes funções jurídicas

## Componentes Avançados

### Agente de Precedentes
- **FIRAC+** (Facts, Issue, Rule, Analysis, Conclusion + Critical Review): Estruturação lógica de decisões judiciais
- **NER Jurídico** (Named Entity Recognition): Identificação de entidades específicas em textos jurídicos
- **Classificação de precedentes**: Leading case, Julgado de consolidação, Tese emergente, Distinguishing possível
- **Geração automática de BibTeX**: Criação de entradas bibliográficas no padrão BibTeX
- **Fichamento em Markdown**: Criação de notas estruturadas com metadados YAML

### Agente de Contexto
- Consulta à base de conhecimento no Obsidian
- Recuperação de histórico do caso, teses já trabalhadas e decisões anteriores
- Produção de contexto sintético e operacional para uso por outros agentes

### Agente de Estratégia
- Análise de precedentes validados e contexto do caso
- Definição da estratégia jurídica central
- Validação da existência real dos precedentes que sustentam a estratégia
- Utilização de ferramentas MCP para verificar informações em tempo real

### Agente de TOC (Índice de Tópicos)
- Geração de esqueleto argumentativo da peça processual
- Criação de estrutura lógica e hierárquica de argumentos
- Produção de mapa lógico da petição com tópicos interligados

### Agente de Redação Jurídica
- Desenvolvimento dos tópicos em três dimensões complementares: Direito, Jurisprudência e Questões de fato e prova
- Integração com os resultados dos agentes de precedentes e prova
- Geração de conteúdo jurídico estruturado e fundamentado

### Agente de Prova e Cadeia de Custódia
- Extração de fatos de documentos, imagens e vídeos
- Vinculação explícita entre fato, prova e tese jurídica
- Geração de citações ABNT do documento original
- Preservação da cadeia de custódia digital

### Agente Zotero
- Sincronização bidirecional com a biblioteca Zotero
- Criação automática de itens bibliográficos
- Geração de links cruzados entre referências e notas
- Integração com as ferramentas do Lex-OS Kernel

## Referências e Documentação Adicional

Para carregar o contexto completo do projeto em sessões futuras, consulte:

- `README.md` - Visão geral do sistema
- `INSTALL.md` - Instruções detalhadas de instalação e configuração
- `CONTEXT.md` - Contexto completo para sessões futuras
- `SUMMARY.md` - Sumário dos componentes principais
- `config/paths.yaml` - Configuração de caminhos e variáveis do sistema
- `docs/governance/` - Infraestrutura cognitiva (agentes, fluxos, patterns, schemas, prompts)

## Referências e Documentação do Fabric

Para detalhes sobre a estrutura de diretórios e comandos úteis do Fabric, consulte:

- `docs/governance/GOVERNANCE.md` - Princípios de governança cognitiva
- Documentação oficial do Fabric: https://github.com/danielmiessler/Fabric

## Licença
Licença MIT