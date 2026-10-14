# Continuação da ablação sem grafo em CPU

O cohort `qwen36_35b_ablation97_no_graph_v1` mantém as 97 tarefas selecionadas antes
dos resultados. Em 14 de outubro de 2026, o GPU job 2028996 tinha parado ao chegar
ao limite temporal: 33 tarefas `complete`, 5 `no_tests` e 1 `running`. O utilizador
autorizou continuar em CPU por esgotamento da quota GPU.

## O que fica igual

`benchmark/xrepotest/run.py`, o backend Ruby, os prompts e `generation/experiment.json`
não são alterados. O fingerprint da geração continua
`d08c8e83198082e22c13bb86fb6014da0632ddbea802bb8f799c2e0c08a43ae6`.
Usam-se o mesmo container Ruby, bundles, repos, tarefas e caches existentes.

O launcher lê o manifesto existente e restaura Qwen3.6:35b (digest fixo), thinking
ligado, contexto 32768, saída 16384, temperatura 0.6, top_p 0.95, penalização de
presença 0, timeout 1800 segundos, três rondas e três tentativas. Não alarga o
timeout por causa da CPU. Recusa configurações incompatíveis e exports já completos.

## O que muda e como se regista

`run_xrepotest_generate_cpu.sh` usa a conta CPU, `normal-x86`, 32 CPUs, 64 GiB e
janelas de 48 horas. O Ollama tem `LLAMA_ARG_THREADS=8`, validado pelo log real do
runner; a verificação exige VRAM zero, contexto correto, pesos fixos e Ollama 0.30.7.
O carregamento usa um prompt vazio: não constitui uma geração adicional.
Não se instala nem descarrega nada.

`metadata/cpu_resume_<JOBID>.json` regista a fronteira por job, prova CPU, timestamp,
estados iniciais/finais, hashes de todos os ficheiros de tarefas já terminadas e
tamanhos/hashes dos logs de eventos à entrada/saída. A auditoria confirma que as
tarefas anteriormente `complete` ou `no_tests` e o manifesto ficaram intactos.
A lista `tasks_finished_in_cpu_job` identifica tarefas finalizadas nesse job;
não significa necessariamente que todo o seu trabalho tenha sido feito em CPU.
Os eventos antigos são preservados, incluindo tentativas interrompidas arquivadas
pela política existente da MARTA.

O lock `generation-job.lock` é o mesmo que na execução GPU: impede duas gerações
simultâneas neste cohort. O evento USR1 de aproximação do walltime agenda uma
continuação CPU depois do job atual (`XREPO_CPU_CHAIN=1`, por omissão). Cancelamentos
e erros não são re-submetidos automaticamente. Depois das 97 tarefas, a geração
exporta `processed.jsonl` e termina; usa-se então o avaliador core da branch
`codex/xrepo-comparable-evaluation`, como nos outros braços.

## Interpretação experimental

Esta é uma ablação com execução GPU/CPU mista. Preservam-se os 38 resultados
terminais GPU, sem repetir tarefas para melhorar as métricas. Uma tarefa que já
tinha começado em GPU pode continuar/reiniciar a tentativa interrompida em CPU.
Alterar o backend pode afetar o percurso numérico/estocástico; não se garante uma
resposta idêntica à que seria obtida em GPU. Esta diferença deve ser declarada
como limitação da comparação com os braços só GPU. Tempos e consumo por backend
devem ser apresentados separadamente.

## Arranque no Deucalion

```bash
(
set -e
cd /projects/F202407648IACDCF2/mario/MARTA-ablation
test "$(git branch --show-current)" = codex/ablation-options
git pull --ff-only
export MARTA_CLUSTER_BASE=/projects/F202407648IACDCF2/mario
export MARTA_CLUSTER_CODE="$PWD"
export XREPO_RUN=qwen36_35b_ablation97_no_graph_v1
export XREPO_CPU_CHAIN=1
mkdir -p logs
JOB=$(sbatch --parsable --export=ALL deucalion/run_xrepotest_generate_cpu.sh)
echo "Retoma CPU sem grafo: $JOB"
squeue -j "$JOB"
)
```

As restantes cinco execuções XRepoTest são independentes. Este job não toca nos
seus resultados, servidores ou agendamentos.
