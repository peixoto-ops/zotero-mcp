# Fluxo: djej_to_zotero

## Objetivo

Pipeline completo para **ingestão automatizada de acórdãos e decisões**
publicadas no Diário da Justiça Eletrônico (DJe) na biblioteca Zotero,
com extração de metadados, geração de BibTeX e fichamento estruturado.

Este fluxo define **ordem, dependências e validações**, não detalhes
de implementação.

---

## Entradas do Fluxo

- PDF oficial do DJe
- Metadados externos disponíveis (ex.: data da publicação, órgão)

---

## Etapas do Fluxo

### 1. Extração de Conteúdo

Objetivo: obter texto utilizável a partir do PDF oficial.

- Download do PDF do DJe
- Extração de texto
- Normalização do texto (remoção de cabeçalhos, rodapés e artefatos)

> Ferramentas concretas (ex.: `pdftotext`) são detalhes de execução e não
fazem parte da especificação cognitiva.

---

### 2. Identificação do Tipo Documental

Objetivo: determinar a natureza jurídica do documento.

- Pattern aplicado:
  - `classify_document_type`
- Saída esperada:
  - classificação do tipo (ex.: acórdão, decisão monocrática)

---

### 3. Extração de Metadados Jurídicos

Objetivo: identificar informações estruturantes do documento.

- Patterns aplicados:
  - `extract_key_dates`
  - `extract_case_numbers`
  - `extract_tribunal_info`
- Exemplos de dados extraídos:
  - número do processo
  - tribunal / órgão julgador
  - datas relevantes

---

### 4. Geração de Registro BibTeX

Objetivo: criar referência bibliográfica adequada à jurisprudência.

- Pattern aplicado:
  - `bibtex_decisao`
- Requisitos:
  - campos normalizados
  - compatibilidade com Zotero
  - aderência a padrões bibliográficos jurídicos

---

### 5. Fichamento Automático

Objetivo: estruturar o conteúdo para posterior consulta e análise humana.

- Patterns aplicados:
  - `firac_plus`
  - `extract_key_notes`
- Saída:
  - fichamento estruturado
  - destaques de pontos relevantes

Este fichamento **não substitui análise jurídica humana**.

---

### 6. Importação para Zotero

Objetivo: persistir o resultado do fluxo na biblioteca Zotero.

- Criação do item via MCP / API Zotero
- Anexação do PDF original
- Inclusão de:
  - BibTeX
  - anotações estruturadas
  - metadados extraídos

---

## Validação e Controle de Qualidade

- Schema obrigatório:
  - `document_classification.schema.json`
- Verificações mínimas:
  - presença de campos essenciais
  - conformidade estrutural das saídas
- Conformidade bibliográfica:
  - padrões jurídicos (ex.: ABNT quando aplicável)

Falhas de validação devem **interromper o fluxo**.

---

## Saídas Finais do Fluxo

- Item completo na biblioteca Zotero
- PDF original anexado
- Anotações estruturadas vinculadas
- Classificação documental e temática

---

## Limites do Fluxo

- Não realiza juízo de valor jurídico.
- Não interpreta fundamentos ou teses.
- Não garante correção semântica do conteúdo extraído.
- Não executa ações fora das etapas explicitadas.

Qualquer ampliação deste fluxo exige atualização deste documento,
conforme a governança cognitiva do projeto.

