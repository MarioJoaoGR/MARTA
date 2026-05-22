
import unittest.mock as mock
from httpie.context import Environment

class TestEnvironment(unittest.TestCase):
    def test_devnull(self):
        env = Environment()
        
        with mock.patch('os.devnull', create=True) as devnull_mock:
            devnull_mock.__str__.return_value = 'mocked_devnull'
            
            # First call should open the mocked devnull
            self.assertEqual(env.devnull(), 'mocked_devnull')
            
            # Subsequent calls should return the same mocked devnull without opening again
            self.assertEqual(env.devnull(), 'mocked_devnull')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_context_Environment_devnull_1_test_edge_cases
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_context_Environment_devnull_1_test_edge_cases.py:5:22: E0602: Undefined variable 'unittest' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_context_Environment_devnull_1_test_edge_cases.py:13:29: E1102: env.devnull is not callable (not-callable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_context_Environment_devnull_1_test_edge_cases.py:16:29: E1102: env.devnull is not callable (not-callable)


"""