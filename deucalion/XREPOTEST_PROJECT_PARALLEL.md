# Ablação sem grafo: divisão por projeto, com validação prévia

## Objetivo e invariantes

O cohort original é `qwen36_35b_ablation97_no_graph_v1`, com 97 tarefas em dez
projetos. A divisão usa a atribuição real de `file_path` do dataset oficial, guardada
em `selections/xrepotest_ablation97_projects_v1.json`. Não faz uma nova amostragem.
Cada projeto mantém TODOS os seus alvos do subset original, o código de produção
completo, as fontes/bundles certificados, os parâmetros e a política sem grafo.

`benchmark/xrepotest/run.py` e o backend Ruby não são alterados. O fingerprint
continua `d08c8e83198082e22c13bb86fb6014da0632ddbea802bb8f799c2e0c08a43ae6`.
Cada manifesto filho só restringe três campos administrativos: `task_selection`,
`input_hashes` e `runtime_hashes`, mantendo a entrada do projeto byte a byte. O
contexto disponível para um alvo é o mesmo, porque os grupos já eram processados
isoladamente pelo runner e não há recuperação de specs de outras tarefas.

## Validação enquanto a execução original continua

`run_xrepotest_project_split_validate_cpu.sh` não carrega o Ollama nem invoca a
pipeline de geração. Consulta as tarefas e a configuração original, produz uma
partição disjunta dos mesmos 97 IDs e invoca o runner congelado com `--validate-only`
para cada um dos dez projetos. O runner verifica as fontes, ambiente e referências
reais. Cada configuração calculada tem de coincidir integralmente com a projeção
do manifesto original. Os relatórios ficam em
`xrepotest/reports/project_split_<JOBID>/`, incluindo `validation.json`.

Esta validação não exige parar o job 2039852. Os números de tarefas pendentes são
provisórios enquanto ele continua; a preparação volta a ler os estados finais.
Não se escrevem resultados nem checkpoints na pasta original nesta fase.

## Preparação, apenas depois da validação e de parar o job serial

`xrepotest_project_split.py prepare --validation <validation.json>` exige um
certificado válido e adquire os dois locks do original: `generation-job.lock` e
`generation/run.lock`. Recusa avançar enquanto algum processo serial estiver ativo.
Guarda hashes de toda a geração original, que passa a permanecer congelada.

Só cria filhos para projetos com tarefas por terminar. Por exemplo, com 40 tarefas
terminadas em Capybara, Dotenv, Grape e Hanami, cria seis filhos: Hashie (10), HTTParty
(10), Pundit (7), ROM (10), RSpec-core (10) e Shoryuken (10).
O nome do filho é `<cohort>_cpu_<projeto>`, com hífen convertido em underscore.

Copia apenas a análise do projeto, os seus estados/specs e o histórico de tentativas
interrompidas. Copia ficheiros independentes, sem hardlinks/symlinks partilhados.
Confere hashes contra o snapshot original. Não copia workspaces temporários: uma
tarefa `running` conserva os artefactos anteriores, que o runner original arquiva
antes de reiniciar a tentativa, pela política que já existia.

O registo `metadata/project_split.json` no cohort original identifica os filhos,
os hashes de partida, a atribuição de tarefas e os limites dos logs de eventos.
Falhas na preparação deixam os temporários para inspeção e não apagam o original.
Uma preparação já publicada é idempotente e não substitui filhos que avançaram.

## Workers CPU

Usa-se o launcher CPU existente com `XREPO_PROJECT_SHARD=<projeto>` e `XREPO_RUN`
igual ao nome registado do filho. O worker recupera os parâmetros do manifesto
filho, valida a sua seleção e os hashes congelados e exige o mesmo Ollama/pesos,
contexto 32768, saída 16384, thinking ligado e oito threads reais. Continua em
janelas de 48h, de acordo com `XREPO_CPU_CHAIN`.

Cada worker tem a sua pasta de resultados, home, workspace e servidor Ollama. O
lock exclusivo do filho impede duplicações; um lock partilhado no original impede
retomas seriais simultâneas e permite vários projetos diferentes em paralelo.
Os launchers serial CPU/GPU também recusam cohorts com o marcador de divisão.
O job serial já em execução não muda de comportamento só por atualizar os ficheiros.

## Junção e avaliação

`xrepotest_project_split.py merge` só publica depois de todos os filhos terem um
export completo, estados terminais e suites coerentes com esse export. Verifica
IDs estrangeiros/duplicados/ausentes e os resultados anteriormente terminados.
Os projetos já concluídos vêm do snapshot original; os restantes vêm do respetivo
filho, incluindo os casos `no_tests`. O denominador final é sempre 97.

O export reunido fica em `project_parallel/merged/processed.jsonl` no cohort pai,
com manifesto e auditoria próprios. Não substitui os estados/checkpoints do original.
Depois usa-se o mesmo avaliador core e a seleção original das 97 tarefas.

O histórico GPU/CPU continua documentado. Os logs copiados contêm custos herdados:
para consumo, conta-se o original uma vez e apenas os novos eventos após a fronteira
de cada filho. Não se somam indiscriminadamente os logs do original e dos filhos.
Não se promete igualdade numérica de respostas entre execuções estocásticas nem
uma aceleração igual ao número de workers; o projeto mais lento domina o prazo.

## Primeiro comando no Deucalion: só validação

```bash
(
set -e
cd /projects/F202407648IACDCF2/mario/MARTA-ablation
test "$(git branch --show-current)" = codex/ablation-options
git pull --ff-only
export MARTA_CLUSTER_BASE=/projects/F202407648IACDCF2/mario
export MARTA_CLUSTER_CODE="$PWD"
mkdir -p logs
JOB=$(sbatch --parsable --export=ALL deucalion/run_xrepotest_project_split_validate_cpu.sh)
echo "Validação da divisão: $JOB"
echo "Log: $PWD/logs/xrepo_split_validate_${JOB}.out"
squeue -j "$JOB"
)
```

## Arranque após a validação aprovada

`start_xrepotest_project_parallel.py --validation-job 2061566 --serial-job 2039852`
funciona com o Python 3.6 do host. Confirma primeiro o certificado e o manifesto.
Agenda a preparação CPU com `afterany` do job serial, se este ainda estiver ativo;
só depois envia TERM ao batch desse job específico. Assim executam-se os traps de
limpeza/auditoria existentes, sem acionar a continuação por USR1. Se a submissão
falhar, não se cancela o serial. Se o ID antigo já não estiver ativo, não se cancela
nenhum outro job; os locks da preparação detetam uma eventual retoma serial ativa.

`run_xrepotest_project_split_prepare_cpu.sh` corre as cópias/hash checks num nó CPU,
fora do login, e lança os projetos pendentes. `submit_xrepotest_project_workers.py`
guarda imediatamente cada ID em `metadata/project_jobs.json`; repetir a submissão
não cria jobs duplicados. Em falha parcial, pode executar-se novamente apenas esse
script para submeter os projetos que ainda não receberam ID. Os jobs previamente
registados que tenham falhado exigem diagnóstico antes de uma retoma explícita.

Cada projeto usa janelas de 48h e a conta CPU. Os cinco modos oficiais XRepoTest
continuam nas suas execuções independentes.

## Junção final e avaliação core

`run_xrepotest_project_merge_evaluate_cpu.sh` valida e reúne os 97 resultados antes
de invocar o mesmo `benchmark.xrepotest.evaluate` usado nas outras ablações, com a
seleção original e sem mutação. A saída fica no cohort pai em `evaluation_core_v1`.
Uma falha na junção impede a avaliação. O job usa o lock de avaliação e pode retomar
no walltime, aproveitando os checkpoints já medidos. Não usa modelo nem GPU.

`xrepotest_official_failure_audit.py` apenas lê as avaliações oficiais existentes
de Standard/LSP, compara as identidades do dataset/avaliador/ambiente com a execução
normal e mostra assinaturas e exemplos dos logs. Estas assinaturas são heurísticas
para diagnóstico: não atribuem automaticamente culpa ao modelo ou ao ambiente.
