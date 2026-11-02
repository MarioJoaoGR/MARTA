# Coverage reporting when application code calls exit

12 October 2026: no-graph generation stopped in Dotenv task 158. Job 2002727
ended near its walltime with exit 15; the chained job 2003122 stopped during
coverage feedback. There were 12 complete tasks, one no_tests, one running,
no processed export and no final evaluation. A queue with no jobs did not mean
this ablation was complete.

The old helper reproduced the exact symptom in repaired-v2 Docker, offline:
four passing RSpec examples followed by `Dotenv::CLI.new(["--version"])`
produced `dotenv 3.2.0`, five examples, zero failures, exit 0, and no JSON.
Dotenv prints its version then calls exit. SystemExit propagates out of the
RSpec runner, so the instruction after Runner.run was never reached.

The generic repair wraps RSpec::Core::Runner.run in begin/ensure. The ensure
emits the already collected coverage through the existing protected IO. It
neither rescues SystemExit nor changes the application's exit status. There
are no Dotenv-specific rules, prompts, source edits or generated-test edits.
Minitest's path and the final XRepoTest evaluator are unchanged.

CPU regressions in the existing image compare an application exit caught by a
test with the same exit propagated through RSpec: lines, branches and method
hits are equal, for exit 0 and exit 7, and the subprocess preserves each status.
The three existing RSpec stdout reopen/replace/close regressions also pass.
No packages or models were installed. Twelve migration tests pass in the
existing venv. These fixtures reproduce the failure mechanism; the actual
saved Deucalion suite has not been downloaded or replayed locally.

The saved generation has a strict code fingerprint. The new migration accepts
only its exact preceding ablation code (17c7de78...), exact repaired code,
no_graph=true and the fixed 97-task selection digest. It takes both generation
locks, hashes every saved file and changes only marta_code in experiment.json.
coverage_system_exit_upgrade.json records the manifests and preserved-file
hashes. Completed tasks and summaries are not regenerated. If GPU generation
is later resumed, the existing policy archives/restarts only running tasks.
Other exported runs are not migrated or re-evaluated by this procedure.

CPU preparation only:

```bash
(
set -e
cd /projects/F202407648IACDCF2/mario/MARTA-ablation
test "$(git branch --show-current)" = codex/ablation-options
git pull --ff-only
export MARTA_CLUSTER_BASE=/projects/F202407648IACDCF2/mario
export MARTA_CLUSTER_CODE="$PWD"
mkdir -p logs
sbatch --parsable --export=ALL deucalion/run_xrepotest_exit_prepare_cpu.sh
)
```

This does not resume the GPU job. With the reported remaining quota of 11 GPU
hours, resumption and the official XRepoTest comparison still require a budget
decision. Thirteen of 97 tasks are finished; 84 remain unfinished. There is no
basis for claiming the remaining no-graph analysis and generation fit in 11h.
