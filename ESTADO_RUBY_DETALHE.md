# MARTA-Ruby — o que existe, onde está, e o que ainda NÃO temos

*Referência factual (2026-07-23). Cada número aqui foi medido e tem ficheiro de
origem. Serve para responder a perguntas sem arriscar afirmações não suportadas.*

---

## ⚠️ 1. Duas correções ao email (antes de falar)

### 1.1 O número do PyCG está errado
O email diz que o PyCG *"anda muitas vezes pelos 50-60% em projetos reais"*.
**O paper do PyCG (ICSE 2021) reporta ~69.9% de recall** (e ~99.2% de precisão)
nos macro-benchmarks com pacotes Python reais. Nunca verificámos os 50-60% — é
um número inventado, e é verificável em 30 segundos por quem ouvir.

### 1.2 Os números não são diretamente comparáveis
O nosso 49.6% e o 69.9% do PyCG **medem-se de maneiras diferentes**:
- **PyCG**: ground truth **anotado manualmente** (micro + macro benchmarks).
- **Nós**: ground truth **observado dinamicamente** (execução da suite), o que
  é mais conservador e tem vieses que documentámos (só vê o que a suite corre;
  não vê métodos C-level como `attr_reader`).

**Formulação segura** (mantém a força do argumento sem expor a afirmação):
> "Para contexto: o PyCG — a ferramenta madura de referência para Python,
> publicada no ICSE — reporta cerca de 70% de recall em projetos reais. Ou seja,
> mesmo o estado da arte numa linguagem com muito mais investimento está longe
> dos 100%. Ter ~50% num primeiro analisador para Ruby, medido de forma
> conservadora (e não diretamente comparável, porque o PyCG usa ground truth
> anotado à mão e nós usámos execução real), parece-me uma base sólida."

---

## 2. O que MEDIMOS (resultados que existem)

| # | Resultado | Valor | Ficheiro |
|---|---|---|---|
| 1 | **Recall do call graph estático** (gem `money`) | 35.9% → **49.6%** após melhorias | `sondagens/s1_callgraph_money/RESULTADOS.md` |
| 2 | Cobertura da suite humana da `money` (validação do instrumento) | 99.8% | idem |
| 3 | **Mutation score** com o `mutant` (`Money#hash`) | 91.66% (12 mutações, 11 mortas) | `sondagens/s3_mutant/RESULTADOS.md` |
| 4 | Ruby no **SWE-bench Multilingual** | 44 tarefas / 6 repos | `sondagens/s4_corpus/RESULTADOS.md` |
| 5 | **Corpus final** | 12 gems, SHAs fixados | `benchmark/results/corpus_final.json` |
| 6 | População de amostragem | 125 gems (110 analisáveis → 92 elegíveis) | `benchmark/results/population.json` |
| 7 | Parser em projetos reais | **0 erros** em ~110 gems | `population_diagnose.json` |
| 8 | Ferramenta (testes unitários) | 92 testes verdes | `marta/ruby_backend/tests/` |
| 9 | Smoke E2E em projeto real (`fpm`) | 3/3 specs gerados e a passar | logs locais |

### Detalhe do resultado #1 (o do call graph — o mais citável)
- Alvo: gem `money` (20 ficheiros, 150 métodos, suite de 499 testes).
- Estático: **231 arestas**; dinâmico observado: **248**; interseção: **123**.
- Recall = 123/248 = **49.6%** (antes das melhorias: 89/248 = 35.9%).
- As 3 melhorias que subiram o número: (i) métodos em `class << self`,
  (ii) colaboradores em variáveis de instância/getters, (iii) `self.class.new`.
- ⚠️ **Medimos recall, não precisão** (as 108 arestas "só estáticas" misturam
  arestas reais-não-exercitadas, `attr_*` invisíveis ao tracer, e eventuais
  falsos positivos). Está documentado na secção "Validade da medição".

---

## 3. Onde está tudo (mapa)

```
Test4Py/
├── marta/ruby_backend/          ← A FERRAMENTA (código)
│   ├── call_graph.py               analisador estático (o "PyCG nosso")
│   ├── dyn_call_graph.py           tracer dinâmico + comparador (só p/ avaliar)
│   ├── rb/marta_parse.rb           parser sobre o Prism
│   ├── tests/                      92 testes
│   └── PARIDADE.md                 mapa Python↔Ruby (material p/ paper)
├── benchmark/                   ← O BENCHMARK
│   ├── build_population.py         (1) awesome-ruby ∩ ≥100M downloads → 125
│   ├── population_diagnose.py      (2) análise estática de todos → 110
│   ├── select_corpus.py            (3+4) filtros → 92; diversidade → ordenação
│   ├── finalize_corpus.py          (5) instalabilidade + fixa SHAs → 12
│   ├── run_ruby_benchmark.py       harness de execução (para o Deucalion)
│   ├── results/corpus_final.json   ← O CORPUS (12 gems + SHAs)
│   ├── METODOLOGIA.md              ← metodologia p/ o Paper 1
│   └── PROVENIENCIA.md             ← defesa da seleção
├── sondagens/s1,s3,s4/RESULTADOS.md  ← os resultados medidos
└── deucalion/run_ruby_benchmark.sh   ← job SLURM (pronto, nunca submetido)
```

**Nota:** os artefactos do corpus estavam apenas no disco local (gitignored) —
corrigido a 2026-07-23, agora versionados.

---

## 4. O que AINDA NÃO temos (não afirmar)

- ❌ **Nenhum resultado de qualidade dos testes gerados em escala** — não há
  ainda números de cobertura ou mutation score da MARTA-Ruby sobre o corpus.
  Só o smoke de 3 métodos na `fpm`. Toda a avaliação depende do Deucalion.
- ❌ **Comparação com o cover-agent** — validado que funciona mecanicamente
  (corri no exemplo Ruby deles), mas **eficácia não medida**.
- ❌ **Defects4Ruby** — identificado, **não reproduzido**.
- ❌ **Ruby não está instalado no Deucalion** — é o bloqueio operacional nº1
  (o container não o tem; é preciso compilá-lo no login node).
- ⚠️ Medição do grafo feita **numa única gem** (`money`). Generalizar exigiria
  repetir noutras — está previsto, não feito.

---

## 5. Como responder a perguntas prováveis

**"Isto funciona mesmo?"** → Sim, ponta-a-ponta: gera, executa, mede cobertura.
Provado num repo real do SWE-bench (`fpm`). Falta só a escala.

**"49.6% não é pouco?"** → Ver §1.2. É recall medido de forma conservadora; o
estado da arte em Python (PyCG, ICSE) reporta ~70% com metodologia mais
favorável. E o grafo não precisa de estar completo para ser útil: serve para
enriquecer o contexto dado ao LLM, não para provar propriedades do programa.

**"Porquê 12 projetos?"** → Número escolhido para caber no orçamento de compute;
o processo produz uma ordenação, portanto "os primeiros k" é válido para qualquer
k. Os 12 cobrem 11 domínios e o espectro completo das métricas de diversidade.

**"E se alguém já fez isto?"** → Verificação documentada: no survey de referência
da área (AwesomeLLM4SE, 1711 linhas) **o Ruby não é mencionado uma única vez**.
As buscas no GitHub e no RubyGems não devolvem nenhum gerador. A formulação
correta é "to the best of our knowledge".
