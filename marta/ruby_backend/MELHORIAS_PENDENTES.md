# MARTA-Ruby — melhorias identificadas (não bloqueantes)

*Nada aqui é bug: a ferramenta funciona. A regra que se tem confirmado é
melhorar guiado por dados e não por intuição — foi assim que o resolver do grafo
subiu de 35,9% para 49,6% (sondagem 1) e foi assim que se encontrou a
divergência do contexto (ver `PARIDADE.md`).*

Última revisão: 2026-08-20.

---

## Por ordem de risco

### 1. O contexto dos métodos chamados não tem travão nenhum
Na segunda passagem dos sumários, o contexto leva o `done_what` **de todos** os
métodos que o alvo chama, sem limite de quantidade nem de tamanho. O
`MAX_CONTEXT_CHARS` protege o código enviado, mas não este caminho.

Medido: um `done_what` tem mediana de **2960 caracteres** (`formatador`), e na
`money` o `Currency#inspect` chama **15 métodos**. Isso dá cerca de **44 000
caracteres** de contexto num único pedido, sete vezes o limite que impomos ao
código.

O caso mau é raro (na `money`, mediana de 2 chamadas por método e só 4 métodos
acima de 5), mas quando acontece afoga o método-alvo — o mesmo mecanismo que fez
o sumarizador da `formatador` descrever a classe em vez do método.

- **Correção:** limitar o número de chamados que entram, à imagem do travão dos
  5 candidatos que já existe no resolver, e truncar cada sumário a 300-400
  caracteres ao entrar no contexto de outro método.
- **Onde:** `project.analyze_summaries` (a lista `called`), `summaries.analyze_done_what`.

### 2. A cache da análise não conhece a versão do contexto
A chave é `hash do código + modelo`. Não inclui nada que identifique a forma como
o contexto é construído, portanto **mexer num prompt não invalida a cache**: um
projeto já analisado continua a servir sumários antigos.

É exatamente o problema que já se pagou uma vez no grafo, e que ali foi resolvido
com o `RESOLVER_VERSION` na chave. Aconteceu de novo a 18/08: a correção da
separação do contexto ficou invisível na `formatador`.

- **Correção:** uma constante `CONTEXT_VERSION` na chave, incrementada sempre que
  se mexe num prompt ou na construção do contexto.
- **Contorno atual:** apagar `.marta_ruby_cache/` antes de correr.
- **Onde:** `project.analyze_summaries`, `cache.py`.

### 3. O `--no_cache` recalcula mas não grava
A gravação está dentro do `if use_cache`, portanto com `--no_cache` os sumários
são recalculados, usados na geração, e deitados fora. Fica-se sem registo do que
o modelo produziu naquela execução — foi o que impediu comparar as duas runs da
`formatador`.

- **Correção:** gravar sempre; ou, se se quiser preservar o anterior, gravar num
  ficheiro à parte quando é `--no_cache`.
- **Onde:** `project.analyze_summaries`, o `if use_cache` final.

### 4. Paralelismo na geração
O `generate_rounds` é sequencial; a MARTA Python usa `asyncio.gather` sobre as
funções. Irrelevante localmente, relevante no Deucalion com 150+ métodos por
projeto.
- **Esforço:** baixo (gather + semáforo para não afogar o servidor LLM).
- **Onde:** `project.generate_all` / `generate_rounds`.

### 5. Ponderar as arestas pela certeza da resolução
Uma chamada sobre uma constante é certa; sobre um parâmetro é palpite; e hoje as
duas arestas valem o mesmo. A forma que resolveu cada aresta **já fica gravada**
no campo `kind`, mas nada a consulta.
- **Esforço:** baixo para gravar o peso, médio para o usar bem.

### 6. Inferência de tipos de retorno no grafo
Subiria o recall acima dos 50% (casos como `Money.default_bank.exchange_with`,
onde é preciso saber o tipo devolvido para resolver a chamada seguinte). São
também a maior parte das chamadas classificadas como `other`.
- **Esforço:** alto, é um projeto em si. Retornos decrescentes.

### 7. Apurar a avaliação do grafo (não a ferramenta)
- Ligar `:c_call` no `marta_tracegraph.rb` → tira a cegueira do grafo dinâmico
  aos métodos implementados em C (`attr_*`), que hoje inflaciona as `static_only`.
- Auditar uma amostra (~30 arestas `static_only`) → permite reportar **precisão**
  e não só recall. Ver `sondagens/s1_callgraph_money/RESULTADOS.md`.

---

## Já feitas

- **Cobertura de ramos** usada mesmo, e não só recolhida: um método cujas linhas
  correram todas mas com um lado do `if` por tomar deixa de ser dado como
  completo (`2073349e`).
- **Contexto focado**: stub da classe + `initialize` + método-alvo, em vez da
  classe inteira, que estourava a janela na `fpm`.
- **Partes do contexto separadas** por marcadores, como o Python faz (`e1060ecf`).
- **Grafo reaproveita o parse** do `discover()` em vez de reler o projeto: metade
  das chamadas ao parser desaparece (`d9263ca5`).
- Resolver do grafo: `class << self`, colaboradores por ivar e getter,
  `self.class.new` → recall 35,9% para 49,6%.
- `cwd` relativo na cobertura e no tracegraph, que teria rebentado no Deucalion.
- `marta_specs/` separado da suite humana, vacina RSpec (`-O /dev/null`), e
  `cg_cache` indexada por `RESOLVER_VERSION`.
