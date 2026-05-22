
import pytest
from unittest.mock import patch
from httpie.internal.daemon_runner import run_daemon_task, ExitStatus, DAEMONIZED_TASKS
from httpie.environment import Environment

def test_valid_inputs():
    # Test with developer mode enabled
    env = Environment(config={'developer_mode': True})
    result = run_daemon_task(env, ['--daemon', '1234'])
    assert result == ExitStatus.SUCCESS

    # Test with developer mode disabled
    env = Environment(config={'developer_mode': False})
    result = run_daemon_task(env, ['--daemon', '1234'])
    assert result == ExitStatus.SUCCESS

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_internal_daemon_runner_run_daemon_task_0_test_valid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_daemon_runner_run_daemon_task_0_test_valid_inputs.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_daemon_runner_run_daemon_task_0_test_valid_inputs.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)


"""