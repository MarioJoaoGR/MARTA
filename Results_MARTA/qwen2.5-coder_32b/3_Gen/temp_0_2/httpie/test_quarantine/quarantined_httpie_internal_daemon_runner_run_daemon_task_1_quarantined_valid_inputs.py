
import pytest
from httpie.internal.daemon_runner import run_daemon_task
from httpie.environment import Environment
from httpie.constants import ExitStatus, DAEMONIZED_TASKS
from unittest.mock import patch
from io import StringIO
import sys

@pytest.fixture
def env():
    return Environment(config={'developer_mode': False})

def test_run_daemon_task_valid_inputs(env):
    with patch('sys.stdout', new=StringIO()) as mock_stdout, \
         patch('sys.stderr', new=StringIO()) as mock_stderr:
        result = run_daemon_task(env, ['--daemon', '1234'])
        assert result == ExitStatus.SUCCESS
        # Add assertions to check if stdout and stderr are suppressed based on developer mode

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_internal_daemon_runner_run_daemon_task_1_test_valid_inputs
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemon_runner_run_daemon_task_1_test_valid_inputs.py:4:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemon_runner_run_daemon_task_1_test_valid_inputs.py:4:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemon_runner_run_daemon_task_1_test_valid_inputs.py:5:0: E0401: Unable to import 'httpie.constants' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_daemon_runner_run_daemon_task_1_test_valid_inputs.py:5:0: E0611: No name 'constants' in module 'httpie' (no-name-in-module)


"""