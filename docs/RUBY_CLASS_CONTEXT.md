# A10 — contexto das classes com comportamento e limites explícitos

Entrega posterior a `79781626f`. Melhora a informação usada na síntese das
classes, sem acrescentar pedidos LLM, subprocessos, retrieval ou embeddings.
A qualidade do resultado no corpus continua a precisar de avaliação empírica.

## Problema e alteração

O contexto anterior reunia o esqueleto da classe e a primeira linha da definição
de até 40 métodos. Voltava a abrir o ficheiro para extrair cada linha e não usava
as descrições de comportamento que a MARTA já tinha produzido. Uma declaração
reaberta também podia ficar representada apenas pelo primeiro esqueleto escolhido.

O novo contexto combina registos identificados:

- declarações com ficheiro, intervalo, nome qualificado e superclass expressa;
- métodos com identidade Ruby e localização, distinguindo instância (`#`) de
  singleton (`.`), e nomes/kinds dos parâmetros reportados pelo parser;
- excertos dos sumários de implementação da **primeira passagem**, baseados no
  código do próprio método;
- statements não metodológicos já capturados pelo parser, quando há espaço,
  incluindo constantes, macros de atributos e chamadas de DSL.

Os sumários da primeira passagem já existem nesta fase, incluindo os de
construtores e métodos que não foram selecionados para gerar testes. A preparação
usa esses objetos em memória. A classe continua a receber uma única síntese LLM.
A população de classes e a seleção de métodos para geração mantêm o contrato
anterior; classes sem métodos não passam a custar novos pedidos.

A escolha da primeira passagem mantém esta entrada independente do enriquecimento
pelo grafo e das intenções extraídas dos READMEs. Os métodos não recebem sumários
suplementares apenas para enriquecer as classes. A fixture de integração verifica
entradas de classe iguais com e sem grafo quando a primeira passagem é igual.

## Seleção e orçamento

`class_context.py` prepara uma vista com limite local de
`MARTA_MAX_CONTEXT_CHARS` (6000 por omissão), seguido do orçamento da mensagem
inteira já existente, que inclui sistema, entrada, reserva de saída e margem.
Esse limite local é de caracteres; não equivale ao limite de tokens do servidor.

A seleção é determinística: declarações, construtores de instância, restantes
métodos e statements. Dentro dos grupos de métodos, intercala os ficheiros por
ordem estável para considerar diferentes partes de uma classe reaberta antes de
consumir o orçamento com todos os métodos do primeiro ficheiro.

Todos os métodos são elegíveis; desaparece o corte fixo dos primeiros 40. Isto
**não significa que todos caibam**. Cada descrição tem um excerto de até 320
caracteres, marcado como incompleto quando necessário. É um cap de apresentação
de prosa, identificado na política, não uma seleção de relevância calibrada.
Quando o registo com descrição não cabe, tenta conservar os factos do parser.
Se nem estes cabem, o método fica omitido e a seleção continua com os seguintes.
Um statement grande não impede considerar statements posteriores mais pequenos.

A identidade da classe e os totais preparados ficam no núcleo. Uma identidade
excecionalmente grande pode exceder o limite local; isso fica registado e o
orçamento total decide se o pedido obrigatório cabe, antes de contactar o modelo.
Os contadores locais dizem **prepared**, distinguindo a preparação local da
redução adicional da mensagem inteira.

Quando o orçamento total precisa de cortar, retira registos completos. Não corta
uma declaração Ruby ou informação de um método a meio. O prompt indica quantos
registos preparados foram efetivamente submetidos e trata omissões como
informação desconhecida.

## Evidência e limites

Declarações reabertas ficam separadas por origem. Referências repetidas ao mesmo
objeto do parser são deduplicadas, mas nós distintos na mesma linha/intervalo
continuam separados. Esta preparação não escolhe a definição ativa em runtime.
As regras existentes de identidade dos métodos e o índice de tipos mantêm os
seus próprios limites; não se reconstrói aqui a ordem de autoload/execução Ruby.

Os nomes/kinds dos parâmetros são factos do parse. Os sumários de implementação
são texto gerado, podem estar incompletos ou errados e não constituem um contrato
verificado. O prompt distingue essas fontes e pede que não se inventem defaults,
visibilidade, tipos de retorno, comportamento herdado ou um vencedor entre
definições. Parâmetros reportados não são apresentados como uma assinatura Ruby
executável com valores default reconstruídos.

A calibração dos gates semânticos do judge continua aberta, tal como a avaliação
de precisão/alcance do grafo e a inferência de retornos (A7). Melhorar esta entrada
não prova maior precisão do judge nem estabelece valores de limiar por omissão.

## Custo e proveniência

| Alteração | Trabalho evitado ou informação aproveitada | Custo adicional |
|---|---|---|
| Metadata e sumários em memória | Elimina a leitura de ficheiro por assinatura na fase das classes | Agrupamento e seleção locais |
| Comportamento por método | Aproveita descrições já pagas na primeira passagem | O input por classe pode ter mais tokens que um stub curto |
| Limites e registos inteiros | Evita enviar uma classe inteira ou cortar código arbitrariamente | Comparação local de tamanhos e contagem da mensagem completa |
| Declarações reabertas | Evita escolher silenciosamente um único esqueleto | Referências aos objetos de declaração das classes elegíveis |

Não há outro modelo, embedding ou pedido de compressão. O ganho específico é
I/O evitado e informação mais útil por chamada; não se afirma uma redução global
de tokens/tempo nem um ganho de qualidade já medido. A retenção adicional de
metadata limita-se às classes que já pertencem à fase de síntese.

A política `class-source-evidence-v1`, o limite de contexto e o hash do builder
entram na proveniência/fingerprint. Eventos `class_context` distinguem contagens
disponíveis, preparadas e omitidas, descrições aproveitadas, tamanho e origem dos
sumários; eventos `prompt_budget` registam reduções posteriores. O arquivo de
análise conserva o pedido efetivo. O texto final das classes já participa na
identidade dos vetores. Não há migração automática de experiências ou resultados
dos papers para esta nova preparação.

## Verificação offline

`test_class_context.py` cobre factos e descrições sem ler fontes, mais de 40
métodos elegíveis, reaberturas, ordem estável entre ficheiros, limites/excertos,
fallback para factos, ausência de comportamentos inventados, registos inteiros
sob orçamento total, identidade obrigatória e proveniência. A integração usa
Prism real e respostas scriptadas: verifica a população/custo de pedidos,
ausência de releitura na fase de classes, cache hit e independência do grafo.
Não faz inferência real, instalações ou downloads.

Validação final: **947 testes locais aprovados**, sete ignorados no host;
**16 testes aprovados no container existente**, incluindo quatro dos ignorados.
Total: **963 aprovados; três permanecem ignorados**. Os avisos de depreciação
Pydantic/Chroma já existentes não exigiram atualizar pacotes.
