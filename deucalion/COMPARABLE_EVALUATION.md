# Comparabilidade MARTA / XRepoTest

Atualização: 7 de outubro de 2026. Esta preparação é independente da geração e
não modifica o benchmark, as suites exportadas, a imagem repaired-v2 nem os
resultados anteriores. Ainda não há um novo avaliador de mutação validado.

## Protocolo comum

- Mesmas tarefas oficiais, código Ruby e versões de dependências, identificados
  por hashes. Os 675 IDs na experiência principal e os mesmos 97 IDs em todos
  os braços de ablação. Falhas e ausência de testes permanecem no denominador.
- Um resultado final por tarefa. A MARTA pode juntar várias rondas na sua suite;
  o pipeline XRepoTest fornece a sua resposta. Declarar os diferentes orçamentos,
  chamadas, tokens, tempos e mecanismos; não alegar igualdade de orçamento.
- Mesmo modelo/digest, configuração e avaliador para a comparação controlada
  que ainda vamos executar. Resultados das tabelas do paper são referência
  externa, não uma reprodução controlada do ambiente dos autores.
- CSR/TPR/IR e cobertura focal seguem o avaliador publicado com as duas
  correções de cobertura já autorizadas. IR é análise sintática, não prova de
  execução dinâmica. Não alterar prompts para satisfazer a heurística.
- Mutação deve medir somente a suite fornecida, no método focal correto. Todas
  as abordagens e braços terão de usar a mesma versão final validada do executor.
  Uma correção exige nova pasta de avaliação e proveniência; não sobrescrever
  os checkpoints antigos nem regenerar suites para melhorar números.

## Fórmulas do paper (Apêndice D)

Para cada tarefa, score de mutação = mortos / total quando há uma medição válida
com testes aprovados; zero quando não existe medição. MS = média sobre todas as
N tarefas. MS@Pass = média sobre tarefas com testes aprovados E mutação válida,
conforme a definição do conjunto `pass` no paper. Guardar N e Npass.

O código publicado `base/metrics.py` devolve uma razão agrupada por número de
mutantes, em vez destas médias. `xrepotest_paper_metrics.py` calcula as fórmulas
do paper a partir de resultados congelados; mantém uma razão agrupada apenas
como diagnóstico e marca a validade da mutação como não verificada. Corrigir
as fórmulas não corrige as medições de origem.

Exemplo: tarefas com 1/1 e 0/9 mutantes mortos têm média 50%, mas razão agrupada
10%. Acrescentando uma tarefa sem medição, MS = 33,33% e MS@Pass = 50%.

## Evidência disponível e limites

No subset de 97: 77 testes aprovados, 36 registos de mutação válidos segundo o
código publicado. Das 41 restantes, 11 falham a extração da classe e 30 devolvem
“No mutations generated”. Esta última mensagem também esconde erros de
arranque: o wrapper ignora stderr e devolve-a quando não encontra contagens.

Diagnósticos locais em Docker repaired-v2, offline e sem instalações, usaram
suites triviais de diagnóstico, NÃO as suites geradas no cluster:

- Pundit (220): `uninitialized constant RSpec` ao carregar spec_helper antes de
  carregar o RSpec; classificado incorretamente como zero mutantes.
- Dotenv (155): uma suite que apenas verifica `true == true` viu 197 testes
  disponíveis, incluindo specs humanas, e reportou 84/85 mortos. A integração
  Mutant usa `spec/` por omissão mesmo que `requires` inclua apenas temp_spec.
- Uma proposta de argumentos explícitos e RSpec carregado antes do helper
  limitou a descoberta de specs e desbloqueou Pundit. A seleção por descrições
  e o carregamento duplicado da suite exigem validação adicional.

Não se pode atribuir todos os 30 casos à mesma causa ou inferir que os autores
usaram exatamente esta configuração. Os MS agrupados 63,43% (675) e 67,27%
(97) antigos são provisórios; não são o MS macro das tabelas.

## Diagnóstico seguinte, sem chamadas ao modelo

`run_xrepotest_mutation_diagnostic_cpu.sh` executa em cópias descartáveis as
suites exatas exportadas, nos casos 155/220 e nos casos de extração 4/416.
`xrepotest_mutation_diagnostic.py` conserva stdout, stderr, código de saída,
configuração, hash da suite, ambiente e hashes do avaliador.

Compara o publicado com uma PROPOSTA de configuração:

1. carregar RSpec antes do spec_helper;
2. indicar explicitamente temp_spec.rb, sem descoberta automática de spec/;
3. deixar a integração carregar a suite uma única vez;
4. marcar apenas exemplos provenientes da suite fornecida como elegíveis e
   associá-los ao método focal, sem depender dos textos de describe.

A proposta não modifica o parser publicado, os operadores ou as fórmulas.
A proposta final de configuração passou controlos locais em Dotenv e Pundit:
ambos descobriram e selecionaram exatamente um exemplo fornecido, com um único
método focal. Estes controlos não são resultados de qualidade: eram suites
triviais, que obtiveram 1/85 e 1/57 mortos (o Mutant também pode observar efeitos
de carregamento). As suites reais e os restantes projetos ainda não foram
validados com a proposta.

As falhas de extração podem continuar; devem ser observadas, não adivinhadas.
O relatório é diagnóstico e não substitui os resultados oficiais.

Só depois de validar o método focal, a exclusão de specs humanas, controlos
negativos/positivos, as falhas reais e os dez projetos poderemos fechar a versão
corrigida e voltar a medir as suites congeladas de todas as abordagens. A
comparação de mutação da ablação deverá apresentar o efeito sobre disponibilidade
e sobre qualidade: MS sobre os mesmos IDs e, se se comparar scores condicionais,
um conjunto comum de medições válidas para a comparação emparelhada.
