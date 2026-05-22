
import unittest
from httpie.manager.__main__ import program
from environment import Environment
from exit_status import ExitStatus

class TestProgram(unittest.TestCase):
    
    def test_program_default(self):
        with unittest.mock.patch('sys.argv', ['httpie']):
            env = Environment()
            result = program(env=env)
            self.assertEqual(result, ExitStatus.SUCCESS)

    def test_program_with_option(self):
        with unittest.mock.patch('sys.argv', ['httpie', '--option', 'value']):
            env = Environment()
            result = program(env=env)
            self.assertEqual(result, ExitStatus.SUCCESS)

    def test_program_with_keyboard_interrupt(self):
        with unittest.mock.patch('sys.argv', ['httpie']), \
             unittest.mock.patch('builtins.input', side_effect=['y']):
            env = Environment()
            result = program(env=env)
            self.assertEqual(result, ExitStatus.ERROR_CTRL_C)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_manager___main___program_0_test_edge_cases
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager___main___program_0_test_edge_cases.py:4:0: E0401: Unable to import 'environment' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager___main___program_0_test_edge_cases.py:5:0: E0401: Unable to import 'exit_status' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager___main___program_0_test_edge_cases.py:12:21: E1123: Unexpected keyword argument 'env' in function call (unexpected-keyword-arg)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager___main___program_0_test_edge_cases.py:18:21: E1123: Unexpected keyword argument 'env' in function call (unexpected-keyword-arg)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager___main___program_0_test_edge_cases.py:25:21: E1123: Unexpected keyword argument 'env' in function call (unexpected-keyword-arg)


"""