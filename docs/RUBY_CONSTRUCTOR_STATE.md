# A7, segunda etapa — campos construídos e getters simples

Entrega de 6 de novembro de 2026. Complementa as
[fábricas diretas](RUBY_RETURN_TYPES.md); não é um sistema global de tipos Ruby.

## Comportamento

```ruby
class Widget
  def run; :ok; end
end

class Box
  attr_reader :widget  # Também aceita: def widget; @widget; end

  def initialize(value = nil)
    @widget = Widget.new(value)
    @counter = 0
  end

  def use; widget.run; end
  def direct; @widget.run; end
  def tick; @counter += 1; end
end
```

O grafo pode propor `Box#use -> Widget#run` com evidência
`state_return_inferred` e origem `Box#initialize, Box#widget`.
Para `Box#direct -> Widget#run`, usa `constructor_ivar_inferred`, com origem
`Box#initialize`. Esta origem identifica a atribuição; não afirma que o valor
retornado por `initialize` seja o objeto construído por `Class.new`.

São hipóteses sobre instâncias **depois de a construção normal terminar**, no
modelo das fontes fornecidas. Não são garantias de execução nem provas de
imutabilidade. Não entram na seleção `supported-only`. Não se usam estas novas
hipóteses dentro de `initialize`, nem por um getter de outra classe.

## Padrão aceite e abstenção

- O dono é uma classe sem superclass explícita, mixins ou subclasses conhecidas.
  Todas as suas declarações/reaberturas têm de ser suportadas.
- Há um único `initialize` próprio. O corpo contém apenas atribuições diretas a
  campos, até 64 instruções. O campo consultado recebe diretamente `Foo.new`.
  Outros campos podem receber valores simples sem invalidar aquele candidato.
- Argumentos/defaults aceitam formas sintáticas simples, como literais,
  parâmetros, constantes e coleções limitadas. Chamadas, blocos, `self`, splats,
  controlo condicional e defaults que chamam métodos são recusados. A inspeção
  dos valores tem limites de 64 nós e profundidade 12.
- Existe exatamente uma escrita observada naquele campo, no construtor. Setters,
  `attr_writer`/`attr_accessor`, `||=`, `&&=`, operações, atribuição múltipla e
  escritas em blocos ou outras reaberturas impedem a hipótese. Mesmo reatribuir
  `Foo.new` é motivo de abstenção nesta etapa.
- O getter explícito apenas devolve o campo, com retorno implícito, `return` ou
  forma endless. `attr_reader` é reconhecido quando não há redefinição/conflito.
- A classe construída tem lookup único/exato, sem `new` próprio conhecido nos
  caminhos já verificados pela primeira etapa. APIs de construção/accessors
  próprios no dono e aliases de constantes conhecidos também bloqueiam.

A análise junta as escritas dos métodos de **todos os ficheiros fornecidos**;
um ficheiro sem metadados desta política ou com erro de parse impede concluir
que não há outras escritas. Isso não demonstra que o chamador forneceu todo o
programa e todas as dependências.

Efeitos reflexivos conhecidos, como `instance_variable_set`, `eval`, alterações
de métodos/constantes, `allocate` ou `send` de destino desconhecido, tornam a nova
inferência de estado indisponível no projeto. Esta guarda global é conservadora:
pode recusar um caso seguro porque não acompanha a identidade dos objetos.
Um `send` literal para método comum não é automaticamente bloqueado; as escritas
observadas nesse método continuam a contar.

Campos de instância de objetos-classe e campos de instâncias não são misturados.
Variáveis de classe, campos recebidos apenas por parâmetro, fluxos locais,
retornos condicionais, cadeias recursivas de fábricas e anotações não são
inferidos por esta entrega.

Ruby permite patches externos, serialização/alocação especial e alterações fora
das fontes analisadas. Os guardas não fecham esse mundo dinâmico. Se não houver
nova hipótese utilizável, o resolver conserva o fallback duck anterior e a sua
própria categoria de evidência; abster-se aqui não elimina todas as arestas.

## Implementação e custo

`rb/marta_state_facts.rb` extrai factos na árvore Prism que já estava em memória.
`ruby_ast.py` transporta os metadados; `param_types.py` agrega declarações.
`return_types.py` constrói o índice de escritas apenas quando há uma consulta de
estado e memoriza os resultados por campo. Projetos opacos/antigos dispensam a
construção das tabelas por campo. Não se cria um dicionário de efeitos vazio para
cada método no JSON.

`call_graph.py` aplica as hipóteses e conserva a origem e a categoria inferida.
O conflito entre um método explícito e um accessor gerado também passa a impedir
uma hipótese de retorno da primeira etapa, em vez de escolher uma definição.

Não há novo subprocesso, execução do código-alvo, embedding ou pedido LLM para
esta inferência. Há metadados adicionais no parse e índices locais. Um grafo
diferente pode alterar o contexto e o custo das fases LLM seguintes; não se
promete custo total idêntico, aceleração ou ganho de qualidade sem medição.

## Proveniência e validação

Política `constructor-state-v1`; resolver **5**. O extrator, o índice e a política
entram na proveniência da análise. Metadados antigos não provam ausência de
escritas. Caches incompatíveis são reconstruídas pelos mecanismos existentes;
não se migram experiências nem se reclassificam resultados dos papers.

`test_constructor_state.py` cobre getters/atributos, escrita direta, reaberturas
em vários ficheiros, mutações e reflexão, aliases, herança, colisões de métodos,
metadados incompletos, limites, defaults e origem das hipóteses. Os exemplos Ruby
são analisados com o Prism instalado, sem os executar nem consultar modelos.

A precisão/alcance em repositórios reais continua a ser uma avaliação pendente.

Validação desta entrega: **1053 testes locais aprovados**, sete ignorados no
host; **16 testes aprovados no contentor existente**, incluindo quatro daqueles
ignorados. Total: **1069 aprovados; três permanecem ignorados**. Sem instalações
ou inferência real. O parse usa Ruby 3.4.10/Prism 1.5.3 já disponíveis.
