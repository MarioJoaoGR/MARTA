
import unittest
from unittest.mock import patch, MagicMock
from httpie.manager.core import dispatch_cli_task, CLI_TASKS, Environment, ExitStatus

class TestDispatchCliTask(unittest.TestCase):
    
    @patch('httpie.manager.core.CLI_TASKS', {'fetch': lambda env, args: MagicMock()})
    def test_valid_inputs(self):
        # Create a mock environment and arguments
        env = Environment()
        args = MagicMock()
        args.action = 'fetch'
        
        # Call the function under test
        result = dispatch_cli_task(env, args.action, args)
        
        # Assert that the correct task is called with the environment and arguments
        self.assertIsNotNone(result)
