# Revisão total pré-Deucalion — ferramenta + benchmark

*Auditoria de prontidão feita a 2026-07-22, enquanto a experiência Python corre
no cluster. Cada item foi VERIFICADO (comando corrido), não assumido.
Veredicto no fim.*

---

## A. Ferramenta (MARTA-Ruby) — ✅ pronta

| Item | Estado | Verificação |
|---|---|---|
| Suite de testes | ✅ 92 passed | `pytest marta/ruby_backend/tests/` |
| Paridade com o Python (contexto, prompts, loop, caches, salvamento) | ✅ | `marta/ruby_backend/PARIDADE.md` |
| E2E em projeto real (fpm/SWE-bench): gerar→correr→medir | ✅ | smoke 2026-07-21 |
| Resume/caches (job encadeado retoma e melhora) | ✅ | run retomado: 22→8 chamadas LLM, 1→3 specs |
| CLI ↔ harness (args `--num/--limit/--output_dir/...`) | ✅ | `--help` conferido |
| Bugs de projeto real (contexto, GEM_PATH, namespace compacto) | ✅ corrigidos | commits `dbda588e`, `f8d0c703` |

**Riscos conhecidos, aceites e documentados:** geração sequencial (sem
paralelismo — custo de walltime, mitigado pelo auto-chain); branch coverage
recolhida mas não usada no targeting; `MELHORIAS_PENDENTES.md`.

## B. Baselines — 🔴 era o maior buraco; agora mapeado

**Correção de registo:** a ferramenta externa é o **cover-agent / Qodo Cover**,
implementação open-source do **TestGen-LLM da Meta** (não Google). RuTeG (SBST
2011) confirmado morto — o "vazio SBST" argumenta-se no paper.

### Sondagem 2 (cover-agent) — FEITA HOJE, com E2E real
- ✅ **Instala** (source do GitHub; não está no PyPI) e o CLI funciona.
- ✅ **Tem suporte Ruby** (exemplo `ruby_sinatra` oficial) e fala com o nosso
  **ollama** via litellm (`--model ollama/... --api-base ...`).
- ✅ **E2E corrido no exemplo deles com deepseek-16b**: o pipeline mecânico
  funciona (lê cobertura-base 37.25%, gera candidatos, valida, faz rollback dos
  que não aumentam cobertura). Neste run curto (2 iterações), **nenhum candidato
  aumentou cobertura** → 37.25% final.
- 📋 **Requisitos práticos mapeados** (importam para o desenho da comparação):
  1. Trabalha **por ficheiro** (`--source-file-path`), não por projeto → precisamos
     de um adaptador/loop.
  2. **Estende uma suite existente** — não gera do zero → há que dar-lhe um
     *seed spec* mínimo por ficheiro (decisão metodológica a registar).
  3. Exige **relatório cobertura em XML** → `simplecov` + `simplecov-cobertura`
     configurados no alvo → só em **cópias sandbox** dos projetos (a regra
     "não alterar os projetos" mantém-se nos originais).
  4. Último commit upstream: 2025-06 (parado há ~1 ano — citar a versão).
- ⚠️ **Fica em aberto:** eficácia real em gems nossas (o run de 2 iterações não
  chega para julgar) — medir no benchmark é precisamente o objetivo.

### Single-prompt baseline — ❌ DESCARTADO por decisão do utilizador (2026-07-22)
**Não construímos baselines nossas.** A comparação é contra ferramentas
EXISTENTES apenas; a ausência delas é o claim de pioneirismo, não um buraco a
preencher por nós. (Removido do plano; o `single-prompt` referido no plano
original fica sem efeito.)

### Sondagem 3 (mutant) — ✅ FEITA (2026-07-22)
Corrido de verdade na `money`: 12 mutações em `Money#hash`, 11 mortas,
**mutation score 91.66%**. `--usage opensource` aceite sem conta. Fricções
mapeadas (locale UTF-8 obrigatório; `RUBYOPT -I` para a integração rspec fora
de bundle; binário é `mutant-ruby`). Ver `sondagens/s3_mutant/RESULTADOS.md`.
Pendente só: confirmar no nó offline do Deucalion.

## C. Benchmark/dados

| Item | Estado |
|---|---|
| Fase 1 (SWE-bench): 6 repos, commits reais fixados | ✅ `ruby_projects.json` |
| `prepare_ruby_projects.py` (offline-ready, testado em faker+fpm) | ✅ |
| Harness (state/resume/SIGTERM/medição tool-only) | ✅ validado local |
| Job SLURM (auto-chain, OOM-retry, MODEL parametrizável) | ✅ escrito, ⚠️ nunca submetido |
| Corpus 12 gems (Fase 2) | ✅ selecionado/pinado; ⚠️ `prepare` ainda só lê a config da Fase 1 — generalizar antes da Fase 2 |
| Runs independentes (N runs + Wilcoxon) | ✅ **corrigido hoje**: `--fresh-specs` (specs limpos por run; caches de análise ficam, como no Python) |
| Defects4Ruby | ❌ por reproduzir (linha de bugs reais; não bloqueia a Fase 1) |
| Comparação vs suite humana | 🟡 medição existe (`diagnose --coverage`) mas fora do harness — decidir se entra na Fase 1 |

## D. Pré-flight Deucalion (a fazer no login node, por ordem)

1. **Ruby 3.4 no cluster** — 🔴 o `.sif` não tem Ruby; o job espera
   `RUBY_ROOT=/projects/.../ruby-3.4.10`. Compilar via ruby-build no login node
   (ou juntar ao .sif) + `gem install rspec` nesse Ruby. **Sem isto nada corre.**
2. `git pull` do repo no cluster (o harness/benchmark/ tem de lá estar).
3. `python -m benchmark.prepare_ruby_projects --out /projects/.../ruby_projects`
   (rede: clones + deps offline).
4. Smoke de 1 job: `PROJECTS=fpm LIMIT=3 sbatch deucalion/run_ruby_benchmark.sh`
   — valida container+ollama+ruby+harness com custo mínimo, ANTES do run grande.
5. Decisão do **modelo** (16B vs 236B — aguarda o resultado da experiência Python).
6. Só depois: run completo da Fase 1.

## Veredicto

**A ferramenta e o harness estão prontos.** Falta: (i) infra no cluster (Ruby
no Deucalion — obrigatório, item D.1) e (ii) decidir o protocolo do cover-agent
(seed specs + sandbox + nº iterações). **Comparação fechada por decisão:** MARTA
vs cover-agent (única ferramenta externa viável — Keploy é record-replay de
APIs, não gera testes de bibliotecas; Diffblue=Java, CoverUp=Python,
TestPilot=JS) vs suites humanas como referência. Não se constrói baseline
nossa. A Fase 1 arranca assim que o modelo for decidido **e** o D.1 estiver
feito.
