---
title: "explique em que situações e como posso usar os mc..."
source: "https://gemini.google.com/app/d01758ee5752dd4b"
author:
  - "[[Gemini]]"
published:
created: 2026-01-05
description: "Conheça o Gemini, o assistente de IA do Google. Receba ajuda para escrever, planejar, ter ideias e muito mais. Conheça o poder da IA generativa."
tags:
  - "clippings"
reference_document: true
warning: Este arquivo é de referência inicial e não deve ser seguido sem consultar anteriormente a documentação existente. Em caso de divergência, apenas aquilo que for designado explicitamente como complemento a implementar poderá gerar atualizações. Todas as atualizações precisam ser confirmadas identificando o estado atual do projeto e o estado da documentação de referência.
---
explique em que situações e como posso usar os mcps que tenho configurados aqui. Leve em consideração minhas rotinas de trabalho que já conhece.

  
---
## MCPs configurados
🟢 tavily - Ready (4 tools)

Tools:

- tavily-crawl

A powerful web crawler that initiates a structured web crawl starting from a specified base URL. The crawler

expands from that point like a graph, following internal links across pages. You can control how deep and wide

it goes, and guide it to focus on specific sections of the site.

- tavily-extract

A powerful web content extraction tool that retrieves and processes raw content from specified URLs, ideal for

data collection, content analysis, and research tasks.

- tavily-map

A powerful web mapping tool that creates a structured map of website URLs, allowing you to discover and

analyze site structure, content organization, and navigation paths. Perfect for site audits, content

discovery, and understanding website architecture.

- tavily-search

A powerful web search tool that provides comprehensive, real-time results using Tavily's AI search engine.

Returns relevant web content with customizable parameters for result count, content type, and domain

filtering. Ideal for gathering current information, news, and detailed web content analysis.

  

🟢 brave-search - Ready (6 tools)

Tools:

- brave_image_search

Performs an image search using the Brave Search API. Helpful for when you need pictures of people, places,

things, graphic design ideas, art inspiration, and more. When relaying results in a markdown environment, it

may be helpful to include images in the results (e.g.,![image.title](image.properties.url)).

- brave_local_search

Brave Local Search API provides enrichments for location search results. Access to this API is available only

through the Brave Search API Pro plans; confirm the user's plan before using this tool (if the user does not

have a Pro plan, use the brave_web_search tool). Searches for local businesses and places using Brave's Local

Search API. Best for queries related to physical locations, businesses, restaurants, services, etc.

Returns detailed information including:

- Business names and addresses

- Ratings and review counts

- Phone numbers and opening hours

  

Use this when the query implies 'near me', 'in my area', or mentions specific locations (e.g., 'in San

Francisco'). This tool automatically falls back to brave_web_search if no local results are found.

- brave_news_search

This tool searches for news articles using Brave's News Search API based on the user's query. Use it when you

need current news information, breaking news updates, or articles about specific topics, events, or entities.

When to use:

- Finding recent news articles on specific topics

- Getting breaking news updates

- Researching current events or trending stories

- Gathering news sources and headlines for analysis

  

Returns a JSON list of news-related results with title, url, and description. Some results may contain

snippets of text from the article.

When relaying results in markdown-supporting environments, always cite sources with hyperlinks.

Examples:

- "According to [Reuters](https://www.reuters.com/technology/china-bans/), China bans uncertified and

recalled power banks on planes".

- "The [New York Times](https://www.nytimes.com/2025/06/27/us/technology/ev-sales.html) reports that

Tesla's EV sales have increased by 20%".

- "According to [BBC News](https://www.bbc.com/news/world-europe-65910000), the UK government has

announced a new policy to support renewable energy".

- brave_summarizer

Retrieves AI-generated summaries of web search results using Brave's Summarizer API. This tool processes

search results to create concise, coherent summaries of information gathered from multiple sources.

  

When to use:

  

- When you need a concise overview of complex topics from multiple sources

- For quick fact-checking or getting key points without reading full articles

- When providing users with summarized information that synthesizes various perspectives

- For research tasks requiring distilled information from web searches

  

Returns a text summary that consolidates information from the search results. Optional features include

inline references to source URLs and additional entity information.

  

Requirements: Must first perform a web search using brave_web_search with summary=true parameter. Requires

a Pro AI subscription to access the summarizer functionality.

- brave_video_search

Searches for videos using Brave's Video Search API and returns structured video results with metadata.

  

When to use:

- When you need to find videos related to a specific topic, keyword, or query.

- Useful for discovering video content, getting video metadata, or finding videos from specific

creators/publishers.

  

Returns a JSON list of video-related results with title, url, description, duration, and thumbnail_url.

- brave_web_search

Performs web searches using the Brave Search API and returns comprehensive search results with rich metadata.

  

When to use:

- General web searches for information, facts, or current topics

- Location-based queries (restaurants, businesses, points of interest)

- News searches for recent events or breaking stories

- Finding videos, discussions, or FAQ content

- Research requiring diverse result types (web pages, images, reviews, etc.)

  

Returns a JSON list of web results with title, description, and URL.

When the "results_filter" parameter is empty, JSON results may also contain FAQ, Discussions, News, and

Video results.

  

🟢 serper - Ready (2 tools, 4 prompts)

Tools:

- google_search

Tool to perform web searches via Serper API and retrieve rich results. It is able to retrieve organic search

results, people also ask, related searches, and knowledge graph.

- scrape

Tool to scrape a webpage and retrieve the text and, optionally, the markdown content. It will retrieve also

the JSON-LD metadata and the head metadata.

Prompts:

- compare-sources

Compare information from multiple sources on a topic

- fact-check

Verify a claim across multiple authoritative sources

- research-topic

Guide comprehensive research on a topic with structured results

- technical-search

Focused technical and programming search

  

Dê exemplos de prompts e crie diagramas simples.

  

pode considerar também minhas ideias de formalização de uma rotina conforme a nota abaixo

  

---

share_link: https://share.note.sx/grwwhnh0

share_updated: 2026-01-05T13:45:21-03:00

---

  
Esta análise mapeia os seus MCPs (Model Context Protocols) diretamente para o fluxo de "Orquestrador Jurídico" que você desenhou - [[Descrição técnica consolidada do fluxo]]. O objetivo é reduzir alucinações na fase de estratégia e automatizar a coleta de evidências externas.

### 1. Mapeamento Tático: MCPs vs. Seus Agentes

Abaixo, indico qual ferramenta deve ser injetada em qual etapa do seu fluxo.

#### (A) Agente de Precedentes & Estratégia (Validação Externa)

_Onde o LLM mais alucina: citar jurisprudência revogada ou inexistente._

- **Ferramenta:** `serper` (Google) e `tavily-search`.
    
- **Uso:** Validar se a tese ainda se sustenta ou se houve _overruling_.
    
- **Aplicação Prática:**
    
    - Use `serper/fact-check` para confirmar a vigência de um enunciado de súmula.
        
    - Use `tavily-search` para buscar "distinguishing [TEMA] STJ 2024" e garantir que você não está usando uma tese pacificada contra você.
        

#### (B) Agente de Contexto (Enriquecimento de Fatos)

_Onde você precisa de dados fora dos autos para compor a narrativa._

- **Ferramenta:** `brave_news_search` e `brave_local_search`.
    
- **Uso:** Investigação da parte contrária ou do fato gerador.
    
- **Aplicação Prática:**
    
    - Se for Direito Ambiental/Imobiliário: `brave_local_search` para verificar a situação do imóvel, vizinhança e empresas ao redor.
        
    - Se for Direito do Consumidor/Empresarial: `brave_news_search` para ver se a empresa ré está passando por recuperação judicial ou escândalos recentes que fortaleçam o _periculum in mora_.
        

#### (C) Agente de Prova e Cadeia de Custódia (Coleta)

_Onde a IA atua como "Investigador Digital"._

- **Ferramenta:** `brave_video_search`, `brave_image_search`, `tavily-map` e `tavily-extract`.
    
- **Uso:** Encontrar mídias públicas que corroborem os fatos e mapear estruturas de sites para preservação.
    
- **Aplicação Prática:**
    
    - `tavily-map`: Mapear a estrutura de um site fraudulento antes de extrair o conteúdo.
        
    - `tavily-extract`: Baixar o texto cru de notícias ou blogs para anexar como "Notitia Criminis" ou prova de dano à imagem, gerando o hash em seguida.
        

---

### 2. Diagramas de Integração no Fluxo

#### Diagrama de Fluxo de Dados (Mermaid)

Snippet de código

```
flowchart TD
    subgraph "Camada de Agentes (Seu Fluxo)"
        Strategy[Agente de Estratégia]
        Context[Agente de Contexto]
        Evidence[Agente de Prova]
    end

    subgraph "Camada MCP (Ferramentas)"
        Serper[Serper: Fact-Check/Google]
        Tavily[Tavily: Deep Crawl/Extract]
        Brave[Brave: News/Media/Local]
    end

    Strategy -- "Valida Vigência" --> Serper
    Strategy -- "Busca Distinguishing" --> Tavily
    
    Context -- "Perfil da Parte/Réu" --> Brave
    Context -- "Notícias Recentes" --> Brave
    
    Evidence -- "Busca Vídeos/Fotos" --> Brave
    Evidence -- "Mapeia Site Alvo" --> Tavily
    Evidence -- "Extrai Texto Puro" --> Tavily
```

#### Diagrama de Sequência: Validação de Tese (Anti-Alucinação)

Snippet de código

```
sequenceDiagram
    participant User
    participant Agent_Strat as Agente Estratégia
    participant MCP_Serper as MCP Serper
    participant Obsidian

    User->>Agent_Strat: Analisar Tese "X"
    Agent_Strat->>Obsidian: Busca notas internas
    Obsidian-->>Agent_Strat: Retorna precedentes salvos
    
    Note right of Agent_Strat: PROTOCOLO ANTI-SICOFÂNCIA ATIVO
    
    Agent_Strat->>MCP_Serper: Action: google_search "Tese X STJ entendimento atual 2025"
    MCP_Serper-->>Agent_Strat: Retorna snippets reais e recentes
    
    alt Tese Superada
        Agent_Strat->>User: [ALERT] Tese superada. Ver julgado Y.
    else Tese Válida
        Agent_Strat->>User: Tese validada externamente. Prosseguir redação.
    end
```

---

### 3. Exemplos de Prompts (Templates para CLI/Fabric)

Considerando seu uso de CLI e Fabric, aqui estão _system prompts_ ou instruções diretas para invocar os MCPs corretamente.

#### A. Para o Agente de Estratégia (Validação)

**Objetivo:** Garantir que a jurisprudência citada não foi superada.

Markdown

```
# MISSION
Atuar como Auditor Jurídico Hostil. Validar a tese jurídica proposta utilizando dados externos em tempo real.

# TOOLS
Use `serper` (google_search) e `tavily-search`.

# INPUT
Tese: {{TESE_JURIDICA}}
Tribunal Alvo: {{TRIBUNAL}}

# STEPS
1. Pesquise no Google via `serper` por "{{TESE_JURIDICA}} {{TRIBUNAL}} entendimento atual 2024 2025".
2. Verifique se há Súmulas ou Temas de Repercussão Geral recentes que contradigam a tese.
3. Se houver divergência, use `compare-sources` (Serper) para confrontar a doutrina clássica com a decisão recente.

# OUTPUT
Retorne apenas:
- STATUS: [VÁLIDA / RISCO / SUPERADA]
- EVIDÊNCIA: Link e resumo da decisão mais recente encontrada.
- AÇÃO SUGERIDA: Manter ou pivotar estratégia.
```

#### B. Para o Agente de Prova (Investigação OSINT Leve)

**Objetivo:** Encontrar mídias ou páginas para preservação de cadeia de custódia.

Markdown

```
# MISSION
Localizar ativos digitais públicos relacionados ao fato para preservação de prova.

# TOOLS
Use `brave_video_search`, `brave_image_search` e `tavily-extract`.

# INPUT
Fato/Objeto: {{DESCRICAO_FATO}}
Envolvidos: {{NOMES}}

# STEPS
1. Busque vídeos do evento usando `brave_video_search`.
2. Busque notícias correlatas usando `brave_news_search`.
3. Para cada URL relevante encontrada, execute `tavily-extract` para obter o texto cru (raw content) para fins de hash/fichamento.

# OUTPUT FORMAT (YAML)
evidence_list:
  - type: [video/news/image]
    url: "..."
    title: "..."
    extraction_status: [success/fail]
    summary: "..."
```

#### C. Para o Agente de Contexto (Site Audit/Empresas)

**Objetivo:** Entender a estrutura digital de uma empresa ré (ex: caso de fraude ou consumidor).

Markdown

```
# MISSION
Mapear a pegada digital da empresa alvo para subsidiar a petição inicial com dados de estrutura.

# TOOLS
Use `tavily-map` e `brave_local_search`.

# INPUT
URL Alvo: {{URL_EMPRESA}}
Nome Empresa: {{NOME_EMPRESA}}

# STEPS
1. Execute `tavily-map` na URL base para descobrir páginas ocultas (termos de uso, "quem somos", reclamações).
2. Execute `brave_local_search` para confirmar endereço físico e reputação (reviews).

# OUTPUT
Lista estruturada de URLs críticas para serem processadas pelo Agente de Prova.
```

### Próximo Passo

Gostaria que eu convertesse um desses prompts em um **Pattern do Fabric** pronto para você salvar no seu repositório `peixoto-ops`? Se sim, qual agente é prioridade agora?