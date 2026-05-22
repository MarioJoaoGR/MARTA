
import pytest
from httpie.plugins.builtin import HTTPBearerAuth

def test_none_input():
    with pytest.raises(TypeError):
        auth = HTTPBearerAuth()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_plugins_builtin_HTTPBearerAuth___init___0_test_none_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_builtin_HTTPBearerAuth___init___0_test_none_input.py:7:15: E1120: No value for argument 'token' in constructor call (no-value-for-parameter)


"""