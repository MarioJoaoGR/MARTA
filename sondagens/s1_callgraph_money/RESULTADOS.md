# Sondagem 1 — Call graph estático vs dinâmico num gem real (`money`)

**Data:** 2026-07-19 · **Veredicto: ✅ viável, com limitações quantificadas (ver conclusões)**

> **UPDATE (mesmo dia): resolver melhorado com os dados desta sondagem — recall 35.9% → 49.6%.**
> Três correções guiadas pelo diagnóstico dos misses:
> 1. **Bug:** métodos em `class << self` eram registados como instância → agora singletons (resolve `Currency.wrap` e afins).
> 2. **Colaboradores em ivar/getter** (o padrão dominante, ex.: `bank.exchange_with`): duck-typing por interface — os métodos invocados no colaborador em toda a classe → `candidates()` via MRO (cap de 5 candidatos; multi-alvo = polimorfismo).
> 3. **`self.class.new`** → `Owner#initialize`.
>
> Nova medição: estático 231 arestas (getter:20, selfclass:5, ivar:1), both=123, dynamic_only=125, **recall 49.6%**. Nota operacional: o `cg_cache` é keyed só pelo hash do source — depois de mudar o *resolver* é preciso apagar `.marta_ruby_cache/` manualmente (melhoria futura: incluir versão do resolver na chave).

## Setup
- Alvo: `RubyMoney/money` @ `ed8ed6b6` (2026-06-22), clonado em `sondagens/targets/money` (gitignored; pin registado aqui).
- Toolchain: Ruby 3.4.10 (rbenv), RSpec 3.13, `bundle install` limpo.
- Instrumentos: `marta/ruby_backend/call_graph.py` (estático, Prism), `dyn_call_graph.py` (TracePoint), `compare()`.
- Comandos: ver §Reprodução no fim.

## Resultados — frente estática (não-LLM) do MARTA-Ruby
| Métrica | Valor |
|---|---|
| Ficheiros lib/ | 20 · **0 erros de parse** |
| Métodos-alvo | 150 · classes no índice: 29 (namespaces `Money::Bank::Base` OK) |
| Targets com tipos inferidos (judge) | 41/150 |
| Tempo do discover() completo | 1.4s |
| Suite humana | 499 exemplos, 0 falhas |
| Cobertura da suite humana nos métodos-alvo (harness nosso) | **99.8%** (149/150 métodos a 100%) |

## Resultados — Sondagem 1 (grafo)
Driver dinâmico = a própria suite do gem (499 exemplos ≈ ground truth dos caminhos exercidos; a cobertura de 99.8% torna-a quase-completa).

| Métrica | Valor |
|---|---|
| Arestas estáticas resolvidas | 201 |
| Arestas dinâmicas observadas | 248 |
| Interseção (both) | 89 |
| **Recall do estático vs arestas exercidas** | **89/248 = 35.9%** |
| static_only | 112 |
| dynamic_only | 159 |

### Leitura (importante para não sobre-interpretar)
- **`static_only` (112) NÃO são todos falsos positivos:** o TracePoint não vê métodos C-level — **todas as arestas para `attr_reader`/`attr_accessor`** (que o estático apanha de propósito) ficam invisíveis ao dinâmico. Com 99.8% de cobertura, pouco resta por "não exercido"; o grosso é attr-edges + resolução imperfeita.
- **`dynamic_only` (159) = os padrões que o estático não resolve**, e são os clássicos de Ruby:
  1. **Dispatch por colaborador em ivar** (dominante): `Money#exchange_to → @bank.exchange_with` (o bank é configurado em runtime); `Money#decimal_mark → LocaleBackend::*#lookup` (registry).
  2. **`self.class.new`**: `Money#dup_with → Money#initialize`.
  3. Polimorfismo real (vários alvos para o mesmo call site: `SingleCurrency` E `VariableExchange`).
- Em Python, o PyCG tem limitações da mesma família — isto não invalida a abordagem; **quantifica-a** (material direto para o paper: primeira medição estático-vs-dinâmico de call graph em Ruby neste contexto).

## Percalços encontrados (e corrigidos)
1. `coverage_runner.run_line_coverage` e `dyn_call_graph.run_dynamic` partiam-se com `cwd` **relativo** (o filtro de caminhos compara absolutos; os testes usavam sempre tmp_path absoluto e nunca o apanharam). Fix: `os.path.abspath(cwd)` em ambos.

## Recomendações
- **Melhoria com maior alavanca no estático:** resolver receivers `@ivar` via atribuições vistas no `initialize` (ex.: `@bank = Bank::VariableExchange.new` ⇒ `@bank.x → VariableExchange#x`). Ataca o padrão dominante do `dynamic_only`.
- Investigar por que `Currency.wrap` (const+singleton) escapou ao estático (candidato a bug de resolução).
- Corpus: `money` é ótima para engenharia mas tem cobertura humana ~100% — incluir gems com cobertura mais baixa para a ferramenta ter margem de demonstração.

## Reprodução
```bash
git clone https://github.com/RubyMoney/money sondagens/targets/money && cd $_ && git checkout ed8ed6b6
bundle install && bundle exec rspec                      # 499 examples, 0 failures
# frente estática + cobertura humana + comparação: ver comandos python inline
# (RubyProject.discover; coverage_runner.run_line_coverage('lib', ['spec'], ...);
#  dyn_call_graph.run_dynamic('lib', 'marta_driver.rb', ...); compare(static, dyn))
# driver dinâmico: marta_driver.rb = RSpec::Core::Runner.run(["spec"], $stderr, $stderr)
```
