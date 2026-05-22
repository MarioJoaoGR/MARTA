
import pytest
from unittest.mock import patch
from httpie.manager.core import dispatch_cli_task, CLI_TASKS, parser, ExitStatus
from argparse import Namespace
from httpie.manager.environment import Environment

def test_dispatch_cli_task_missing_action():
    env = Environment()
    args = Namespace()
    
    with pytest.raises(SystemExit) as cm:
        dispatch_cli_task(env, None, args)
    
    assert str(cm.value) == "error: no such option: ''"

def test_dispatch_cli_task_valid_action():
    env = Environment()
    args = Namespace(action='fetch')
    
    with patch('httpie.manager.core.parser'):
        result = dispatch_cli_task(env, 'fetch', args)
        
    assert result == CLI_TASKS['fetch'](env, args)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_manager_core_dispatch_cli_task_0_test_edge_cases
httpie/Test4DT_tests_codestral/test_httpie_manager_core_dispatch_cli_task_0_test_edge_cases.py:6:0: E0401: Unable to import 'httpie.manager.environment' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_manager_core_dispatch_cli_task_0_test_edge_cases.py:6:0: E0611: No name 'environment' in module 'httpie.manager' (no-name-in-module)


"""