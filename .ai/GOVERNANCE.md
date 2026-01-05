# Governança Cognitiva

## Objetivo
Este documento estabelece os princípios e práticas para governança da infraestrutura cognitiva do projeto zotero-mcp, contida na pasta `.ai/`.

## Princípios Fundamentais

### 1. Separação de Responsabilidades
- A lógica de raciocínio (pasta `.ai/`) é separada da lógica de execução (código do MCP)
- As especificações cognitivas são contratos formais, não implementações

### 2. Transparência e Auditabilidade
- Todas as decisões cognitivas devem estar documentadas em `.ai/`
- É proibido esconder lógica de raciocínio no código executável

### 3. Reprodutibilidade
- Os fluxos devem ser reproduzíveis com base nas especificações em `.ai/`
- As saídas devem ser consistentes e previsíveis

## Processos de Governança

### Revisão de Especificações
- Toda alteração em `.ai/` deve passar por revisão de pares
- Padrões de qualidade são verificados automaticamente via CI

### Validação de Schemas
- Todos os schemas JSON em `.ai/schemas/` devem ser válidos
- As saídas dos agentes devem ser validadas contra os schemas apropriados

### Controle de Qualidade
- Padrões de qualidade para patterns, agents e flows devem ser seguidos
- A consistência entre as diferentes partes da infraestrutura cognitiva deve ser mantida

## Responsabilidades

### Desenvolvedores
- Devem seguir os padrões estabelecidos em `.ai/`
- Não devem duplicar lógica cognitiva no código executável

### Revisores
- Devem verificar a conformidade com os princípios de governança
- Devem assegurar a qualidade e consistência das especificações

## Referências
- Padrões do repositório oficial do Fabric: https://github.com/danielmiessler/Fabric
- Diretrizes de documentação do projeto
- Especificações MCP (Model Context Protocol)