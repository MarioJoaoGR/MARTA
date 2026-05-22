
import unittest
from unittest.mock import patch, nullcontext
from httpie.core.models import Environment
from contextlib import suppress

class TestGetSuppressContext(unittest.TestCase):
    def test_valid_inputs(self):
        # Test when developer mode is enabled
        with patch('httpie.core.models.Environment.config', {'developer_mode': True}):
            env = Environment()
            ctx_mgr = _get_suppress_context(env)
            with self.assertRaises(Exception):  # Since we are not suppressing all exceptions, any exception should be raised
                with ctx_mgr:
                    raise ValueError("Test Error")
        
        # Test when developer mode is disabled
        with patch('httpie.core.models.Environment.config', {'developer_mode': False}):
            env = Environment()
            ctx_mgr = _get_suppress_context(env)
            with suppress(BaseException):  # Suppress BaseException for the context
                with ctx_mgr:
                    raise ValueError("Test Error")  # This should be suppressed

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_internal_update_warnings__get_suppress_context_1_test_valid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_update_warnings__get_suppress_context_1_test_valid_inputs.py:3:0: E0611: No name 'nullcontext' in module 'unittest.mock' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_update_warnings__get_suppress_context_1_test_valid_inputs.py:4:0: E0401: Unable to import 'httpie.core.models' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_update_warnings__get_suppress_context_1_test_valid_inputs.py:4:0: E0611: No name 'models' in module 'httpie.core' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_update_warnings__get_suppress_context_1_test_valid_inputs.py:12:22: E0602: Undefined variable '_get_suppress_context' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_update_warnings__get_suppress_context_1_test_valid_inputs.py:20:22: E0602: Undefined variable '_get_suppress_context' (undefined-variable)


"""