
import unittest.mock as mock
from httpie.internal.update_warnings import _get_suppress_context
from contextlib import nullcontext, suppress
from httpie.environment import Environment

def test_valid_inputs():
    # Test when developer mode is enabled
    with mock.patch('httpie.environment.Environment.config', {'developer_mode': True}):
        env = Environment()
        ctx_mgr = _get_suppress_context(env)
        assert isinstance(ctx_mgr, nullcontext)
    
    # Test when developer mode is disabled
    with mock.patch('httpie.environment.Environment.config', {'developer_mode': False}):
        env = Environment()
        ctx_mgr = _get_suppress_context(env)
        assert isinstance(ctx_mgr, suppress)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_internal_update_warnings__get_suppress_context_0_test_valid_inputs
httpie/Test4DT_tests_codestral/test_httpie_internal_update_warnings__get_suppress_context_0_test_valid_inputs.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_internal_update_warnings__get_suppress_context_0_test_valid_inputs.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)


"""