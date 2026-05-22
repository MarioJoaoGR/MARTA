
import pytest
from httpie.plugins.builtin import HTTPBasicAuth
from base64 import b64encode

def test_empty_inputs():
    with pytest.raises(ValueError):
        HTTPBasicAuth().make_header('', '')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_plugins_builtin_HTTPBasicAuth_make_header_2_test_empty_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_builtin_HTTPBasicAuth_make_header_2_test_empty_inputs.py:8:8: E1120: No value for argument 'username' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_builtin_HTTPBasicAuth_make_header_2_test_empty_inputs.py:8:8: E1120: No value for argument 'password' in constructor call (no-value-for-parameter)


"""