# Metodologia de construção do corpus — MARTA-Ruby

*Documento de referência para o Paper 1 (benchmark/Data Showcase). Descreve o
processo reprodutível de seleção do corpus, as decisões e o racional. Cada passo
tem um script associado em `benchmark/`. Escrito enquanto o processo está fresco;
os números finais da seleção entram na §4 quando o diagnóstico da população
terminar.*

Última atualização: 2026-07-19.

---

## 0. Duas linhas de dados (não confundir)

O trabalho tem **dois conjuntos com papéis distintos**:

| Linha | Fonte | RQ que serve | Métrica |
|---|---|---|---|
| **A. Corpus de cobertura** (este documento) | gems curadas | qualidade dos testes gerados | cobertura, mutation, pass-rate |
| **B. Estudo de bugs reais** | SWE-bench Multilingual (+ Defects4Ruby, futuro) | deteção de faltas (*fixed→buggy*) | bugs apanhados |

A linha B vem pré-selecionada (cada task traz `base_commit`+`patch`+`test_patch`);
não passa pela amostragem descrita aqui. Nota: como a MARTA gera **sempre RSpec**
independentemente do framework do projeto, os **6** repos Ruby do SWE-bench são
utilizáveis (44 tasks), não só os 3 de RSpec.

---

## 1. Objetivo do corpus (linha A)

Um corpus de projetos Ruby reais, diversos, sobre os quais se **gera** testes do
zero (a suite humana é ignorada/apagada) e se mede a qualidade dos testes
gerados. Requisitos: reprodutível, diverso, e defensável perante revisão.

**Decisão de âmbito:** só *library gems*, não aplicações Rails. Racional: as apps
Rails (Mastodon, Discourse…) exigem instalação pesada (BD, serviços, extensões
nativas), o que compromete a reprodutibilidade FAIR e o custo de compute. É uma
ameaça à validade externa, declarada na §5.

---

## 2. Universo de amostragem (*sampling frame*)

**Fonte citável:** [awesome-ruby](https://github.com/markets/awesome-ruby) —
lista curada pela comunidade, organizada por categoria (a categoria fornece
diversidade de domínio de forma objetiva). Snapshot: `master`, 2026-07-19.

**Filtro de popularidade objetivo:** downloads totais no RubyGems.org ≥ **100 M**
(medido via API `rubygems.org/api/v1/gems/<g>.json`). Racional: garante código
"real e amplamente usado"; o limiar contínuo evita um top-N arbitrário.

**Resultado:** 840 candidatas no awesome-ruby (após remover secções não-library:
recursos, frameworks web, serviços…) → **125 gems** acima do limiar, em **55
categorias**. Script: `build_population.py` → `results/population.json`.

> Ameaça: o mapeamento entrada-awesome-ruby → nome-de-gem usa o nome do repo
> (heurística); gems onde repo≠gem podem escapar. Documentado; efeito pequeno no
> topo de popularidade (repo=gem é a norma nas gems mais usadas).

---

## 3. Critérios de inclusão (reprodutíveis, aplicados por script)

Aplicados a cada uma das 125 pela `population_diagnose.py`, que clona (raso),
analisa **estaticamente** e **apaga** o clone (nada é instalado):

1. **É library gem** — tem `lib/` (ou `src/`).
2. **Parseia** — 0 erros de parse do Prism (a MARTA tem de conseguir analisá-la).
3. **Dimensão mínima** — ≥ 15 métodos-alvo (gems minúsculas não dão sinal).
4. **Não é framework/ferramenta** — exclui `rails`, `rake`, `rspec`, `minitest`,
   `bundler`, etc. (lista explícita).

*(A instalabilidade — `bundle install` limpo — só é exigida às FINALISTAS, quando
se medem cobertura/mutation, não na seleção. A seleção é 100% estática.)*

---

## 4. Seleção estratificada por diversidade de código

**Princípio:** de entre as incluídas, escolher para **cobrir o espaço** de
características de código — não por juízo. As métricas (por `diagnose.py`), e a
parte da MARTA que cada uma exercita:

| Métrica | Exercita | Interpretação |
|---|---|---|
| nº métodos, LOC | escala, custo | tamanho do projeto |
| avg LOC/método | contexto do LLM | métodos grandes = prompts grandes |
| % singleton | regime de método | módulo-funções vs OO de instância |
| % duck-typed | inferência de tipos por uso | quão dinâmico é o dispatch |
| mixins/classe, prof. herança | grafo + MRO | complexidade estrutural |
| metaprog/100 métodos | **limite da análise estática** | `define_method`, `method_missing`, `send`… |

**Processo (script de seleção, a correr após o diagnóstico):** normalizar as
métricas, e escolher ~12 que maximizam a cobertura do espaço (extremos + centro
de cada dimensão), garantindo variedade de categoria/domínio. Isto transforma
"porquê estas 12?" numa resposta com dados: *"span das dimensões medidas na
população de 125"*.

> **[A PREENCHER]** número final, tabela das selecionadas, e a distância ao resto
> da população (para mostrar que cobrem os extremos).

---

## 5. Ameaças à validade (a declarar no paper)

- **Popularidade:** enviesamento para gems muito usadas — não representa código
  Ruby "médio" (mas garante relevância e manutenção).
- **Só gems:** apps Rails excluídas (instalação pesada) — decisão explícita.
- **Framework:** ~metade do ecossistema usa Minitest; geramos sempre RSpec (como
  o pytest para Python), e a suite humana serve de baseline de comparação.
- **Mapeamento awesome-ruby→gem** por heurística de nome de repo.
- **Análise estática:** métricas de diversidade dependem do que o Prism resolve;
  metaprogramação é subcontada (é, ela própria, uma das dimensões medidas).

---

## 6. Reprodutibilidade (FAIR)

Toda a construção é re-executável, sem LLM e sem instalar nada no sistema:

```bash
python -m benchmark.build_population       # awesome-ruby ∩ ≥100M downloads → population.json
python -m benchmark.population_diagnose    # clona+mede+apaga cada uma → population_diagnose.json
python -m benchmark.select_corpus          # [a criar] seleção estratificada → corpus final
python -m benchmark.sampling_frame         # verificação: corpus ⊆ universo (ranks de download)
```

Para publicação: fixar os commits das finalistas (pinning), arquivar em
repositório com DOI (Zenodo/OSF), e incluir os `results/*.json` como artefacto.

## 7. Trilho de decisões (registo histórico)

- **Sondagem 1** (`sondagens/s1_callgraph_money/`): call graph estático vs
  dinâmico na `money` — recall 36%→50% após melhorias; validou a análise estática.
- **Sondagem 4** (`sondagens/s4_corpus/`): quantificou o Ruby no SWE-bench
  (44 tasks/6 repos) e o levantamento inicial *ad-hoc* de gems.
- **Correção de rumo** (utilizador): cobertura da suite humana **não** é critério
  de seleção (apagamos os testes humanos); o critério é a **diversidade de
  código**. E a MARTA gera **um** framework (RSpec), como o Test4Py escolheu
  pytest — daí a remoção do backend Minitest.
- **Correção de rumo** (utilizador): a seleção *ad-hoc* de 12 gems carecia de
  fundamento; daí o Caminho B (este documento) — população sistemática.
