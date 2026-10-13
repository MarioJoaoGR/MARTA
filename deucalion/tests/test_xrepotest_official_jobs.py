"""Check the actual Slurm shell orchestration using fake external commands."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest

from deucalion.xrepotest_official_generate import MODES

CODE = Path(__file__).resolve().parents[2]
COHORT = 'qwen36_35b_xrepotest_contexts_thinking_v1'


class OfficialJobTests(unittest.TestCase):
    def test_gpu_modes_have_separate_outputs_and_one_shared_server(self):
        self.check_jobs('gpu')

    def test_cpu_modes_have_same_prompts_and_no_gpu_allocation(self):
        self.check_jobs('cpu')

    def test_one_cpu_context_mode_runs_only_its_675_prompt_stream(self):
        self.check_jobs('cpu', single_mode='file_context')

    def test_different_cpu_modes_can_run_together_but_duplicates_and_all_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            binaries = root / 'bin'
            binaries.mkdir()
            markers = root / 'markers'
            markers.mkdir()
            fake = binaries / 'fake'
            fake.write_text('#!' + sys.executable + '\n' + r"""
import fcntl, os, sys, time
from pathlib import Path
name = Path(sys.argv[0]).name
if name == 'flock':
    flag = fcntl.LOCK_SH if 's' in sys.argv[1] else fcntl.LOCK_EX
    try:
        fcntl.flock(int(sys.argv[-1]), flag | fcntl.LOCK_NB)
    except BlockingIOError:
        sys.exit(1)
if name == 'curl':
    print('{"version":"0.30.7"}')
if name == 'singularity':
    if sys.argv[-2:] == ['ollama', 'serve']:
        while True:
            time.sleep(0.05)
    if 'xrepotest_official_generate.py' in ' '.join(sys.argv) and '--output' in sys.argv:
        markers = Path(os.environ['TEST_MARKERS'])
        mode = sys.argv[sys.argv.index('--mode') + 1]
        (markers / mode).write_text('active')
        while not (markers / 'stop').exists():
            time.sleep(0.05)
""")
            fake.chmod(0o755)
            for name in ('singularity', 'curl', 'scontrol', 'flock'):
                (binaries / name).symlink_to(fake)
            cohort = 'qwen36_35b_xrepotest_contexts_thinking_cpu_threads8_v2'
            run = root / 'xrepotest/runs' / cohort
            for mode in MODES:
                path = run / 'modes' / mode / 'metadata/official_preflight.json'
                path.parent.mkdir(parents=True)
                path.write_text('{}')
            env = dict(os.environ, MARTA_CLUSTER_BASE=str(root), MARTA_CLUSTER_CODE=str(CODE),
                       XREPO_RUN=cohort, XREPO_CPU_CHAIN='0', SLURM_GPUS_ON_NODE='0',
                       XREPO_OFFICIAL_CTX='32768', TEST_MARKERS=str(markers),
                       PATH=str(binaries) + ':' + os.environ['PATH'])
            script = CODE / 'deucalion/run_xrepotest_official_generate_cpu.sh'
            workers = []
            try:
                for number, mode in enumerate(('standard', 'file_context')):
                    worker = subprocess.Popen(['bash', str(script)],
                        env=dict(env, XREPO_OFFICIAL_MODE=mode, SLURM_JOB_ID=str(12000 + number)),
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    workers.append(worker)
                    end = time.monotonic() + 10
                    while not (markers / mode).exists() and time.monotonic() < end and worker.poll() is None:
                        time.sleep(0.02)
                    if not (markers / mode).exists():
                        worker.terminate()
                        out, err = worker.communicate(timeout=10)
                        self.fail('Worker did not start generation: ' + out + err)
                    self.assertIsNone(worker.poll())
                # Real inherited file locks are used, not a stub that always succeeds.
                for mode in ('standard', 'file_context', 'all'):
                    denied = subprocess.run(['bash', str(script)],
                        env=dict(env, XREPO_OFFICIAL_MODE=mode, SLURM_JOB_ID='13000'),
                        capture_output=True, text=True, timeout=10)
                    self.assertEqual(denied.returncode, 2, denied.stdout + denied.stderr)
                    self.assertIn('already running', denied.stdout)
                (markers / 'stop').touch()
                for worker in workers:
                    out, err = worker.communicate(timeout=10)
                    self.assertEqual(worker.returncode, 0, out + err)
            finally:
                (markers / 'stop').touch()
                for worker in workers:
                    if worker.poll() is None:
                        worker.terminate()
                    worker.communicate(timeout=10)

    def check_jobs(self, backend, single_mode=None):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            binaries = root / 'bin'
            binaries.mkdir()
            log = root / 'commands.jsonl'
            fake = binaries / 'fake'
            fake.write_text('#!' + sys.executable + '\n' + r"""
import json, os, sys, time
from pathlib import Path
name = Path(sys.argv[0]).name
with open(os.environ['FAKE_COMMAND_LOG'], 'a') as out:
    out.write(json.dumps([name] + sys.argv[1:]) + '\n')
if name == 'singularity' and sys.argv[-2:] == ['ollama', 'serve']:
    while True:
        time.sleep(1)
if name == 'curl':
    print('{"version":"0.30.7"}')
""")
            fake.chmod(0o755)
            for name in ('singularity', 'curl', 'ml', 'scontrol', 'flock'):
                (binaries / name).symlink_to(fake)
            cohort = COHORT if backend == 'gpu' else 'qwen36_35b_xrepotest_contexts_thinking_cpu_threads8_v2'
            run = root / 'xrepotest/runs' / cohort
            for mode in MODES:
                preflight = run / 'modes' / mode / 'metadata/official_preflight.json'
                preflight.parent.mkdir(parents=True)
                preflight.write_text('{}')
                complete = run / 'modes' / mode / 'generation/complete.json'
                complete.parent.mkdir(parents=True)
                complete.write_text('{}')
            env = dict(os.environ, MARTA_CLUSTER_BASE=str(root), MARTA_CLUSTER_CODE=str(CODE),
                       XREPO_RUN=cohort, XREPO_OFFICIAL_MODE=single_mode or 'all', XREPO_CPU_CHAIN='0', SLURM_GPUS_ON_NODE='0', XREPO_OFFICIAL_CTX='32768', SLURM_JOB_ID='12345',
                       XREPO_TASK_IDS='stale-selection-must-not-be-used',
                       FAKE_COMMAND_LOG=str(log), PATH=str(binaries) + ':' + os.environ['PATH'])
            for phase in ('prepare_cpu', 'generate_' + backend, 'evaluate_cpu'):
                script = CODE / 'deucalion' / ('run_xrepotest_official_' + phase + '.sh')
                subprocess.run(['bash', '-n', str(script)], check=True)
                completed = subprocess.run(['bash', str(script)], env=env, text=True,
                                           capture_output=True, timeout=20)
                self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            commands = [json.loads(line) for line in log.read_text().splitlines()]
            servers = [c for c in commands if c[-2:] == ['ollama', 'serve']]
            self.assertEqual(len(servers), 1)
            self.assertIn('OLLAMA_CONTEXT_LENGTH=32768', servers[0])
            if backend == 'cpu':
                self.assertNotIn('--nv', servers[0])
                self.assertIn('CUDA_VISIBLE_DEVICES=-1', servers[0])
                self.assertIn('LLAMA_ARG_THREADS=8', servers[0])
                self.assertIn('ROCR_VISIBLE_DEVICES=-1', servers[0])
                script = CODE / 'deucalion/run_xrepotest_official_generate_cpu.sh'
                self.assertIn('#SBATCH --account=f202407648iacdcf2x', script.read_text())
                self.assertNotIn('#SBATCH --gpus', script.read_text())
                self.assertEqual(len([c for c in commands if 'verify_ollama_cpu.py' in ' '.join(c)]), 1)
                self.assertFalse(any(c[0] == 'ml' for c in commands))
            generations = [c for c in commands if 'xrepotest_official_generate.py' in ' '.join(c)
                           and '--output' in c]
            expected_modes = [single_mode] if single_mode else list(MODES)
            self.assertEqual(len(generations), len(expected_modes))
            self.assertEqual([c[c.index('--mode') + 1] for c in generations], expected_modes)
            self.assertTrue(all(c[c.index('--context-length') + 1] == '32768' for c in generations))
            self.assertEqual(len({c[c.index('--output') + 1] for c in generations}), len(expected_modes))
            if backend == 'cpu':
                self.assertTrue(all(c[c.index('--backend') + 1] == 'cpu' for c in generations))
                self.assertTrue(all('--cpu-proof' in c for c in generations))
            evaluations = [c for c in commands if 'benchmark.xrepotest.evaluate' in c]
            self.assertEqual(len(evaluations), 5)
            for mode, command in zip(MODES, evaluations):
                self.assertNotIn('--task-ids', command)
                self.assertNotIn('--mutation', command)
                self.assertIn('/modes/' + mode + '/generation/processed.jsonl',
                              command[command.index('--processed') + 1])
                self.assertNotIn('\\', command)
            bad_env = dict(env, XREPO_OFFICIAL_CTX='65536')
            for phase in ('prepare_cpu', 'generate_' + backend):
                rejected = subprocess.run(['bash', str(CODE / 'deucalion' /
                    ('run_xrepotest_official_' + phase + '.sh'))], env=bad_env,
                    text=True, capture_output=True, timeout=20)
                self.assertEqual(rejected.returncode, 2)
                self.assertIn('Context must match MARTA', rejected.stdout)
            preflights = [c for c in commands if '--preflight-output' in c]
            self.assertEqual(len(preflights), 5)


if __name__ == '__main__':
    unittest.main()
