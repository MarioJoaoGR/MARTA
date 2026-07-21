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

**Processo (`select_corpus.py`):** normalizar as métricas (log para tamanho/
profundidade, linear para o resto), e aplicar **farthest-first traversal** —
escolher iterativamente a gem mais distante das já escolhidas no espaço
normalizado. Determinístico (semente = a mais afastada do centróide) e
reprodutível. Restrição: ≤2 gems por categoria (variedade de domínio).

**Refinamento dos critérios de inclusão (achado empírico):** a seleção crua
apanhou extremos **impraticáveis** — gems acopladas a Rails (`activerecord-import`,
`rails-i18n`…, precisam de install pesado) e código **auto-gerado** (`twilio-ruby`,
22 047 métodos de boilerplate). *Extremo matemático ≠ alvo útil.* Adicionados
dois filtros (`select_corpus.py`): (a) excluir dependência runtime de Rails
(rails/activerecord/railties/…); (b) cap de tamanho (>2000 métodos). Efeito:
110 incluídas → 13 Rails + 2 gigantes excluídas → **95 elegíveis**.

## 4b. Portão final: instalabilidade isolada (`finalize_corpus.py`)

A análise estática não vê se uma gem **instala sem dependências pesadas**. Passo
final: percorrer a ordenação de diversidade e, por cada gem, clonar (registar o
**SHA** = pinning) e instalar as **runtime deps do gemspec** (`gem build` +
`gem install`, num `GEM_HOME` isolado no clone; NÃO o Gemfile de dev do repo) —
apagando o clone a seguir. Mantêm-se as 12 primeiras que passam.

**Achado — o portão expôs 4 modos de falha reais** (contribuição metodológica;
qualquer benchmark Ruby os enfrenta):
1. **dev-deps ≠ runtime-deps** — instalar o Gemfile de dev do repo dava falsos
   fracassos (tooling irrelevante que não compila). Correto: só o gemspec.
2. **extensões nativas** (`mysql2`, `bootsnap`, `concurrent-ruby`) — precisam de
   compilação + libs de sistema (não portável ao Deucalion) → excluídas por
   classe (deteção: `ext/**/extconf.rb`).
3. **gemspec dinâmico** (`kramdown` gera-o via Rakefile) — sem gemspec estático,
   build não-standard → excluída por reprodutibilidade.
4. **acoplamento a Rails / plugins de ferramentas** — já filtrado na §4a.

## 4c. CORPUS FINAL (12 gems, verificadas + pinadas, 2026-07-19)

| gem | categoria | métodos | metaprog/100 | singleton% | SHA |
|---|---|---:|---:|---:|---|
| gitlab | third-party apis | 644 | 1.4 | 4 | `8aef58f39f` |
| parallel | concurrency | 53 | 9.4 | 75 | `9bc03fe4e8` |
| rdoc | documentation | 1771 | 1.4 | 5 | `75fecbb911` |
| faker | testing (data-gen) | 1381 | 0.9 | 98 | `cca4184947` |
| connection_pool | database tools | 38 | 2.6 | 8 | `b262ff9981` |
| virtus | core extensions | 204 | **28.4** | 30 | `fce56bd667` |
| formatador | cli utilities | 20 | 0.0 | 0 | `b059e42ee5` |
| addressable | core extensions | 132 | 2.3 | 23 | `d298c9f551` |
| rouge | code highlighting | 844 | 1.8 | 70 | `aed8a2f81e` |
| pry-byebug | debugging tools | 66 | 3.0 | 2 | `5459d85346` |
| sprockets | assets | 485 | 1.9 | 11 | `834279b163` |
| httparty | http clients | 238 | 8.8 | 13 | `2daba91bf3` |

**Span:** métodos 20→1771 · metaprog 0→28.4/100 · singleton 0→98% · avg
LOC/método 4.0→18.3 · **11 categorias distintas**.

**Validação:** das 12 *ad-hoc* iniciais, só 3 (`addressable`, `faker`, +`httparty`
via ordenação estendida) sobreviveram à seleção sistemática — a escolha por juízo
**não** coincidia com a diversidade real. Prova que o Caminho B era necessário.

> Borderline (variedade OK, mas são extensões de outras ferramentas): `pry-byebug`
> (plugin do pry), `sprockets` (pipeline de assets). Instalam limpo, logo válidos;
> podem trocar-se por `state_machines` (DSL, metaprog 20.7) ou `timecop` se se
> preferir "libraries puras". Decisão do corpus final.

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
