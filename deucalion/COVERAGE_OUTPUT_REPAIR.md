# Recovery after redirected coverage output

On 6 October 2026, job 1983841 stopped in MARTA's internal coverage feedback
for task 376 (`Shoryuken::Runner#daemonize`). The run had 651 finished tasks
(497 `complete`, 154 `no_tests`) and task 376 was still `running`.

The saved round-1 suite passed all three RSpec examples. Its first example
mocked `Process.daemon` but allowed the source method to reopen `$stdout` and
`$stderr` onto its temporary logfile. MARTA's coverage helper subsequently
wrote its JSON through `$stdout`, so Python received empty stdout and stderr.
This is an output transport failure, not evidence of zero coverage.

## Repair and validation

`marta/ruby_backend/rb/marta_coverage.rb` duplicates the original stdout IO
before loading application code. RSpec and Minitest coverage callbacks write
and flush their report through that saved IO. The application still sees its
own redirected, replaced or closed stdout. Coverage collection, synthesis,
prompts, attempt limits and the final XRepoTest evaluator are unchanged.

The exact supplied suite was reproduced in `marta-xrepotest:repaired-v2`,
offline and without LLM calls, on a disposable copy of the pinned Shoryuken:

- Before: all three RSpec examples passed; coverage raised the same empty
  non-JSON error as Deucalion.
- After: all three examples passed; the helper returned a valid report with
  `lib/shoryuken/runner.rb` present.
- Fixture SHA256:
  `51f02b32fc8775cd6a3c1f218827e7274920af2c70da1f50884d0543cb718ae1`.
- Regression tests compare the same application coverage with normal output
  and with stdout reopened, replaced by StringIO, or closed, under both RSpec
  and Minitest. Lines, branches and method counts must match.

The diagnostic fixture and before/after outputs live outside the repository
in `~/.cache/marta-xrepotest/coverage-report-repair/`.

## Audited continuation

The helper change changes the experiment fingerprint. The migration
`deucalion/upgrade_xrepotest_coverage_output.py` accepts only the exact old
fingerprint and exact repaired code. It obtains the wrapper and runner locks,
validates task states and summary checkpoints, records hashes of all saved
files (including interrupted history), and changes only `marta_code` in
`experiment.json`. The old and new manifests remain in
`coverage_output_upgrade.json`. Exported runs are refused.

The existing restart policy remains in force: all `complete` and `no_tests`
tasks are skipped; the unfinished task 376 is archived and generated again.
The failed attempt's suite, events and cost remain in `interrupted_tasks/`.
The diagnostic suite is not imported into the experiment. No completed task
is regenerated or selected again for a better score.

Run only after the generation job has stopped:

```bash
(
set -e
cd /projects/F202407648IACDCF2/mario/MARTA
git pull --ff-only

export XREPO_RUN=qwen36_35b_thinking_bundle_loading_v4
XROOT=/projects/F202407648IACDCF2/mario/xrepotest

GOMAXPROCS=2 singularity exec --cleanenv \
  --home "$XROOT/runs/$XREPO_RUN/home:/home/marta" \
  --bind "$PWD:/opt/marta:ro" \
  --bind "$XROOT:/data/xrepo" \
  --env PYTHONPATH=/opt/marta \
  --env GOMAXPROCS=2 \
  "$XROOT/repaired-v2.sif" \
  python3 -B /opt/marta/deucalion/upgrade_xrepotest_coverage_output.py \
  "/data/xrepo/runs/$XREPO_RUN/generation"

export MODEL=qwen3.6:35b XREPO_THINKING=on
export OLLAMA_CTX=32768 XREPO_MAX_TOKENS=16384
export XREPO_TEMPERATURE=0.6 XREPO_TOP_P=0.95
export XREPO_PRESENCE_PENALTY=0
export XREPO_REQUEST_TIMEOUT=1800 XREPO_NO_GRAPH=0

mkdir -p logs
sbatch --parsable --export=ALL deucalion/run_xrepotest_generate_gpu.sh
)
```

The fingerprint is intentionally strict. The separate ablation branch must
incorporate this helper repair before a future experiment; this migration
does not accept an ablation configuration or another code revision.
