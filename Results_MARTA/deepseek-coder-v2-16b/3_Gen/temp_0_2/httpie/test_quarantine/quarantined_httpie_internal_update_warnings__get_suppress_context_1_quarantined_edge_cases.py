
from unittest import TestCase, mock
from contextlib import nullcontext, suppress
from httpie.internal.update_warnings import _get_suppress_context
from httpie.core.environment import Environment

class TestGetSuppressContext(TestCase):
    def test_edge_cases(self):
        # Test when developer mode is enabled
        with mock.patch('httpie.internal.update_warnings._get_suppress_context') as mock_func:
            env = Environment(config={'developer_mode': True})
            ctx_mgr = _get_suppress_context(env)
            self.assertIsInstance(ctx_mgr, nullcontext)
            # Since developer mode is enabled, the context manager should be a no-op

        # Test when developer mode is disabled
        with mock.patch('httpie.internal.update_warnings._get_suppress_context') as mock_func:
            env = Environment(config={'developer_mode': False})
            ctx_mgr = _get_suppress_context(env)
            self.assertIsInstance(ctx_mgr, suppress)
            # Since developer mode is disabled, the context manager should suppress BaseException errors

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_internal_update_warnings__get_suppress_context_1_test_edge_cases
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_update_warnings__get_suppress_context_1_test_edge_cases.py:5:0: E0401: Unable to import 'httpie.core.environment' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_update_warnings__get_suppress_context_1_test_edge_cases.py:5:0: E0611: No name 'environment' in module 'httpie.core' (no-name-in-module)


"""