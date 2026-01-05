# Agente: zotero_ingest

## Objetivo

Realizar a **ingestão automatizada de documentos jurídicos** na biblioteca Zotero,
com extração de metadados, classificação documental e geração de registros
estruturados, em conformidade com a infraestrutura cognitiva do projeto `zotero-mcp`.

Este agente atua exclusivamente na **ingestão e estruturação**, não na análise
substantiva do conteúdo jurídico.

---

## Entradas Esperadas

- Conteúdo bruto do documento:
  - PDF
  - HTML
  - Texto plano
- Metadados básicos (quando disponíveis):
  - título
  - data
  - fonte/origem
- Indicação do tipo documental (quando conhecida):
  - acórdão
  - decisão
  - petição
  - publicação do DJe
  - artigo
  - outro

> Caso algum dado esteja ausente, o agente deve declarar explicitamente a ausência,
sem inferência não documentada.

---

## Saídas Produzidas

- Entrada **BibTeX estruturada**, adequada a documentos jurídicos
- Classificação do tipo documental, validável por schema
- Anotações estruturadas em Markdown (contexto e metadados)
- Links para fontes oficiais, quando identificáveis

Todas as saídas devem:
- seguir formato previamente documentado, e
- ser passíveis de validação por schema quando aplicável.

---

## Patterns do Fabric Utilizados

Os seguintes patterns cognitivos são aplicados, conforme documentado em `.ai/patterns/`:

- `bibtex_decisao` — geração de entrada BibTeX jurídica
- `classify_document_type` — classificação do tipo documental
- `extract_key_dates` — extração de datas relevantes
- `generate_tags` — geração de tags semânticas

Patterns seguem o repositório oficial do Fabric:  
https://github.com/danielmiessler/Fabric

---

## Fluxos Relacionados

- `djej_to_zotero.flow.md`

Este agente **não executa fluxos por conta própria**, apenas atua quando orquestrado
por um fluxo documentado.

---

## Limites e Restrições

- Não realiza análise de mérito jurídico.
- Não interpreta fundamentos, teses ou conclusões.
- Não substitui revisão humana para metadados críticos.
- Não corrige deficiências graves do texto de entrada.
- Não produz saída não estruturada ou fora dos padrões definidos.

Qualquer extrapolação fora destes limites constitui **violação da governança cognitiva**.

---

## Observações de Governança

- Qualquer alteração no comportamento deste agente exige atualização deste arquivo.
- Nenhuma lógica cognitiva adicional deve ser implementada apenas no código.
- Este documento é um **contrato formal de funcionamento**, não documentação opcional.

