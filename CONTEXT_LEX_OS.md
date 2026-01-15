# Contexto do Projeto Lex-OS

## Visão Geral do Projeto
O projeto Lex-OS (Legal Operating System) é um servidor Python que implementa um Sistema Operacional Jurídico baseado no Model Context Protocol (MCP). O sistema atua como middleware inteligente entre o Zotero, Obsidian e a engine de IA local (Fabric), permitindo a automação completa de workflows jurídicos com alta eficiência e rastreabilidade.

## Propósito
O projeto Lex-OS fornece uma plataforma integrada para:
- Análise automatizada de precedentes jurídicos
- Processamento de coleções específicas do Zotero
- Fichamento estruturado de processos e decisões
- Produção assistida de peças jurídicas
- Validação cruzada entre sistemas (Zotero, Obsidian, Fabric)
- Processamento paralelo de múltiplos casos jurídicos

## Arquitetura do Sistema

### 1. Servidor MCP Lex-OS (`src/lex_os_server.py`)
Implementa três módulos principais:

#### Módulo de Memória (Obsidian First)
- `check_local_memory`: Verifica a memória local (Obsidian) antes de buscar externamente
- Implementa lógica "Memory First" para evitar buscas redundantes
- Usa fuzzy matching para encontrar notas relevantes no vault do Obsidian

#### Módulo de Execução (Fabric Wrapper)
- `run_fabric_pipeline`: Executa pipelines do Fabric para processamento de texto jurídico
- Tipos de pipeline suportados:
  - `analise_precedente`: Análise FIRAC+ e extração de notas
  - `fichamento_simples`: Sumarização e fichamento de processos
  - `verificacao_tese`: Verificação de fatos e acordo

#### Módulo de Orquestração Zotero
- `process_zotero_collection`: Processa coleções específicas do Zotero
- Restringe operações por coleção (não permite leitura da biblioteca inteira)
- Aplica pipelines do Fabric e salva resultados diretamente no Obsidian
- Implementa persistência desacoplada da conversação com o LLM

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

## Recursos Principais

### Ferramentas Disponíveis
- **check_local_memory**: Verifica informações localmente antes de buscar externamente
- **run_fabric_pipeline**: Executa pipelines do Fabric para processamento jurídico
- **process_zotero_collection**: Processa coleções específicas do Zotero com pipeline do Fabric

### Padrões de Análise Jurídica
- **FIRAC+ Aprimorado**: Estrutura para análise de precedentes jurídicos
- **Matriz de Comparação de Precedentes**: Comparação sistemática entre decisões
- **Análise de Proporcionalidade**: Avaliação de medidas cautelares
- **Análise de Medidas Cautelares Alternativas**: Checklist para aplicação

### Sistema de Equipes
- **Equipe de Pesquisa de Precedentes**: Especializada em análise jurisprudencial
- **Equipe de Análise de Caso**: Foco na análise dos elementos do caso específico
- **Equipe de Planejamento Estratégico**: Definição da estratégia jurídica
- **Equipe de Redação de Documentos**: Produção de peças jurídicas
- **Equipe de Processamento de Evidências**: Tratamento de provas e cadeia de custódia

## Instalação e Configuração

### Pré-requisitos
- Ambiente Python 3.8+
- Aplicativo Zotero Desktop (para acesso à API local) OU credenciais da API Web do Zotero
- Obsidian Vault configurado
- Fabric patterns instalado

### Configuração do Sistema
1. Configure o caminho do seu vault do Obsidian no arquivo `paths.yaml`
2. Configure as credenciais do Zotero (ou habilite o modo local)
3. Verifique se o caminho para os patterns customizados está correto

### Variáveis de Ambiente
- `ZOTERO_LOCAL=true`: Usa a API local do Zotero (padrão: false)
- `ZOTERO_API_KEY`: Sua chave de API do Zotero (não é necessária para a API local)
- `ZOTERO_LIBRARY_ID`: Seu ID de biblioteca do Zotero (seu ID de usuário para bibliotecas de usuário, não é necessário para a API local)

## Integração com Qwen Code
Para usar com o Qwen Code, adicione o seguinte à sua configuração mcpServers:

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

## Uso do Sistema

### Executar o Servidor
```bash
python src/lex_os_server.py --host localhost --port 8000
```

### Exemplo de Uso das Ferramentas
```python
# Verificar memória local antes de buscar externamente
await check_local_memory("prisão preventiva estelionato", threshold=0.7)

# Executar pipeline do Fabric para análise de precedente
await run_fabric_pipeline(texto_decisao, "analise_precedente")

# Processar coleção específica do Zotero
await process_zotero_collection("HC_Precedents", "Analisar casos de estelionato")
```

## Benefícios do Sistema

1. **Eficiência**: Processamento automatizado de coleções inteiras do Zotero
2. **Persistência**: Resultados salvos diretamente no Obsidian, garantindo integridade
3. **Escalabilidade**: Sistema de equipes paralelas para múltiplos casos
4. **Validação**: Sistema de verificação cruzada entre sistemas
5. **Integração**: Conexão fluida entre Zotero, Obsidian e Fabric
6. **Rastreabilidade**: Cadeia de custódia completa das análises
7. **Redução de Alucinações**: Lógica "Memory First" evita busca desnecessária

## Casos de Uso

### Análise de Precedentes
- Processamento automatizado de coleções de decisões do STJ
- Extração de padrões jurisprudenciais usando FIRAC+
- Comparação sistemática entre decisões semelhantes

### Produção de Peças Jurídicas
- Geração assistida de petições iniciais
- Elaboração de memoriais jurídicos
- Preparação de sustentação oral

### Pesquisa Jurisprudencial
- Busca e análise de decisões relevantes
- Validação de teses jurídicas
- Identificação de tendências jurisprudenciais

## Estrutura .ai/ — Infraestrutura Cognitiva do Projeto

A pasta `.ai/` define a **infraestrutura cognitiva do projeto Lex-OS**.

Ela descreve **como os agentes pensam, classificam, extraem e estruturam
informação jurídica**, servindo como contrato formal entre:

- código MCP
- agentes de IA
- fluxos documentais
- integrações com Zotero e Obsidian

Nenhum conteúdo aqui é código executável.
Tudo aqui é **especificação, governança e reprodutibilidade**.

### Princípios Fundamentais

A infraestrutura cognitiva segue estes princípios:

1. **Separação Estrita de Responsabilidades**: A pasta `.ai/` contém exclusivamente lógica cognitiva e especificações; o código do MCP contém exclusivamente lógica de execução.

2. **Transparência e Auditabilidade Total**: Toda decisão cognitiva relevante deve estar documentada em `.ai/`.

3. **Reprodutibilidade e Determinismo Cognitivo**: Fluxos descritos em `.ai/flows/` devem ser completos, ordenados e reproduzíveis.

4. **Saídas Estruturadas e Validáveis**: Nenhum agente pode produzir saída livre sem formato definido; toda saída relevante deve obedecer a um schema JSON ou seguir um formato formal documentado.

5. **Patterns como Unidades Mínimas de Raciocínio**: Patterns representam unidades cognitivas reutilizáveis, com intenção clara, definindo entrada e saída.

## Referências e Documentação Adicional

Para carregar o contexto completo do projeto em sessões futuras, consulte:

- `README_LEX_OS.md` - Visão geral do sistema Lex-OS
- `MCP_SERVER_SETUP.md` - Instruções de configuração do servidor MCP
- `paths.yaml` - Configuração de caminhos e variáveis do sistema
- `.ai/` - Infraestrutura cognitiva (agentes, fluxos, patterns, schemas, prompts)

## Licença
Licença MIT