
import unittest
from unittest.mock import patch, nullcontext
from httpie.core.environment import Environment
from contextlib import suppress

class TestHttpieInternalUpdateWarnings(unittest.TestCase):
    @patch('httpie.core.environment.Environment')
    def test_get_suppress_context_developer_mode_enabled(self, MockEnvClass):
        # Arrange
        env = MockEnvClass.return_value
        env.config.developer_mode = True
        
        # Act
        ctx_mgr = _get_suppress_context(env)
        
        # Assert
        self.assertIsInstance(ctx_mgr, nullcontext)
    
    @patch('httpie.core.environment.Environment')
    def test_get_suppress_context_developer_mode_disabled(self, MockEnvClass):
        # Arrange
        env = MockEnvClass.return_value
        env.config.developer_mode = False
        
        # Act
        ctx_mgr = _get_suppress_context(env)
        
        # Assert
        self.assertIsInstance(ctx_mgr, suppress)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_internal_update_warnings__get_suppress_context_0_test_valid_input_happy_path
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_update_warnings__get_suppress_context_0_test_valid_input_happy_path.py:3:0: E0611: No name 'nullcontext' in module 'unittest.mock' (no-name-in-module)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_update_warnings__get_suppress_context_0_test_valid_input_happy_path.py:4:0: E0401: Unable to import 'httpie.core.environment' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_update_warnings__get_suppress_context_0_test_valid_input_happy_path.py:4:0: E0611: No name 'environment' in module 'httpie.core' (no-name-in-module)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_update_warnings__get_suppress_context_0_test_valid_input_happy_path.py:15:18: E0602: Undefined variable '_get_suppress_context' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_update_warnings__get_suppress_context_0_test_valid_input_happy_path.py:27:18: E0602: Undefined variable '_get_suppress_context' (undefined-variable)


"""