# Medição comum de mutação — 21 de outubro de 2026

O diagnóstico `mutation_validate_2099026` passou os controlos nos dez projetos.
Confirmou 12/14 alvos em execução; 11/12 suites reais produziram medições válidas.
A tarefa 166 não oferece um subject no Mutant e continua explicitamente indisponível.
Estes valores são diagnósticos, não scores finais. Ver [MUTATION_VALIDATION.md](MUTATION_VALIDATION.md).

## Mesma medição para as onze configurações

| Índice do array | Configuração | Tarefas |
|---|---|---:|
| 0 | MARTA normal | 675 |
| 1 | Sem feedback de cobertura | 97 |
| 2 | Sem reparação | 97 |
| 3 | Sem pesquisa de métodos | 97 |
| 4 | Sem sugestões de tipos | 97 |
| 5 | Sem grafo | 97 |
| 6 | XRepoTest Standard | 675 |
| 7 | XRepoTest LSP | 675 |
| 8 | XRepoTest Ficheiro | 675 |
| 9 | XRepoTest BM25 | 675 |
| 10 | XRepoTest Dense | 675 |

Todas usam o mesmo executor/Mutant 0.15.1 já validado, o mesmo timeout de 900s e
quatro workers. Não há GPU, modelo, rede nem instalação de dependências. Só se
executa mutação nas suites que passaram a avaliação core. Ausência de suite e
falha da suite continuam registadas nos mesmos IDs e denominadores.

Cada configuração escreve numa pasta `mutation_v1/` nova, junto da sua avaliação
core, sem substituir fontes, geração, avaliações anteriores ou diagnósticos. Os
inputs são montados read-only; só a nova pasta da configuração é gravável. O braço
sem grafo lê o export congelado em `project_parallel/merged/processed.jsonl`.

## Proveniência e retoma

Antes de medir, conferir o certificado do diagnóstico (incluindo hashes do
suporte/hook, controlos e quatro suites reais que verificaram as correções),
hashes do dataset, ambiente, avaliador, respostas, avaliação core, seus 675/97
registos e seleção congelada. O preflight faz isso nas onze configurações sem
medir. A versão de cada executor e das fórmulas fica no novo manifest.

- Nunca repetir medições terminais, incluindo indisponíveis, para melhorar scores.
- Reaproveitar o resultado de um subprocesso concluído se houver interrupção antes
  da publicação do checkpoint da tarefa. Trabalho realmente incompleto é arquivado.
- Mudanças de executor, entradas ou ambiente recusam retoma; não misturar versões.
- Só o aviso de walltime encadeia o mesmo índice do array; cancelamentos e erros
  comuns não desencadeiam novas execuções. `XREPO_MUTATION_CHAIN=0` desativa isso.
- Cada pasta tem lock independente; lançamentos duplicados recusam concorrência.
- Para a referência normal de 97 tarefas, extrair as mesmas medições da execução
  normal de 675 em `ablation97_summary.json`; não voltar a executar os testes.

A disponibilidade inclui `valid`, `unavailable`, `no_tests` e `core_failed`.
`unavailable` tem motivo e evidência (stdout/stderr, contagens, identidade), não é
uma medição com score zero. Para MS global, a contribuição de tarefas sem medição
é zero, preservando N. MS@Pass usa apenas suites aprovadas com medição válida,
com Npass/valid_measurements explícitos. Uma razão agrupada por número de mutantes
fica como diagnóstico separado, não como MS das tabelas. As contagens e operadores
do Mutant são mantidos; não se eliminam mutantes ou tarefas para melhorar números.

Resultados: `summary.json`, `detailed_results.jsonl`, `tasks/ID.json`,
`measurements/ID/`, `complete.json` e `experiment.json` em cada `mutation_v1/`.
Os campos core são conservados; os scores antigos de mutação são excluídos da
nova agregação. Logs core antigos permanecem como evidência histórica; o resultado
novo está em `mutation_execution` e em `measurements/`, nunca nesses logs antigos.

## Lançamento no Deucalion

```bash
(
set -e
cd /projects/F202407648IACDCF2/mario/MARTA-evaluation
git pull --ff-only
export MARTA_CLUSTER_BASE=/projects/F202407648IACDCF2/mario
export MARTA_CLUSTER_CODE="$PWD"
export XREPO_MUTATION_VALIDATION=/data/xrepo/runs/qwen36_35b_thinking_bundle_loading_v4/diagnostics/mutation_validate_2099026/results/report.json
export XREPO_MUTATION_CHAIN=1
mkdir -p logs
PRE=$(sbatch --parsable --export=ALL deucalion/run_xrepotest_mutation_preflight_cpu.sh)
MUT=$(sbatch --parsable --export=ALL --array=0-10 --dependency="afterok:$PRE" deucalion/run_xrepotest_mutation_cpu.sh)
echo "Preflight: $PRE"
echo "Mutação (11 configurações): $MUT"
squeue -j "$PRE,$MUT"
)
```

Os onze workers usam quatro CPUs cada. Só arrancam após o preflight bem-sucedido.
A submissão acima não foi executada localmente: exige acesso ao Slurm do projeto.
Após todas as pastas estarem seladas, juntar os artefactos e efetuar a análise.
O estudo local Qwen3-8B é separado; este lançamento cobre as experiências 35B.
