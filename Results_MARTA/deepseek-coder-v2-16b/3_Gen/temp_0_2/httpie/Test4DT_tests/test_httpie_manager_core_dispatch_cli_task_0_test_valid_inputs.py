
import unittest
from unittest.mock import patch, MagicMock
from httpie.manager.core import dispatch_cli_task
from argparse import Namespace
from enum import Enum

class Environment:
    pass

class ExitStatus(Enum):
    SUCCESS = 0

CLI_TASKS = {
    'fetch': lambda env, args: ExitStatus.SUCCESS
}

def missing_subcommand(cmd):
    return f"Missing subcommand '{cmd}'."

class TestDispatchCliTask(unittest.TestCase):
    
    @patch('httpie.manager.core.parser')
    def test_dispatch_cli_task_with_valid_action(self, mock_parser):
        env = Environment()
        args = Namespace(action='fetch', other_arg='value')
        
        with patch('httpie.manager.core.CLI_TASKS', CLI_TASKS):
            result = dispatch_cli_task(env, 'fetch', args)
            
            self.assertEqual(result, ExitStatus.SUCCESS)
    
    @patch('httpie.manager.core.parser')
    def test_dispatch_cli_task_with_none_action(self, mock_parser):
        env = Environment()
        args = Namespace(action=None)
        
        with patch('httpie.manager.core.CLI_TASKS', CLI_TASKS):
            mock_parser.error = MagicMock(side_effect=ValueError("Action is None"))
            with self.assertRaises(ValueError):
                dispatch_cli_task(env, None, args)
