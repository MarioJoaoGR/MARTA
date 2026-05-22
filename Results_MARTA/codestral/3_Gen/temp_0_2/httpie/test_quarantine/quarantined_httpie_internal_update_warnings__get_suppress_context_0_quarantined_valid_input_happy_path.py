
import unittest
from unittest.mock import patch, nullcontext
from httpie.core.environment import Environment
from contextlib import suppress

class TestGetSuppressContext(unittest.TestCase):
    @patch('httpie.core.environment.Environment')
    def test_valid_input_happy_path(self, MockEnv):
        # Create a mock environment with developer mode disabled
        env = MockEnv()
        env.config.developer_mode = False
        
        # Call the function under test
        ctx_mgr = _get_suppress_context(env)
        
        # Check that it returns a context manager that suppresses BaseException errors
        with self.subTest("Check suppress context for non-developer mode"):
            with ctx_mgr:
                raise ValueError("Test Error")  # This should be suppressed

        # Create another mock environment with developer mode enabled
        env = MockEnv()
        env.config.developer_mode = True
        
        # Call the function under test again
        ctx_mgr = _get_suppress_context(env)
        
        # Check that it returns a no-op context manager when developer mode is enabled
        with self.subTest("Check no-op context for developer mode"):
            with ctx_mgr:
                pass  # No error should be raised

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_internal_update_warnings__get_suppress_context_0_test_valid_input_happy_path
httpie/Test4DT_tests_codestral/test_httpie_internal_update_warnings__get_suppress_context_0_test_valid_input_happy_path.py:3:0: E0611: No name 'nullcontext' in module 'unittest.mock' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_internal_update_warnings__get_suppress_context_0_test_valid_input_happy_path.py:4:0: E0401: Unable to import 'httpie.core.environment' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_internal_update_warnings__get_suppress_context_0_test_valid_input_happy_path.py:4:0: E0611: No name 'environment' in module 'httpie.core' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_internal_update_warnings__get_suppress_context_0_test_valid_input_happy_path.py:15:18: E0602: Undefined variable '_get_suppress_context' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_internal_update_warnings__get_suppress_context_0_test_valid_input_happy_path.py:27:18: E0602: Undefined variable '_get_suppress_context' (undefined-variable)


"""