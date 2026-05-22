
import pytest
from httpie.plugins.builtin import HTTPBasicAuth
from base64 import b64encode

def test_none_inputs():
    with pytest.raises(TypeError):
        HTTPBasicAuth().make_header(None, None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_plugins_builtin_HTTPBasicAuth_make_header_1_test_none_inputs
httpie/Test4DT_tests_codestral/test_httpie_plugins_builtin_HTTPBasicAuth_make_header_1_test_none_inputs.py:8:8: E1120: No value for argument 'username' in constructor call (no-value-for-parameter)
httpie/Test4DT_tests_codestral/test_httpie_plugins_builtin_HTTPBasicAuth_make_header_1_test_none_inputs.py:8:8: E1120: No value for argument 'password' in constructor call (no-value-for-parameter)


"""