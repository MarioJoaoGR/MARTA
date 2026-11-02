# Validação da mutação — 20 de outubro de 2026

Esta é uma proposta de executor comum, separada da geração e das quatro métricas
core já congeladas. Não substitui resultados nem torna válidas as medições antigas.
Nenhuma geração é repetida e não se instalam pacotes. Usa Mutant/mutant-rspec 0.15.1
já presentes na imagem repaired-v2; fontes Ruby, suites e operadores ficam iguais.

## Correções e verificações

- Preservar o caminho relativo completo depois do nome do projeto: por exemplo,
  `rom/core/lib/rom/pipeline.rb` aponta para `core/lib/rom/pipeline.rb`.
- Selecionar a definição por nome e intervalo de linhas oficiais, verificando
  também o código focal. Operadores (`[]`, `==`, setters) usam o campo de nome
  da AST tree-sitter, não apenas nós identifier. Não se usa a primeira ocorrência.
- A classe/módulo e o tipo de método inferidos são apenas candidatos. Antes de
  executar mutantes, exigir exatamente um subject do Mutant com a mesma expressão,
  caminho físico completo e intervalo de linhas da tarefa. Falhar em vez de
  adivinhar quando o Mutant não consegue representar o alvo.
- Carregar RSpec antes do helper, e o ficheiro focal antes de selecionar subjects.
  A integração recebe exclusivamente a suite fornecida e carrega-a uma vez.
  `--options /dev/null` evita opções locais que acrescentem descoberta de testes.
- Cada exemplo recebe metadata que o associa ao alvo independentemente do texto
  de describe. Verificar no ambiente real que todos os exemplos descobertos,
  elegíveis e selecionados vêm da suite fornecida. Specs humanas são recusadas.
- Capturar stdout, stderr, exit code, identidade, contagens e hashes. Exigir o
  resumo completo (`Results == Mutations`) e contagens consistentes. Falhas de
  arranque, neutral failures, timeouts e medições incompletas são inválidas,
  nunca scores zero disfarçados. Exit 1 por mutantes sobreviventes é normal.
- Em timeout, terminar todo o grupo de processos, incluindo workers do Mutant.
- Manter a contagem/score do Mutant e os operadores instalados; não reescrever
  os métodos nem remover mutantes para melhorar números.

## Diagnósticos locais

`xrepotest_mutation_validate.py` cria cópias descartáveis da imagem existente,
sem rede. Para cada um dos dez projetos testa uma função sintética simples com
uma suite que verifica o resultado e outra que apenas verifica true. Os controlos
passam quando ambas as medições são válidas, os conjuntos têm o mesmo número de
mutantes e a suite útil mata mais mutantes. Um ficheiro sentinela em spec/ causa
uma exceção se a descoberta automática de specs humanas voltar a acontecer.
Os controlos sintéticos NÃO são resultados de benchmark.

Os dez projetos passaram estes controlos: a suite útil matou 12/12 e a suite
trivial 1/12 em cada ambiente. Não se exige zero no controlo trivial: preserva-se
o comportamento e a contagem do Mutant, incluindo mortes que não demonstram
qualidade das asserções fornecidas. O isolamento é confirmado separadamente pelos
exemplos efetivamente selecionados e pelo sentinela. Passaram também 12 testes de
regressão do novo suporte e 11 testes existentes das fórmulas de agregação.
Os registos completos estão em
`~/.cache/marta-xrepotest/mutation-validation-20261020/`.

A seleção estática identifica 673/675 definições. As tarefas 126 e 127 definem
métodos em blocos DSL sem owner nomeado; ficam explicitamente não resolvidas.
A inspeção real confirmou, entre outros, os casos 4 (`Capybara::Result#[]`),
155 (`Dotenv#parse`), 220 (`Pundit::Context#authorize`) e
416 (`ROM::Pipeline::Proxy#method_missing`), com caminho e linhas exatos.
Nas tarefas 166 e 379 o candidato estático existe, mas o Mutant não produz um
subject: a verificação recusa a medição. Não se altera o benchmark para forçar
suporte a estas construções. A disponibilidade real será reportada em todas as
abordagens, mantendo as tarefas no denominador global.

## Diagnóstico no cluster, antes da medição completa

Na branch `codex/xrepo-comparable-evaluation`:

```bash
(
set -e
cd /projects/F202407648IACDCF2/mario/MARTA-evaluation
git pull --ff-only
export MARTA_CLUSTER_BASE=/projects/F202407648IACDCF2/mario
export MARTA_CLUSTER_CODE="$PWD"
mkdir -p logs
sbatch --parsable --export=ALL deucalion/run_xrepotest_mutation_validate_cpu.sh
)
```

O job usa CPU, monta as experiências apenas para leitura e grava em
`runs/qwen36_35b_thinking_bundle_loading_v4/diagnostics/mutation_validate_JOBID/results/`.
Repete os controlos, verifica os alvos em execução e mede como diagnóstico as
suites congeladas dos casos 4/155/220/416 e a primeira suite aprovada de cada
projeto. A escolha é de diagnóstico; não substitui o conjunto de avaliação.
Confere o hash de processed.jsonl e a identidade do avaliador/ambiente contra a
avaliação core. Cada caso conserva as falhas, sem tentar melhorar a suite.

Só depois de inspecionar estes resultados será fechada a medição de produção
numa pasta nova, para MARTA normal, ablações e os cinco modos XRepoTest, com o
mesmo executor. As quatro métricas core e os antigos resultados de mutação ficam
intactos. Este job ainda NÃO mede a mutação completa nem a agenda automaticamente.
MS e MS@Pass devem ser calculados com as fórmulas do paper; a razão agrupada
publicada no código original continua apenas como diagnóstico separado.
