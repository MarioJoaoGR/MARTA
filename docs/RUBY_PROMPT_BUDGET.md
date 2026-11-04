# Orçamento do pedido completo — MARTA Ruby

Implementado em 2026-11-04, depois de `94c9269ac`. Esta política aplica-se a novas
execuções do backend Ruby; não migra nem reclassifica experiências dos papers.

## Contrato

Antes de cada pedido de análise, Planner ou Developer, conta-se o pedido completo:
mensagem de sistema e de utilizador, incluindo instruções, source, sumários,
README, contexto recuperado, feedback de cobertura, plano, diagnóstico e teste
anterior quando presentes. O limite de entrada é:

```
entrada disponível = janela declarada − reserva de saída − margem
```

Não se aumenta a janela, o limite de saída, as tentativas ou as rondas. A reserva
inclui todo o limite de completion do cliente, incluindo thinking quando o
servidor o contabiliza nesse limite; não se inventa uma divisão entre raciocínio
e resposta. Reservar saída não garante que o modelo termine o seu raciocínio.

Se o pedido original couber, o texto enviado é o mesmo que antes. Se exceder o
orçamento, só componentes explicitamente opcionais podem ser reduzidos. A própria
nota de redução entra na contagem. As listas conservam entradas completas; a
prosa pode conservar um prefixo; código auxiliar passa inteiro para um fallback
explícito, sem ser cortado a meio de uma instrução.

O método-alvo completo, o plano efetivo original, o teste anterior completo e o
núcleo do diagnóstico (tipo, tentativa, estado e contagens observadas) são
obrigatórios quando presentes. As instruções e o contexto de carregamento também
permanecem. Se isso não couber, `PromptBudgetExceeded` interrompe o fluxo **antes
do pedido correspondente**. Não é uma resposta vazia do modelo, uma suite válida
nem um resultado `no_tests`. Pedidos anteriores da mesma tarefa podem já ter sido
executados. Os mecanismos existentes de arquivo/checkpoint conservam a evidência;
não se introduz uma repetição automática para tentar obter uma resposta melhor.

## Contagem e limites da garantia

Há dois modos, identificados explicitamente na proveniência e na telemetria:

1. **Tokenizer local configurado**: `MARTA_TOKENIZER_PATH` aponta para uma pasta
   já existente. Usa `AutoTokenizer.from_pretrained(..., local_files_only=True,
   trust_remote_code=False)` e `apply_chat_template(..., tokenize=True,
   add_generation_prompt=True)`. Inclui os tokens de controlo do template local;
   passa `enable_thinking` quando o cliente declara esse modo. Falhas do tokenizer
   configurado são erros, sem download nem fallback silencioso.
2. **Estimativa por omissão**: bytes UTF-8 de sistema + utilizador + 64 unidades
   para enquadramento. É deliberadamente conservadora em usos comuns, mas **não é
   uma contagem exata nem um limite matemático para qualquer tokenizer/template**.
   Pode reduzir ou recusar pedidos que caberiam no modelo real. Não se apresenta
   esta estimativa como tokens medidos pelo servidor.

A exatidão do primeiro modo é relativa ao tokenizer e template fornecidos.
Cabe à configuração corresponder ao modelo, versão e template reais do servidor.
Não há descoberta/atestação da janela física nem do template via API. O estado
atual do projeto não tem um tokenizer LLM correspondente configurado; não foi
instalado nem descarregado nenhum nesta entrega.

Para exigir contagem local, definir `MARTA_REQUIRE_EXACT_TOKENS=1`: a ausência de
um contador exato configurado interrompe a execução. Um callback avançado pode
expor `prompt_budget=PromptBudget(...)` com um contador próprio e uma `identity`
estável que identifique implementação, template e assets. Esse contrato é
externo; a MARTA não consegue verificar uma alegação de exatidão de um callback.
As reservas/janelas explicitamente declaradas e o cap exposto pelo cliente não
podem ser contrariados pelo orçamento injetado.

Referências do mecanismo: [templates de chat do Transformers](https://huggingface.co/docs/transformers/main/en/chat_templating)
e [API pública do Ollama](https://docs.ollama.com/api/introduction). Não se assume
um endpoint público `/api/tokenize` nem se usa um tokenizer de outra família como
se fosse exato para Qwen/DeepSeek.

## Configuração

| Parâmetro | Comportamento |
|---|---|
| `MARTA_CONTEXT_TOKENS` | Janela declarada para o cliente Ruby |
| `OLLAMA_CTX`, `OLLAMA_CONTEXT_LENGTH` | Outras declarações existentes; usa-se a menor janela positiva declarada |
| Sem janela declarada | Política local de 16 384; marcada `client-default-unverified-server`, não descoberta do servidor |
| `client.max_tokens` / `LLM_MAX_TOKENS` | Reserva pelo menos o cap efetivo exposto pelo cliente; callbacks opacos usam a declaração do ambiente ou o default existente 2 048 |
| `MARTA_OUTPUT_RESERVE` | Reserva positiva adicional; não pode reduzir o cap do cliente |
| `MARTA_CONTEXT_MARGIN` | Margem não negativa; por omissão 256 |
| `MARTA_TOKENIZER_PATH` | Pasta local do tokenizer de chat correspondente; nunca faz download |
| `MARTA_REQUIRE_EXACT_TOKENS=1` | Recusa o modo de estimativa |

Caps explicitamente ilimitados, nulos ou inválidos são recusados: não permitem
reservar uma saída finita. O orçamento não altera `client.max_tokens`. Callbacks
opacos têm de declarar os seus limites reais para oferecer uma garantia útil.

## Prioridades de redução

A ordem indicada é da primeira informação a reduzir para a última:

| Fase | Contexto opcional |
|---|---|
| `done_what` | Lista de sumários de callees; depois contexto auxiliar do source |
| `what_todo` README | Overview; depois contexto auxiliar do source |
| `what_todo` propagado | Intenção do caller; depois contexto auxiliar do source |
| Sumário final | Prosa de `done_what` e `what_todo`; depois contexto auxiliar do source |
| Overview do README | Prosa do documento; conserva um prefixo mínimo de 256 caracteres |
| Sumário de classe | Stub/assinaturas completos ou fallback ao cabeçalho da classe/módulo |
| Planner | Related; sumário; contexto auxiliar do source |
| Developer inicial | Contexto auxiliar do source |
| Developer reparação | Ajuda recuperada; listas de exemplos de validação anterior/atual; detalhe extenso do erro; contexto auxiliar do source |

Os overviews, intenção do caller e perspetivas do sumário final conservam um
mínimo de 128 caracteres quando disponíveis. O detalhe do erro pode passar para
início/fim com marcador de omissão, além da condensação histórica do builder de
erros. As contagens e classes de falha não são recalculadas a partir da lista
reduzida. Plano e teste anterior não são encurtados para acomodar esse detalhe.

São prioridades determinísticas de engenharia, **não rankings de relevância
aprendidos**. A lista de callees ainda segue a ordem existente; uma entrada longa
pode impedir outras posteriores de caber. Continua por estudar seleção por
relevância/evidência e confiança nas arestas. A síntese da segunda passagem
continua a ser um pedido ao modelo, não concatenação substitutiva; quando o
orçamento força a remoção de todos os callees, essa síntese recebe menos contexto,
explicitamente sinalizado. Não se promete full context ilimitado.

O limite local anterior de caracteres para construir a vista do source continua
independente. Agora a vista expõe separadamente o código focal obrigatório. O
orçamento global pode remover o bloco auxiliar inteiro, mas nunca o código focal.
A qualidade dos sumários de classe/top-40 e a abstenção do judge continuam A10.

## Evidência, cache e retoma

Cada decisão emite `tipo=prompt_budget`, fase/contexto do recorder, política,
contador, janela, reserva, margem, contagens original/selecionada, `fits`, tamanhos
dos componentes reduzidos e hashes dos dois pedidos. Estas unidades de orçamento
**não** substituem os tokens de usage devolvidos pelo modelo nem entram nas suas
métricas como tokens observados. Pedidos recusados não contam como chamadas LLM.

`ANALYSIS_SCHEMA=7` e a proveniência incluem a política e a configuração efetiva,
os hashes da implementação e dos assets locais conhecidos do tokenizer (incluindo
template, vocabulário e modelos SentencePiece quando presentes). A receita da
geração também inclui esse orçamento. Alterar janela/reserva/margem/contador ou
os assets identificados invalida a reutilização incompatível. Tokenizers externos
ou customizados exigem identificação externa completa. A cache de carregamento
local usa a fingerprint dos assets; não se recarrega o tokenizer a cada contagem.

Uma análise recusada fica como arquivo falhado, sem publicar bundle incompleto ou
substituir uma cache válida anterior. O arquivo independente da análise mantém as
suas regras; as rondas de geração mantêm o seu contrato de validação/checkpoint.
Experiências históricas conservam código, manifests e métricas congelados. Não se
faz migração automática das referências XRepoTest para esta política.

## Validação

`test_prompt_budget.py` verifica limites incluindo system/output/margem,
prioridades e marcador de omissão, modo estrito, carregamento só local,
preservação do método/plano/teste, textos inalterados quando cabem, falha antes do
pedido e invalidação/preservação da cache. Os contadores de fixtures e respostas
scriptadas não chamam LLMs nem estimam ganhos de qualidade no corpus. Correm ainda
as suites existentes de análise, retoma, Ruby/RSpec, RAG e adapters de benchmark.

Validação final: 793 testes locais aprovados (3 ignorados) e 12 testes no
container existente, sem rede. Total: **805 aprovados**. Não houve inferência,
instalação de dependências ou alteração de resultados históricos.
