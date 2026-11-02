#!/bin/bash
#SBATCH --job-name=xrepo_split_check
#SBATCH --account=f202407648iacdcf2x
#SBATCH --partition=dev-x86
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=00:30:00
#SBATCH --output=logs/xrepo_split_validate_%j.out
set -euo pipefail
BASE=${MARTA_CLUSTER_BASE:-/projects/F202407648IACDCF2/mario}
CODE=${MARTA_CLUSTER_CODE:-$BASE/MARTA-ablation}
XROOT="$BASE/xrepotest"
IMAGE="$XROOT/repaired-v2.sif"
REPORT="$XROOT/reports/project_split_$SLURM_JOB_ID"
mkdir -p "$REPORT/home"
C=(singularity exec --cleanenv --home "$REPORT/home:/home/marta"
    --bind "$CODE:/opt/marta:ro" --bind "$XROOT:/data/xrepo"
    --env PYTHONPATH=/opt/marta --env GOMAXPROCS=4)
HELPER=/opt/marta/deucalion/xrepotest_project_split.py
VIRTUAL_REPORT="/data/xrepo/reports/project_split_$SLURM_JOB_ID"
"${C[@]}" "$IMAGE" python3 -B -m benchmark.xrepotest.cluster --root /data/xrepo --require-loading
"${C[@]}" "$IMAGE" python3 -B "$HELPER" plan --report "$VIRTUAL_REPORT/plan.json"
for project in capybara dotenv grape hanami hashie httparty pundit rom rspec-core shoryuken; do
    "${C[@]}" "$IMAGE" python3 -B "$HELPER" validation-env --project "$project" \
        --env-file "$VIRTUAL_REPORT/env_$project.sh" --selection "$VIRTUAL_REPORT/ids_$project.json"
    source "$REPORT/env_$project.sh"
    FLAGS=(--no-graph --task-ids "$XREPO_TASK_IDS" --rounds "$XREPO_ROUNDS" --attempts "$XREPO_ATTEMPTS")
    if [[ -n "$XREPO_REUSE_ANALYSIS_FROM" ]]; then FLAGS+=(--reuse-analysis-from "$XREPO_REUSE_ANALYSIS_FROM"); fi
    RUNTIME=(--env "OLLAMA_CTX=$OLLAMA_CTX")
    for key in TRANSFORMER_PATH MARTA_MAX_CONTEXT_CHARS; do
        if [[ -n "${!key:-}" ]]; then RUNTIME+=(--env "$key=${!key}"); fi
    done
    "${C[@]}" --bind "$XROOT/python:/opt/conda/envs/test4py_env:ro" \
        --bind "$BASE/pydeps/marta:/data/pydeps/marta:ro" \
        --env PYTHONPATH=/data/pydeps/marta:/opt/marta "${RUNTIME[@]}" "$IMAGE" \
        /opt/conda/envs/test4py_env/bin/python -B -m benchmark.xrepotest.run \
        --validate-only --dataset /app/xrepotest/ruby_functions.jsonl \
        --preflight /data/xrepo/reports/preflight.json \
        --output "/data/xrepo/runs/project_validation_$project/generation" \
        --work "/data/xrepo/runs/project_validation_$project/work" \
        --model "$MODEL" --model-digest 096fdbd02fe620fc10cbeb6537e080f8041aece851e5d696aed024d4f70f2e47 \
        --thinking "$XREPO_THINKING" --max-tokens "$XREPO_MAX_TOKENS" \
        --temperature "$XREPO_TEMPERATURE" --top-p "$XREPO_TOP_P" \
        --presence-penalty "$XREPO_PRESENCE_PENALTY" --request-timeout "$XREPO_REQUEST_TIMEOUT" \
        "${FLAGS[@]}" > "$REPORT/config_$project.json"
    "${C[@]}" "$IMAGE" python3 -B "$HELPER" check-config --project "$project" \
        --candidate "$VIRTUAL_REPORT/config_$project.json" --report "$VIRTUAL_REPORT/check_$project.json"
done
"${C[@]}" "$IMAGE" python3 -B "$HELPER" certify --checks-dir "$VIRTUAL_REPORT" \
    --report "$VIRTUAL_REPORT/validation.json"
echo "All ten project partitions match the frozen runner exactly. 97 IDs, unchanged context and parameters."
echo "Validation only: serial job continues; no inference, cancellation or result copies. Reports: $REPORT"
