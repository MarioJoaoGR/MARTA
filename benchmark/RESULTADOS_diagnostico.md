# Diagnóstico das candidatas ao corpus (2026-07-19)

Produzido por `python -m benchmark.diagnose <paths>` (sem LLM). Output máquina em
`benchmark/results/diagnose.json`, tabela em `benchmark/results/diagnose.md`.

## Tabela

| gem | fw | ficheiros | LOC | métodos | classes | arestas | erros parse | cobertura-base | métodos 100% |
|---|---|---|---|---|---|---|---|---|---|
| money | rspec | 20 | 2830 | 150 | 22 | 231 | 0 | 99.8% | 149 |
| ruby-jwt | rspec | 47 | 2832 | 208 | 54 | 317 | 0 | 95.7% | 201 |
| **httparty** | rspec | 24 | 2906 | 238 | 27 | 400 | 0 | **25.4%** | 4 |
| i18n | minitest | 46 | 4699 | 265 | 30 | 353 | 0 | 91.8% | 205 |
| rubyzip | minitest | 48 | 4916 | 387 | 47 | 543 | 0 | 95.0% | 337 |
| addressable | rspec | 7 | 8491 | 132 | 10 | 350 | 0 | n/d ⚠️ | — |
| faker | minitest | 253 | 22402 | 1381 | 260 | 204 | 0 | n/d ⚠️ | — |

## Achados

### 1. Parser: **0 erros em 7 gems** (445 ficheiros, ~49k LOC, 2761 métodos)
O parser Prism e a frente estática aguentam projetos reais de ambos os
frameworks sem uma única falha de parse. Robustez confirmada fora da `money`.

### 2. 🔴 Gems Ruby maduras são MUITO bem testadas — pouca margem para ganho
Das 5 medidas, **quatro estão acima de 91%** e três acima de 95%. Só a
`httparty` (25.4%) deixa espaço claro para uma ferramenta demonstrar ganho de
cobertura. Isto é **um resultado a reportar** (ameaça à validade externa de
qualquer avaliação de geração de testes em Ruby) e um critério de curadoria:
**um corpus só de gems maduras mede pouco**. Convém misturar:
- gems com cobertura baixa/média (headroom real) — ex.: `httparty`;
- gems muito cobertas (medem *pass rate* e qualidade, não ganho de cobertura);
- e, para ganho, considerar **medir por módulo** em vez de projeto inteiro
  (mesmo na `money`, métodos individuais têm linhas por cobrir).

### 3. ⚠️ Dois modos de falha do harness (critérios de inclusão)
- **`faker`**: o `test_helper` do projeto arranca **SimpleCov**, que colide com
  o nosso `Coverage.start` (deprecation fatal). Projetos que já instrumentam
  cobertura precisam de tratamento especial: desligar a instrumentação deles
  (muitos usam `ENV["COVERAGE"]`) ou **consumir o `.resultset.json` do próprio
  SimpleCov** em vez de medir nós. → decisão de desenho pendente.
- **`addressable`**: a medição devolve **zero ficheiros** — as specs resolvem
  `addressable/*` a partir do **gem instalado**, não do `lib/` local, por isso
  nenhum caminho coberto cai sob o nosso prefixo. Precisa de forçar o load path
  local (ou `bundle exec` com a gem em modo path).

### 4. Convenções de nome em Minitest (percalço corrigido)
Coexistem `foo_test.rb` (i18n, rubyzip) e `test_foo.rb` (faker). Apanhar só uma
convenção perde a suite inteira — o `diagnose` cobre agora ambas.

### 5. Dependências como critério
A `i18n` exigiu `mocha`; só mediu após `bundle install` completo. Fragilidade de
instalação é critério de exclusão (e argumento para fixar Dockerfiles).

## Percalços corrigidos no harness (durante o diagnóstico)
1. `coverage_runner` fazia `json.loads` direto ao stdout — o `spec_helper` da
   `ruby-jwt` imprime a versão do OpenSSL e corrompia o parse. Agora extrai o
   payload defensivamente (como o `runner.py` já fazia).
2. Modo minitest não punha `test/` no `$LOAD_PATH` → `LoadError` em
   `require "test_helper"` (é o que o `rake test -Ilib -Itest` faz).

## Corpus recomendado (v1) — a fixar
**Núcleo sólido (medição fiável, ambos os frameworks):**
`httparty` (rspec, 25.4% — headroom) · `money` (rspec, 99.8%) ·
`ruby-jwt` (rspec, 95.7%) · `rubyzip` (minitest, 95.0%) · `i18n` (minitest, 91.8%)

**A resolver antes de incluir:** `addressable` (load path), `faker` (SimpleCov
próprio; além disso 1381 métodos torna-a cara — candidata a amostragem).

**Por procurar:** mais 2-3 gems de cobertura BAIXA (<60%), que são as que dão
sinal de ganho. A busca deve filtrar por cobertura-base, não só por estrelas.
