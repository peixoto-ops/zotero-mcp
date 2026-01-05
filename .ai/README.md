# .ai — Especificação Cognitiva do zotero-mcp

Esta pasta define a **camada de inteligência do projeto zotero-mcp**.

Ela não contém código executável, mas sim **contratos formais de análise,
extração, classificação e geração de conhecimento jurídico** para agentes que
se integram com MCP, Zotero e seus fluxos documentais.

O objetivo é garantir:
- fluxos reproduzíveis (e.g., ingestão de DJe para Zotero)
- agentes auditáveis (com entradas e saídas estruturadas)
- integração clara com o repositório de código existente (MCP server)
- validação automática por schemas
- rastreabilidade de decisões analíticas

---

## Estrutura desta pasta

- `agents/` — especificações funcionais de agentes
- `flows/` — pipelines completos de processamento
- `patterns/` — unidades de raciocínio reutilizáveis (padrões)
- `schemas/` — esquemas JSON para validação estrita
- `prompts/` — prompts de alto nível para agentes/orquestradores

---

## Depêndencias conceituais

Este projeto funciona em conjunto com a implementação MCP do Zotero,
como as variantes disponíveis em Python e JavaScript.

Para referência de padrões cognitivos, usamos o repositório oficial:

https://github.com/danielmiessler/Fabric