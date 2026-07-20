# MARTA-Ruby — melhorias identificadas (não bloqueantes)

*Registado a 2026-07-19, após o smoke test com LLM na gem `money`. A ferramenta
está funcional; nada aqui é bug. Decisão tomada: **congelar** e melhorar depois
com dados do benchmark, porque nesta sessão "melhorar guiado por dados" bateu
sempre "melhorar por intuição" (ver sondagem 1: recall 36%→50%).*

## Por ordem de ROI

### 1. Targeting de *branches* no loop de cobertura
Hoje o loop sintetiza e mira apenas **linhas** em falta. O módulo `Coverage` do
Ruby já devolve `:branches` (o `marta_coverage.rb` até já as pede) — está a ser
deitado fora. A MARTA Python usa `coverage.py --branch`.
- **Valor:** alto (branch coverage é métrica de avaliação nos papers).
- **Esforço:** médio (sintetizar branches por método + formato no prompt).
- **Onde:** `coverage_runner.synthesize`, `MethodCoverage`, `generate_rounds`.

### 2. Guard de contexto para classes grandes
`MethodTarget.context_source` envia a **classe inteira** ao LLM. Na `money`, a
classe `Money` tem centenas de linhas → prompts enormes (contribuiu para os 56k
tokens do smoke de 3 métodos) e risco de estourar a janela em classes maiores.
- **Valor:** alto em projetos reais (custo + falhas por truncatura).
- **Esforço:** baixo-médio (selecionar `initialize` + método-alvo + assinaturas
  dos restantes, em vez do corpo todo; truncar com marcador).
- **Onde:** `project.MethodTarget.context_source`.

### 3. Paralelismo na geração
O nosso `generate_rounds` é **sequencial**; a MARTA Python usa `asyncio.gather`
sobre as funções. Irrelevante localmente, relevante no Deucalion com 150+
métodos por projeto.
- **Valor:** médio (tempo de wall-clock nas runs grandes).
- **Esforço:** baixo (gather + semáforo para não afogar o servidor LLM).
- **Onde:** `project.generate_all` / `generate_rounds`.

### 4. Inferência de tipos de retorno no call graph
Subiria o recall acima dos ~50% (casos como `Money.default_bank.exchange_with`,
onde é preciso saber o tipo devolvido para resolver a chamada seguinte).
- **Valor:** médio. **Esforço:** alto (é um projeto em si). Retornos decrescentes.

### 5. Apurar a *avaliação* do grafo (não a ferramenta)
- `:c_call` no `marta_tracegraph.rb` → elimina a cegueira do dinâmico aos
  métodos C-level (`attr_*`), reduzindo o confound nas `static_only`.
- Auditoria manual amostrada (~30 arestas `static_only`) → permite reportar
  **precisão**, não só recall. Ver `sondagens/s1_callgraph_money/RESULTADOS.md`.

## Já feitas nesta sessão (para memória)
- Fix `cwd` relativo (coverage + tracegraph) — teria rebentado no Deucalion.
- Resolver do grafo: `class << self`, colaboradores ivar/getter, `self.class.new`
  → recall 35.9% → 49.6%.
- Separação `marta_specs/` + vacina RSpec (`-O /dev/null`) + `cg_cache` keyed
  por `RESOLVER_VERSION`.
