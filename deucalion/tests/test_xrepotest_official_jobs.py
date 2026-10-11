"""Check the actual Slurm shell orchestration using fake external commands."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from deucalion.xrepotest_official_generate import MODES

CODE = Path(__file__).resolve().parents[2]
COHORT = 'qwen36_35b_xrepotest_contexts_thinking_v1'


class OfficialJobTests(unittest.TestCase):
    def test_all_modes_have_separate_outputs_and_one_shared_server(self):
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
            run = root / 'xrepotest/runs' / COHORT
            for mode in MODES:
                preflight = run / 'modes' / mode / 'metadata/official_preflight.json'
                preflight.parent.mkdir(parents=True)
                preflight.write_text('{}')
                complete = run / 'modes' / mode / 'generation/complete.json'
                complete.parent.mkdir(parents=True)
                complete.write_text('{}')
            env = dict(os.environ, MARTA_CLUSTER_BASE=str(root), MARTA_CLUSTER_CODE=str(CODE),
                       XREPO_RUN=COHORT, XREPO_OFFICIAL_CTX='65536', SLURM_JOB_ID='12345',
                       XREPO_TASK_IDS='stale-selection-must-not-be-used',
                       FAKE_COMMAND_LOG=str(log), PATH=str(binaries) + ':' + os.environ['PATH'])
            for phase in ('prepare_cpu', 'generate_gpu', 'evaluate_cpu'):
                script = CODE / 'deucalion' / ('run_xrepotest_official_' + phase + '.sh')
                subprocess.run(['bash', '-n', str(script)], check=True)
                completed = subprocess.run(['bash', str(script)], env=env, text=True,
                                           capture_output=True, timeout=20)
                self.assertEqual(completed.returncode, 0, completed.stderr + completed.stdout)
            commands = [json.loads(line) for line in log.read_text().splitlines()]
            servers = [c for c in commands if c[-2:] == ['ollama', 'serve']]
            self.assertEqual(len(servers), 1)
            self.assertIn('OLLAMA_CONTEXT_LENGTH=65536', servers[0])
            generations = [c for c in commands if 'xrepotest_official_generate.py' in ' '.join(c)
                           and '--output' in c]
            self.assertEqual(len(generations), 5)
            self.assertEqual([c[c.index('--mode') + 1] for c in generations], list(MODES))
            self.assertTrue(all(c[c.index('--context-length') + 1] == '65536' for c in generations))
            self.assertEqual(len({c[c.index('--output') + 1] for c in generations}), 5)
            evaluations = [c for c in commands if 'benchmark.xrepotest.evaluate' in c]
            self.assertEqual(len(evaluations), 5)
            for mode, command in zip(MODES, evaluations):
                self.assertNotIn('--task-ids', command)
                self.assertNotIn('--mutation', command)
                self.assertIn('/modes/' + mode + '/generation/processed.jsonl',
                              command[command.index('--processed') + 1])
                self.assertNotIn('\\', command)
            preflights = [c for c in commands if '--preflight-output' in c]
            self.assertEqual(len(preflights), 5)


if __name__ == '__main__':
    unittest.main()
