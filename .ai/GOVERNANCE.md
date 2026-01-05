# Governança Cognitiva — zotero-mcp

## Objetivo

Este documento estabelece os princípios, regras e processos de governança
da **infraestrutura cognitiva** do projeto `zotero-mcp`, contida na pasta `.ai/`.

A governança cognitiva existe para garantir que:
- o raciocínio do sistema seja explícito,
- os agentes sejam auditáveis,
- os fluxos sejam reproduzíveis,
- e nenhuma lógica cognitiva fique implícita no código executável.

---

## Princípios Fundamentais

### 1. Separação Estrita de Responsabilidades

- A pasta `.ai/` contém **exclusivamente lógica cognitiva e especificações**.
- O código do MCP contém **exclusivamente lógica de execução**.
- Especificações cognitivas **não são implementações**, mas **contratos formais**.
- O código **deve obedecer** às especificações cognitivas, nunca o inverso.

---

### 2. Transparência e Auditabilidade Total

- Toda decisão cognitiva relevante deve estar documentada em `.ai/`.
- É expressamente proibido:
  - esconder raciocínio em código,
  - depender de prompts implícitos,
  - introduzir heurísticas não documentadas.
- Qualquer pessoa deve conseguir entender:
  - *o que* o sistema faz,
  - *por que* faz,
  - *em que ordem* faz,
  apenas lendo `.ai/`.

---

### 3. Reprodutibilidade e Determinismo Cognitivo

- Fluxos descritos em `.ai/flows/` devem ser:
  - completos,
  - ordenados,
  - reproduzíveis.
- A mesma entrada deve produzir:
  - o mesmo tipo de saída,
  - no mesmo formato,
  - validável pelo mesmo schema.
- Variações devem ser explicitamente documentadas.

---

### 4. Saídas Estruturadas e Validáveis

- Nenhum agente pode produzir saída livre sem formato definido.
- Toda saída relevante deve:
  - obedecer a um schema JSON, **ou**
  - seguir um formato formal documentado.
- Schemas são a **autoridade final** sobre estrutura de saída.

---

### 5. Patterns como Unidades Mínimas de Raciocínio

- Patterns representam unidades cognitivas reutilizáveis.
- Nenhum raciocínio complexo deve existir fora de um pattern documentado.
- Todo pattern deve:
  - ter intenção clara,
  - definir entrada e saída,
  - referenciar o repositório oficial do Fabric:
    https://github.com/danielmiessler/Fabric

---

## Processos de Governança

### Revisão de Especificações Cognitivas

- Toda alteração em `.ai/` **deve** passar por revisão.
- Revisões devem verificar:
  - clareza semântica,
  - consistência entre agents, flows e patterns,
  - aderência aos schemas.
- Alterações não revisadas são consideradas inválidas.

---

### Validação Automática (CI)

- Schemas em `.ai/schemas/` devem ser sempre válidos.
- A pipeline de CI deve falhar se:
  - schemas forem inválidos,
  - patterns não referenciarem o Fabric,
  - agentes ou fluxos estiverem ausentes ou incoerentes.
- CI é parte integrante da governança cognitiva.

---

### Controle de Qualidade Cognitiva

- Agentes devem declarar explicitamente:
  - objetivos,
  - entradas,
  - saídas,
  - limites.
- Fluxos devem descrever:
  - ordem de execução,
  - dependências,
  - saídas finais.
- Patterns devem ser reutilizáveis e não ad hoc.

---

## Responsabilidades

### Desenvolvedores

- Devem seguir rigorosamente as especificações em `.ai/`.
- Devem atualizar `.ai/` sempre que:
  - introduzirem novo comportamento cognitivo,
  - alterarem fluxo,
  - criarem nova forma de saída.
- É proibido duplicar lógica cognitiva no código executável.

---

### Revisores

- Devem revisar `.ai/` com o mesmo rigor que código crítico.
- Devem garantir:
  - coerência global do sistema cognitivo,
  - ausência de contradições,
  - conformidade com este documento.

---

## Não Conformidades

São consideradas violações graves:

- Lógica cognitiva presente apenas no código.
- Saídas não estruturadas ou não validadas.
- Fluxos implícitos ou incompletos.
- Patterns não documentados.
- Prompts operacionais fora da pasta `.ai/`.

Não conformidades devem bloquear merge.

---

## Referências

- Repositório oficial do Fabric (Patterns):  
  https://github.com/danielmiessler/Fabric
- Especificações MCP (Model Context Protocol)
- Documentação do projeto `zotero-mcp`

