
from httpie.manager.core import dispatch_cli_task, CLI_TASKS, parser, missing_subcommand, ExitStatus
from unittest.mock import patch
import argparse
from httpie.env import Environment

class TestDispatchCliTask:
    @patch('httpie.manager.core.parser')
    def test_missing_action(self, mock_parser):
        env = Environment()
        args = argparse.Namespace(action=None)
        
        with self.assertRaises(SystemExit) as cm:
            dispatch_cli_task(env, args.action, args)
        
        assert str(cm.exception) == missing_subcommand('cli')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_manager_core_dispatch_cli_task_0_test_missing_action
httpie/Test4DT_tests_codestral/test_httpie_manager_core_dispatch_cli_task_0_test_missing_action.py:5:0: E0401: Unable to import 'httpie.env' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_manager_core_dispatch_cli_task_0_test_missing_action.py:5:0: E0611: No name 'env' in module 'httpie' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_manager_core_dispatch_cli_task_0_test_missing_action.py:13:13: E1101: Instance of 'TestDispatchCliTask' has no 'assertRaises' member (no-member)


"""