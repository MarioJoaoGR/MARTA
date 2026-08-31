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

### 2. A segunda passagem dos sumários pode não compensar sempre
Hoje, todo o método que chame outros do projeto é resumido **duas vezes**: a
segunda com os sumários dos chamados. Custa uma chamada ao modelo por método, e
**nunca foi medido o que rende**.

A alternativa levantada pelo utilizador: em vez de pedir ao modelo que sintetize,
**anexar** os sumários dos chamados numa fase offline, sem custo nenhum.

Não é equivalente, e por três razões que convém não perder:
1. A síntese reescreve o sumário do ponto de vista de quem chama; a concatenação
   deixa dois textos lado a lado, cada um na sua perspetiva.
2. **O sumário final é indexado no ChromaDB** (`build_rag`) e serve a busca por
   semelhança. Uma colagem embebe-se mal: o vetor fica uma mistura de assuntos e
   a busca passa a devolver métodos parecidos com os vizinhos.
3. Quinze chamados a ~3000 caracteres não cabem num sumário.

**O teste que falta:** correr o mesmo projeto com síntese e com concatenação, e
comparar os specs gerados e a cobertura. Provavelmente a resposta é mista, e o
desenho certo é híbrido — anexar quando são poucos e curtos, sintetizar quando
são muitos. Isso resolveria ao mesmo tempo o problema do travão (ponto 1).

### 3. A cache da análise não conhece a versão do contexto
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

### 4. O `--no_cache` recalcula mas não grava
A gravação está dentro do `if use_cache`, portanto com `--no_cache` os sumários
são recalculados, usados na geração, e deitados fora. Fica-se sem registo do que
o modelo produziu naquela execução — foi o que impediu comparar as duas runs da
`formatador`.

- **Correção:** gravar sempre; ou, se se quiser preservar o anterior, gravar num
  ficheiro à parte quando é `--no_cache`.
- **Onde:** `project.analyze_summaries`, o `if use_cache` final.

### 5. Paralelismo na geração
O `generate_rounds` é sequencial; a MARTA Python usa `asyncio.gather` sobre as
funções. Irrelevante localmente, relevante no Deucalion com 150+ métodos por
projeto.
- **Esforço:** baixo (gather + semáforo para não afogar o servidor LLM).
- **Onde:** `project.generate_all` / `generate_rounds`.

### 6. Ponderar as arestas pela certeza da resolução
Uma chamada sobre uma constante é certa; sobre um parâmetro é palpite; e hoje as
duas arestas valem o mesmo. A forma que resolveu cada aresta **já fica gravada**
no campo `kind`, mas nada a consulta.
- **Esforço:** baixo para gravar o peso, médio para o usar bem.

### 7. Inferência de tipos de retorno no grafo
Subiria o recall acima dos 50% (casos como `Money.default_bank.exchange_with`,
onde é preciso saber o tipo devolvido para resolver a chamada seguinte). São
também a maior parte das chamadas classificadas como `other`.
- **Esforço:** alto, é um projeto em si. Retornos decrescentes.

### 8. Apurar a avaliação do grafo (não a ferramenta)
- Ligar `:c_call` no `marta_tracegraph.rb` → tira a cegueira do grafo dinâmico
  aos métodos implementados em C (`attr_*`), que hoje inflaciona as `static_only`.
- Auditar uma amostra (~30 arestas `static_only`) → permite reportar **precisão**
  e não só recall. Ver `sondagens/s1_callgraph_money/RESULTADOS.md`.

### 9. A passagem 2 dos sumários depende da ordem de iteração
No ciclo da segunda passagem, o `t.done_what` é **substituído à medida que o
ciclo avança**. Um método processado no fim vai buscar aos vizinhos que já
passaram por lá a versão **já enriquecida**, e não a original da passagem 1.

Ou seja, a profundidade do enriquecimento depende da ordem por que os métodos
aparecem na lista: uns recebem informação de primeira mão, outros recebem
informação que já passou por duas digestões.

Não se manifesta como erro e pode até ser benéfico nalguns casos. Mas torna o
resultado dependente da ordem de iteração, que é o tipo de coisa que estraga a
reprodutibilidade sem dar sinal.

- **Correção:** guardar os `done_what` da passagem 1 numa cópia e ler sempre
  dessa, para todos verem o mesmo estado.
- **Onde:** `project.analyze_summaries`, o ciclo da passagem 2.

### 10. O RAG é consultado a cada ronda e devolve sempre o mesmo
O `_related_for(t)` é chamado dentro do ciclo das rondas (`project.py:599`). A
pergunta é o `t.summary`, que **não muda entre rondas** — só o `coverage_info`
muda. Portanto na ronda 2 refaz-se uma busca que dá exatamente o mesmo resultado
da ronda 1, e o mesmo na 3.

É desperdício pequeno (uma multiplicação de matriz por método por ronda), mas
convém estar registado: se perguntarem se o RAG é consultado a cada ronda, a
resposta é que sim, e sempre com a mesma resposta.

- **Correção:** calcular os relacionados uma vez por método, antes do ciclo das
  rondas, e reutilizar.
- **Onde:** `project.generate_rounds`, o argumento `related=`.

### 11. Sumários de classe cortados demais, e sem validação a jusante
Duas coisas ligadas, ambas no caminho do *judge semântico*.

**O que se envia.** À classe manda-se só o stub (cabeçalho + `body_statements`)
e as assinaturas, nunca os corpos. A regra existe porque a classe inteira
estourava a janela (`fpm/Deb`: 43k chars), mas aplica-se a **todas**: numa
classe de dois métodos cabia tudo, e o resultado é um sumário inútil. Medido na
demo: o modelo respondeu *"incomplete implementation ... challenging to provide
a detailed summary"* para as duas classes.

- **Correção:** enviar os corpos quando cabem no `MAX_CONTEXT_CHARS`, e cair
  nas assinaturas só quando não cabem.
- **Onde:** `project.analyze_summaries`, a construção do `class_src` (:425).

**O que se faz com o resultado.** O `_augment_judge_semantic` pergunta à matriz
das classes qual a mais parecida e escreve-a no judge, **sem limiar nenhum de
semelhança**. A busca por cosseno devolve sempre alguma coisa: se nenhuma classe
servir, devolve a menos má, e ela entra no prompt com o mesmo peso de uma
acertada.

Repare-se no contraste: a parte estrutural tem o travão dos 5 candidatos, que
prefere não dizer nada a dizer demais. Aqui não há equivalente.

- **Correção:** um limiar mínimo de cosseno, abaixo do qual não se acrescenta
  linha nenhuma.
- **Onde:** `project._augment_judge_semantic` (:472), e `rag.query` teria de
  devolver a pontuação, que hoje deita fora.

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
