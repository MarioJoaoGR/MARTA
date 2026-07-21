# MARTA-Ruby — ponto de situação

*Resumo para reunião. Estado a 2026-07-21.*

---

## 1. A ferramenta: feita e a funcionar

Portámos a MARTA para **Ruby**. É a mesma ferramenta que já conhecem — mesma
arquitetura, mesmo desenho experimental — só que gera **RSpec** em vez de Pytest.

O que mudou é só a "camada de linguagem":

| MARTA Python | MARTA Ruby |
|---|---|
| `ast` (parser) | Prism (parser oficial do Ruby) |
| PyCG (call graph) | analisador estático próprio (não existia equivalente) |
| Pytest | RSpec |
| coverage.py | módulo `Coverage` do Ruby |

Tudo o resto — as duas fases, os agentes Planner/Dev, o self-healing, o
salvamento, o loop guiado por cobertura, as caches — é igual, e foi validado
peça a peça (**92 testes unitários**).

**Nota:** a MARTA Python **não foi tocada**. Continua exatamente como está, a
correr a experiência no Deucalion. As duas versões coexistem sem interferência.

### Já foi testada?
Sim, minimamente: corre de ponta a ponta num projeto real (o `fpm`, um dos repos
Ruby do SWE-bench) — gera testes, executa-os, mede cobertura. Ainda **não**
corremos em escala: estamos à espera de (a) a experiência Python terminar no
Deucalion e (b) decidir o modelo (DeepSeek 16B vs 236B).

---

## 2. O problema que encontrámos: para Ruby não existe nada

Fizemos uma pesquisa sistemática e confirmámos: **não existe nenhum benchmark de
geração de testes para Ruby**. O trabalho anterior resume-se a:
- um gerador de 2011, pré-LLM, descontinuado;
- um paper de 2025 que gera "esqueletos" de teste para *uma* classe, sem execução.

Ou seja: para avaliar a ferramenta, **tivemos de construir o dataset**. Isso é
trabalho extra, mas é também uma contribuição publicável por si só.

---

## 3. Os dados: três fontes, dois objetivos diferentes

| Fonte | Para que serve | Estado |
|---|---|---|
| **Corpus de gems** (construído por nós) | Medir **qualidade** dos testes gerados (cobertura, mutação) | ✅ construído |
| **SWE-bench Multilingual** | Medir **deteção de bugs reais** (versão com bug vs corrigida) | ✅ analisado |
| **Defects4Ruby** | Idem — mais bugs reais | ⏳ por explorar |

- **SWE-bench Multilingual**: dataset público com bugs reais. Tem **44 tarefas em
  6 repositórios Ruby**. Cada tarefa traz a versão com bug e a corrigida — serve
  para perguntar *"os testes gerados apanham o bug?"*.
- **Defects4Ruby**: dataset de 2025 com a mesma finalidade. Já identificado;
  ainda não o reproduzimos.
- Estes dois medem **deteção de bugs**. O corpus de gems mede **cobertura**. São
  complementares, não alternativas.

---

## 4. O benchmark que construímos

Não escolhemos os projetos "a olho" — seguimos um processo reprodutível, para a
seleção ser defensável:

```
lista curada da comunidade (awesome-ruby)
   └─ filtro de popularidade (≥100M downloads)          → 125 projetos
      └─ análise estática automática                     → 110 (sem erros)
         └─ filtros (instalação pesada, código gerado)   →  92 elegíveis
            └─ seleção por DIVERSIDADE de código          →  12 finais
```

**Porquê "diversidade de código"**: queremos projetos que testem partes
diferentes da ferramenta. Os 12 escolhidos vão de 20 a 1771 métodos, cobrem 11
domínios distintos, e incluem tanto código simples como código com muita
metaprogramação (o caso mais difícil para a análise estática).

Todos são gems muito usadas (entre as posições #6 e #399 do ecossistema, todas
com +129 milhões de downloads), com a versão fixada para reprodutibilidade.

Tudo isto está documentado e é re-executável por qualquer pessoa (scripts +
metodologia escritos).

---

## 5. Próximos passos

1. Esperar que a experiência Python termine no Deucalion *(em curso)*
2. Decidir o modelo (16B vs 236B)
3. Correr a MARTA-Ruby no benchmark (o harness para o Deucalion já está pronto e
   testado — retoma sozinho quando o tempo de execução do cluster acaba)
4. Comparar com as alternativas existentes e explorar o Defects4Ruby

## 6. Publicações possíveis

- **Paper do benchmark** (curto): o corpus + a ferramenta de avaliação — é o
  primeiro para Ruby.
- **Paper da ferramenta**: a MARTA-Ruby avaliada nesse benchmark, mais a
  discussão da comparação Python↔Ruby.
