# Observação dinâmica de accessors — B1

Entrega de 6 de novembro de 2026. Instrumentação opcional para avaliar o grafo;
não é uma nova fase da geração normal.

## Problema e comportamento

O tracer anterior observava apenas `:call/:return`. No exemplo:

```ruby
class Entry
  attr_reader :amount
end
class Wallet
  def apply(entry)
    entry.amount
  end
end
```

`Wallet#apply -> Entry#amount` podia aparecer no grafo estático e ficar invisível
no driver, porque o accessor gera um evento C. A diferença não bastava para
classificar a resolução estática como errada.

O modo opcional observa também `:c_call/:c_return`. O caminho desse evento pode
ser o **local da chamada**, pelo que não serve sozinho para decidir se o método
pertence ao projeto. Para métodos C, consulta a localização da definição exposta
por `UnboundMethod#source_location`; só a aceita quando está dentro da raiz
indicada. Accessors com origem Ruby conhecida entram; operações internas sem
essa origem, como `Integer#to_s`, ficam de fora. Não cobre todos os métodos C
ou extensões nativas sem localização Ruby.

O filtro de diretórios usa uma fronteira de caminho: `src_extra` não pertence a
`src`. O lookup da origem não é memorizado entre chamadas, pois uma redefinição
pode mudar a definição. Herança/mixins e singleton methods conservam o nome do
dono da definição; aliases usam `method_id`, o nome da definição, e não inventam
uma nova definição a partir do nome invocado.

## Uso

```python
from marta.ruby_backend.dyn_call_graph import trace_dynamic, compare

trace = trace_dynamic("lib", "/projeto/driver.rb", cwd="/projeto", include_c=True)
print(trace.metadata)
comparison = compare(static_graph, trace.graph)
```

`run_dynamic(...)` continua a devolver apenas um `CallGraph` e aceita
`include_c=True` como opção keyword. A omissão continua sem eventos C. Para uma
avaliação auditável, preferir `trace_dynamic`, que devolve grafo, metadados e
stderr. O helper também aceita `--include-c` diretamente.

O driver é executado, como já acontecia nesta API. Deve reservar stdout para o
protocolo JSON do helper e dirigir o seu output de diagnóstico a stderr.
Nenhum driver real é executado automaticamente pela MARTA normal.

## Pilhas e significado das relações

Cada thread/fiber tem a sua própria pilha. Entradas/saídas Ruby e C só são
emparelhadas quando coincidem família de evento, dono e método. Um desencontro
limpa a pilha afetada, evitando atribuir chamadas futuras a um frame antigo;
os contadores `unmatched_returns`, `stack_resets` e `remaining_frames` permitem
inspecionar problemas e execuções suspensas.

Frames C externos são transparentes na projeção do grafo: `Class#new` e
iteradores não escondem o caller Ruby. Um método Ruby fora do projeto continua
a ser uma barreira. Esta é uma projeção das relações observadas, não a listagem
de todos os frames da VM. A política fica registada nos metadados.

O bloco de tracing indica explicitamente `target_thread: nil`, para não limitar
a observação à thread que carrega o driver. Este cuidado está descrito na [documentação oficial de TracePoint](https://docs.ruby-lang.org/en/3.4/TracePoint.html#method-i-enable).
As pilhas só ficam vivas durante o processo de diagnóstico; referências a
threads/fibers são conservadas nesse intervalo para manter identidades distintas.

As arestas novas têm `kind="dynamic_c"` e evidência `runtime_observed`. As Ruby
mantêm `kind="dynamic"`. A projeção por par e a comparação existentes continuam
a funcionar. Linhas de call sites não são reconstruídas; mantêm-se a zero.
A omissão de autoarestas recursivas do contrato anterior também se mantém.

## Conclusão, proveniência e limites

O relatório identifica política `ruby-tracepoint-v2`, versão Ruby, eventos,
origem selecionada e estado do driver. Exceções e `SystemExit` preservam as
arestas recolhidas, mas ficam com `completed=False`, em vez de parecerem uma
execução normalmente concluída. `completed=True` significa que o driver retornou;
não prova cobertura completa nem ausência de limitações do instrumento.

O wrapper regista hash do helper e se permaneceu igual, além dos hashes do driver
antes/depois. Não são um manifesto de todas as dependências executadas. Código
dinâmico, alterações concorrentes de métodos e diferenças entre VMs/Ruby podem
limitar a correspondência entre nomes observados e definições estáticas.

A API de comparação não chama uma diferença `static_only` de falso positivo.
Essa diferença pode ser caminho não exercitado, método invisível ao instrumento
ou resolução estática errada. É preciso auditar as arestas e repetir em várias
gems para estimar precisão e alcance. A sondagem histórica não foi recalculada
nem reclassificada com este novo protocolo.

Não há modelo, embedding ou pacote novo. O modo C acrescenta eventos, lookups
de origem e memória de pilhas apenas quando o diagnóstico é pedido; pode tornar
o driver mais lento. Não se promete overhead nulo ou aceleração global.

## Verificação

Os controlos cobrem accessors, writers, herança/mixins, singletons, aliases,
redefinições, origem externa, fronteira de diretórios, chamadas nativas aninhadas,
recursão, exceções, suspensão de fibers, threads e drivers parciais. São fixtures
sintéticas, sem inferência LLM nem alteração do benchmark.

**1107 testes locais aprovados**, seis ignorados no host; **16 aprovados no
contentor existente**, incluindo quatro daqueles ignorados: **1123 aprovados;
dois permanecem ignorados**. Três controlos adicionais de compatibilidade do
tracer passaram no Ruby 3.2.11 do contentor; o host usa Ruby 3.4.10. Sem downloads
ou instalações.
