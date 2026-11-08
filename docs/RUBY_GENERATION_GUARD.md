# Verificação das entradas antes de certificar uma ronda

Entrega de 8 de novembro de 2026. Corrige uma falha de validade no caminho de
`generate_rounds`, sem alterar os pedidos de geração ou o protocolo de cobertura.

## Problema reproduzido

A receita de geração era capturada no início, mas não era comparada de novo antes
de gravar o checkpoint. Assim, a ronda podia passar o RSpec e ficar registada com
os hashes/parâmetros antigos depois de uma alteração durante um pedido ao modelo
ou durante a execução dos testes.

Os controlos reproduziram isto com uma mudança na fonte, uma nova declaração de
dependências e uma mudança na temperatura declarada pelo cliente. Em cada caso,
a implementação anterior chegava a certificar a ronda apesar da diferença.

## Fronteiras da verificação

1. A receita inicial continua a ligar fontes, declarações de dependências,
   implementação, alvos, sumários, opções, configuração de prompts e ambiente
   declarado. Inclui agora também opções de carregamento e o digest de modelo
   quando o cliente ou `MARTA_MODEL_DIGEST` o declara.
2. Depois de validar a suite acumulada e antes de certificar uma ronda, volta a
   comparar as entradas/configuração observáveis com essa receita.
3. Ao retomar, faz a mesma comparação depois de reexecutar a suite retida, antes
   de avançar para uma ronda nova ou devolver uma retoma concluída.

Se encontrar diferenças ou não conseguir verificar as entradas, interrompe com
`ResumeValidationError`. O evento `generation_inputs_changed` indica a fronteira
e os grupos que mudaram, sem despejar os valores da configuração. Uma porta
local do servidor que rode sem alterar a configuração declarada continua a não
invalidar a execução.

Os candidatos ainda não certificados são arquivados em `rejected_specs/resume_*`.
As rondas anteriores e o seu checkpoint não são reescritos; os specs associados
ficam no lugar. Não há novas tentativas automáticas para substituir o resultado.
A próxima invocação continua a verificar os hashes dos specs retidos segundo o
contrato existente. A proteção também se aplica quando se usam workspaces/workers
nativos. A API `generate_all`, que não certifica checkpoints de rondas, mantém o
seu contrato anterior.

## Custo e limites

A comparação lê os ficheiros ligados à receita e reconstrói os metadados na
fronteira da ronda/revalidação. Aproveita a exclusão de árvores de outputs e
não é executada a cada pedido ou a cada método. Acrescenta IO e hashing;
não é um ganho de tempo global medido.

Os planos de carregamento já registados não são recalculados durante a
verificação. Compara-se o âmbito de fontes/declarações e as opções de
carregamento observáveis, sem repetir inspeções Bundler/Prism, gerar novos
preloads ou fazer chamadas adicionais a Ruby, RSpec ou ao LLM. O cálculo do
contexto de carregamento para os pedidos mantém o seu comportamento anterior.

O digest é **declarado**, não descoberto ou verificado contra os pesos do modelo.
A comparação deteta diferenças nas fronteiras; não prova que não houve uma
alteração intermédia já revertida, nem atesta dependências instaladas fora do
âmbito, código externo ou comportamento não declarado de callbacks. Não é uma
sandbox e não transforma specs ainda sem checkpoint em resultados aceites.

O formato do checkpoint e as métricas mantêm-se. Como noutras mudanças de
implementação, não se migram receitas ou resultados congelados de experiências
anteriores. Não se recorreu ao cluster nem se alterou o avaliador XRepoTest.

## Verificação

Testes com respostas simuladas e RSpec real cobrem alterações de fontes,
dependências, parâmetros/digest, opções de carregamento e configuração inválida;
revalidação sem novos pedidos; arquivo seletivo numa ronda posterior; workers;
e o caso normal sem novas inspeções de carregamento. A regressão inclui a
comparação offline de prompts/chamadas/specs com a implementação anterior.

Validação final: **1175 testes locais aprovados**, seis ignorados no host;
**16 aprovados no contentor existente**, incluindo quatro daqueles ignorados.
Total: **1191 aprovados; dois permanecem ignorados**. Sem inferência real,
instalações ou downloads.
