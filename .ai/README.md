# .ai — Infraestrutura Cognitiva do zotero-mcp

Esta pasta define a **infraestrutura cognitiva** do projeto `zotero-mcp`.

Ela descreve **como os agentes pensam, classificam, extraem e estruturam
informação jurídica**, servindo como contrato formal entre:

- código MCP
- agentes de IA
- fluxos documentais
- integrações com Zotero e Obsidian

Nenhum conteúdo aqui é código executável.
Tudo aqui é **especificação, governança e reprodutibilidade**.

---

## Estrutura

- `AGENT_PROMPT.md` — prompt-base comum a todos os agentes
- `agents/` — especificações funcionais de agentes
- `flows/` — pipelines documentais
- `patterns/` — padrões cognitivos reutilizáveis (Fabric)
- `schemas/` — validação formal de saídas
- `prompts/` — prompts especializados (ex: orquestrador MCP)
- `rules.md` — regras duras de comportamento
- `identity.md` — identidade e escopo do projeto
- `GOVERNANCE.md` — regras de evolução

---

## Referência obrigatória

Patterns documentados seguem o repositório oficial:

https://github.com/danielmiessler/Fabric

