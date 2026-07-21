# Corpus — diagnóstico de diversidade de código (2026-07-19)

Critério de seleção = **diversidade do código Ruby** (não a suite humana; nós
geramos os testes e medimos os nossos). Cada métrica exercita uma parte
diferente da MARTA. Gerado por `python -m benchmark.diagnose <paths>` (sem LLM,
sem cobertura — rápido). 12 candidatas com **0 erros de parse** em todas.

| gem | métodos | classes | LOC | avg loc/mét | % singleton | % duck | mixins/cl | prof. herança | metaprog/100 | domínio |
|---|---|---|---|---|---|---|---|---|---|---|
| public_suffix | 45 | 9 | 1067 | 5.6 | 31% | 42% | 0.0 | 3 | **0.0** | DNS/lookup puro |
| money | 150 | 22 | 2830 | 6.5 | 23% | 27% | 0.0 | 2 | 1.3 | aritmética/finança |
| addressable | 132 | 10 | 8491 | **18.2** | 23% | 52% | 0.1 | 1 | 2.3 | parsing URI |
| ruby-jwt | 208 | 54 | 2832 | 5.7 | 21% | 35% | 0.17 | 3 | **0.0** | cripto/segurança |
| httparty | 238 | 27 | 2906 | 6.6 | 13% | 22% | 0.07 | 4 | 8.8 | cliente HTTP/IO |
| hashie | 256 | 16 | 3276 | 6.2 | 17% | 52% | **1.0** | **5** | **19.1** | metaprogramação |
| chronic | 269 | 72 | 3587 | 8.6 | 15% | 49% | 0.03 | 4 | 1.5 | parsing NL de datas |
| i18n | 265 | 30 | 4699 | 6.6 | 16% | 35% | 0.43 | 4 | 3.8 | internacionalização |
| kramdown | 328 | 19 | 8547 | 10.8 | 10% | **62%** | 0.37 | 4 | 5.8 | parser markdown |
| rubyzip | 387 | 47 | 4916 | 7.2 | **5%** | 30% | 0.45 | 3 | 4.4 | arquivo/binário |
| liquid | 478 | 84 | 6967 | 7.9 | 12% | 35% | 0.11 | 4 | 3.1 | template DSL |
| faker | **1381** | **260** | **22402** | 4.8 | **98%** | 11% | 0.0 | 2 | 0.9 | geração de dados |

## O espectro (os extremos que dão variedade)

- **Tamanho:** `public_suffix` (45 métodos) ↔ `faker` (1381). ~30× de amplitude.
- **Metaprogramação:** `ruby-jwt`/`public_suffix` (0.0, análise estática ideal) ↔
  `hashie` (19.1 — stress-test do parser/grafo; `define_method`/`method_missing`).
- **Estrutura singleton:** `rubyzip` (5%, tudo métodos de instância) ↔ `faker`
  (98%, tudo métodos de classe/módulo — regime oposto).
- **Tamanho de método:** `faker` (4.8, minúsculos) ↔ `addressable` (18.2, enormes
  — stress no contexto do LLM).
- **Mixins/herança:** `money`/`faker` (0.0, planos) ↔ `hashie` (1.0/classe, prof. 5).
- **Duck-typing:** `httparty` (22%) ↔ `kramdown` (62% — muita inferência por uso).

## Percalços
- **`mustermann`**: sem `lib/` na raiz — é um **monorepo** (sub-gems em
  `mustermann-*/`). Excluída (ou apontar a um sub-gem). Não é preciso: já temos 12.

## Recomendação de corpus (v1) — **as 12, span completo**
Cobrem 12 domínios distintos E os extremos de todas as métricas estruturais.
Nenhuma é redundante. Divisão sugerida para o Deucalion (custo × sinal):

- **Núcleo (corrido a fundo: cobertura + mutation + comparação humana):**
  `money`, `ruby-jwt`, `httparty`, `hashie`, `kramdown`, `rubyzip` — spanem
  tamanho, metaprog (0→19), IO vs puro, singleton vs instância.
- **Extensão (cobertura + pass-rate):** `public_suffix`, `addressable`, `i18n`,
  `chronic`, `liquid`, `faker` — variedade extra; `faker` como outlier de escala.

## Nota de custo (Deucalion)
`faker` (1381 métodos) e `liquid` (478) dominam o compute. Opções: correr por
último, ou amostrar métodos. O outlier de escala tem valor (o utilizador quer a
variedade), mas o orçamento tem de contar com ele explicitamente.
