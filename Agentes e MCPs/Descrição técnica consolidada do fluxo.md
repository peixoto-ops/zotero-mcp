---
share_link: https://share.note.sx/grwwhnh0
share_updated: 2026-01-05T13:45:21-03:00
reference_document: true
warning: Este arquivo é de referência inicial e não deve ser seguido sem consultar anteriormente a documentação existente. Em caso de divergência, apenas aquilo que for designado explicitamente como complemento a implementar poderá gerar atualizações. Todas as atualizações precisam ser confirmadas identificando o estado atual do projeto e o estado da documentação de referência.
---


## 1. Descrição técnica consolidada do fluxo (versão “oficial”)

### Visão geral

O sistema é um **orquestrador de produção jurídica assistida por múltiplos agentes**, integrado ao **Zotero**, **Obsidian** e **Fabric**, com foco em:

- análise profunda de precedentes;
    
- construção controlada de teses jurídicas;
    
- redação modular e verificável de peças processuais;
    
- preservação de cadeia de custódia e rastreabilidade probatória.
    

Cada **fluxo jurídico** (ex.: processamento de um acórdão, elaboração de uma petição, análise de prova audiovisual) é **decomposto em patterns especializados**, executados por **agentes distintos**, com responsabilidades bem definidas.

---

### Etapas macro do fluxo

#### (A) Ingestão e análise de precedentes

Para cada acórdão ou documento jurídico:

- Extração estruturada por patterns:
    
    - **NER jurídico** (partes, órgãos, datas, dispositivos, temas)
        
    - **FIRAC+** (Fatos, Questões, Ratio, Argumentos, Conclusão + Observações estratégicas)
        
    - **Classificação temporal e estratégica**
        
        - leading case
            
        - julgado de consolidação
            
        - tese emergente
            
        - distinguishing possível
            
- Geração automática de:
    
    - **entrada BibTeX**
        
    - **nota de fichamento em Markdown**
        
    - **metadados de uso processual**
        

➡️ Tudo é exportado e sincronizado com o **Zotero**, mantendo ligação bidirecional com o Obsidian.

---

#### (B) Construção de contexto do caso

Em paralelo, um agente dedicado:

- consulta a **base de conhecimento no Obsidian**;
    
- recupera:
    
    - histórico do caso;
        
    - teses já trabalhadas;
        
    - decisões anteriores;
        
    - notas manuais ou geradas pelo Copilot;
        
- produz um **contexto sintético e operacional**, que será usado pelos demais agentes.
    

Esse contexto funciona como um **“briefing jurídico vivo”**.

---

#### (C) Definição da estratégia jurídica

Com base em:

- precedentes analisados;
    
- contexto do caso;
    
- objetivo processual;
    

o sistema:

1. **define a estratégia central**
    
2. **valida a existência real dos precedentes que a sustentam**
    
3. só então autoriza a etapa de redação
    

➡️ Isso evita construir teses “bonitas” sem lastro jurisprudencial.

---

#### (D) Criação do TOC (esqueleto da petição)

É gerado um **TOC jurídico**, que funciona como:

- rascunho argumentativo;
    
- mapa lógico da peça;
    
- estrutura-base para Longform.
    

Cada item do TOC é um **nó independente**, que depois se tornará uma nota.

---

#### (E) Desdobramento dos tópicos em três vieses

Cada tópico do TOC é desenvolvido em **três dimensões complementares**:

---

##### 1. Direito (lei e doutrina)

- fundamentação legal e constitucional;
    
- identificação explícita dos pontos a serem:
    
    - **prequestionados**;
        
    - discutidos em **RE e RESP**;
        
- formulação clara das **questões de direito**.
    

---

##### 2. Jurisprudência

- encaixe dos precedentes:
    
    - por categoria (tema, órgão, tese);
        
    - por posição temporal (linha do tempo);
        
- suporte a:
    
    - teses inovadoras;
        
    - julgados de vanguarda;
        
    - distinguishing fundamentado.
        

Aqui entram diretamente os resultados do **agente de precedentes**.

---

##### 3. Questões de fato e prova

Etapa sensível e técnica:

- extração de fatos a partir de:
    
    - documentos;
        
    - imagens;
        
    - vídeos;
        
- seleção de:
    
    - frames relevantes;
        
    - recortes de documentos;
        
- vinculação explícita entre:
    
    - fato → prova → tese jurídica;
        
- geração de:
    
    - citações ABNT do documento original;
        
    - hash criptográfico;
        
    - carimbo de tempo.
        

---

#### (F) Normalização técnica e cadeia de custódia

Antes da finalização:

- normalização de arquivos:
    
    - tamanho;
        
    - formato;
        
    - resolução;
        
- observância dos **requisitos mínimos mais conservadores**, compatíveis com:
    
    - diferentes sistemas judiciais (no RJ, ao menos três);
        
- conversão automática quando necessário;
    
- armazenamento seguro:
    
    - GitHub privado;
        
    - senha;
        
    - Git LFS para arquivos grandes;
        
- preservação integral da **cadeia de custódia digital**.
    

---

#### (G) Redação modular com Longform (Obsidian)

Uso do **Longform** como camada final:

- um **documento mestre** representa a petição;
    
- cada item do TOC vira uma **nota independente**;
    
- essas notas:
    
    - são editáveis isoladamente;
        
    - já contêm links para:
        
        - fichamentos do Zotero;
            
        - precedentes;
            
        - provas.
            

Como o processo é automatizado desde a ingestão dos acórdãos:

> rodar o pipeline significa **validar, classificar e encaixar automaticamente** o argumento de autoridade no ponto exato da petição.

---

## 2. Arquitetura de agentes (sugestão clara)

### Agentes principais

1. **Agente de Precedentes**
    
    - FIRAC+
        
    - NER
        
    - classificação temporal
        
    - BibTeX
        
    - fichamento
        
2. **Agente de Contexto**
    
    - consulta Obsidian
        
    - síntese do caso
        
    - briefing jurídico
        
3. **Agente de Estratégia**
    
    - valida precedentes
        
    - define linha argumentativa
        
    - autoriza redação
        
4. **Agente de TOC**
    
    - cria esqueleto da petição
        
    - organiza tópicos
        
5. **Agente de Redação Jurídica**
    
    - desenvolve os três vieses
        
    - integra doutrina, jurisprudência e fatos
        
6. **Agente de Prova e Cadeia de Custódia**
    
    - frames
        
    - hashes
        
    - normalização
        
    - metadados
        
7. **Agente Zotero**
    
    - sincronização
        
    - criação de itens
        
    - links cruzados
        

---

## 3. Fluxo implementável (mental model de orquestrador)

```text
INPUT (acórdãos, documentos, vídeos)
        ↓
Agente de Precedentes ──┐
                        ├──→ Agente de Estratégia → TOC
Agente de Contexto ─────┘
                                ↓
                    Agente de Redação (3 vieses)
                                ↓
              Agente de Prova e Cadeia de Custódia
                                ↓
                 Longform (Obsidian) + Zotero
                                ↓
                      Petição final rastreável
```

---

## Conclusão

**Não é apenas automação** — é um **sistema de engenharia jurídica**, com:

- separação clara de responsabilidades;
    
- auditabilidade;
    
- rastreabilidade;
    
- e redução real de risco de erro ou alucinação.
    

