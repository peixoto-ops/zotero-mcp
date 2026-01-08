# Sistema Multiagente Jurídico com MCP e Fabric

## Visão Geral

Este projeto implementa um sistema jurídico automatizado baseado em:

- **Patterns do Fabric** (oficiais + personalizados)
- **Agentes especializados**
- **Equipes paralelas**
- **MCPs como IO/auditoria**
- **Obsidian como memória externa**
- **Planejamento sem sobrecarga de contexto**

O sistema é projetado para operar como um **sistema operacional jurídico cognitivo**, com governança de inteligência existente e não apenas criação de novas funcionalidades.

## Arquitetura do Sistema

### Camadas de Decisão

1. **Nível 0 - Meta-Orquestrador**: Visão global do projeto, acionamento de fluxos
2. **Nível 1 - Orquestrador Fabric-aware**: Escolhe patterns e define parâmetros
3. **Nível 2 - Subagentes Cognitivos**: Executam tarefas específicas
4. **Nível 3 - Equipes de Subagentes**: Agrupamentos temporários para tarefas paralelas

### Fases do Fluxo Jurídico

1. **Ingestão** - Leitura de documentos brutos
2. **Classificação Inicial** - Identificação de área do direito e temas
3. **Formulação de Problemas** - Definição de problemas jurídicos
4. **Pesquisa Profunda** - Coleta de jurisprudência e doutrina
5. **Análise Jurídica Estruturada** - Análise FIRAC+, classificação de teses
6. **Auditoria e Validação** - Confirmação de existência e atualidade
7. **Organização Estratégica** - Criação de TOC e mapa argumentativo
8. **Execução Paralela por Equipes** - Trabalho distribuído
9. **Consolidação** - Integração dos outputs
10. **Redação Longform** - Criação do texto final
11. **Revisão Final** - Controle de qualidade

## Componentes Principais

### 1. Catálogo Fabril
- Localização: `.ai/catalog/pattern_catalog.md`
- Descrição: Metadados dos patterns do Fabric com propósito, uso e fases
- Função: Referência externa para seleção de patterns

### 2. Orquestrador Fabric-aware
- Localização: `.ai/orchestrators/fabric_aware_orchestrator.md`
- Descrição: Componente que escolhe patterns e define parâmetros
- Função: Facilitar o trabalho do orquestrador maior

### 3. Abstração de Equipes
- Localização: `.ai/teams/team_abstraction.md`
- Descrição: Estrutura para agrupamento temporário de agentes
- Função: Permitir execução paralela de tarefas independentes

### 4. Sistema de Consolidação
- Localização: `.ai/consolidation/output_consolidation_system.md`
- Descrição: Componente para integração de outputs fragmentados
- Função: Criar produtos finais coerentes e estruturados

### 5. Plano de Integração
- Localização: `.ai/integration/progressive_integration.md`
- Descrição: Estratégia para integração com sistema existente
- Função: Garantir transição segura e gradual

## Princípios de Design

### 1. Contexto Mínimo
- Nada relevante depende de contexto em memória
- Memória vive fora do prompt (Markdown, YAML, Obsidian)

### 2. Separação de Planejamento e Execução
- Agentes de alto nível planejam
- Agentes de baixo nível executam
- MCPs nunca planejam

### 3. Governança de Patterns
- Patterns tratados como IDs referenciáveis
- Catálogo externo ao runtime
- Seleção por fase e propósito

### 4. Paralelismo Controlado
- Equipes executam tarefas em paralelo
- Contexto mínimo por agente
- Consolidação posterior

## Estrutura de Diretórios

```
.ai/
├── catalog/                 # Catálogo de patterns
│   └── pattern_catalog.md
├── orchestrators/          # Orquestradores
│   └── fabric_aware_orchestrator.md
├── teams/                  # Abstração de equipes
│   └── team_abstraction.md
├── consolidation/          # Sistema de consolidação
│   └── output_consolidation_system.md
├── integration/            # Plano de integração
│   └── progressive_integration.md
├── agents/                 # Agentes especializados (existentes)
├── flows/                  # Pipelines (existentes)
├── patterns/               # Patterns personalizados (existentes)
├── schemas/                # Esquemas de validação (existentes)
└── prompts/                # Prompts especializados (existentes)
```

## Uso do Sistema

### Para Novos Projetos
1. Consulte o catálogo para selecionar patterns apropriados
2. Use o orquestrador Fabric-aware para definir parâmetros
3. Monte equipes para execução paralela quando apropriado
4. Utilize o sistema de consolidação para integrar outputs

### Para Integração com Existentes
1. Siga o plano de integração progressiva
2. Comece com o catálogo como referência externa
3. Introduza o orquestrador em modo assistivo
4. Teste equipes em casos piloto
5. Implemente consolidação com supervisão humana
6. Avance para integração completa com otimização

## Benefícios do Sistema

- **Escalabilidade**: Sistema pode crescer com novos patterns e agentes
- **Manutenibilidade**: Componentes bem definidos e separados
- **Rastreabilidade**: Toda decisão e processo é registrado
- **Eficiência**: Paralelismo e reutilização de componentes
- **Qualidade**: Validação e consolidação estruturadas
- **Flexibilidade**: Adaptação a diferentes tipos de tarefas jurídicas

## Próximos Passos

1. Implementar os componentes descritos nos arquivos correspondentes
2. Integrar com os sistemas existentes seguindo o plano de integração
3. Treinar a equipe no uso dos novos componentes
4. Monitorar desempenho e qualidade dos resultados
5. Iterar e otimizar com base no feedback e métricas