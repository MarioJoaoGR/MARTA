
import unittest
from httpie.manager.__main__ import program
from environment import Environment
from exit_status import ExitStatus

class TestProgram(unittest.TestCase):
    
    def test_edge_case(self):
        with unittest.mock.patch('httpie.manager.__main__.sys.argv', ['program']):
            env = Environment()
            result = program(env=env)
            self.assertEqual(result, ExitStatus.SUCCESS)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_manager___main___program_0_test_edge_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager___main___program_0_test_edge_case.py:4:0: E0401: Unable to import 'environment' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager___main___program_0_test_edge_case.py:5:0: E0401: Unable to import 'exit_status' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager___main___program_0_test_edge_case.py:12:21: E1123: Unexpected keyword argument 'env' in function call (unexpected-keyword-arg)


"""