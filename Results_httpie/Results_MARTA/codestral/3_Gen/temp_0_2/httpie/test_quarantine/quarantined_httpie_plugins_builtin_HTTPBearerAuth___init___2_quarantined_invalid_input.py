
import pytest
from httpie.plugins.builtin import HTTPBearerAuth

def test_invalid_input():
    with pytest.raises(TypeError):
        HTTPBearerAuth()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_plugins_builtin_HTTPBearerAuth___init___2_test_invalid_input
httpie/Test4DT_tests_codestral/test_httpie_plugins_builtin_HTTPBearerAuth___init___2_test_invalid_input.py:7:8: E1120: No value for argument 'token' in constructor call (no-value-for-parameter)


"""