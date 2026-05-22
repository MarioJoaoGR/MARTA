
import pytest
from httpie.cli.argtypes import AuthCredentialsArgType

def test_valid_input_username():
    argtype = AuthCredentialsArgType()
    result = argtype("username")
    assert result.key == "username"
    assert result.value is None

    result = argtype("username:password")
    assert result.key == "username"
    assert result.value == "password"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_codestral/test_httpie_cli_argtypes_AuthCredentialsArgType___call___0_test_valid_input_username.py F [100%]

=================================== FAILURES ===================================
__________________________ test_valid_input_username ___________________________

    def test_valid_input_username():
        argtype = AuthCredentialsArgType()
        result = argtype("username")
        assert result.key == "username"
        assert result.value is None
    
        result = argtype("username:password")
>       assert result.key == "username"
E       AssertionError: assert 'username:password' == 'username'
E         
E         - username
E         + username:password

httpie/Test4DT_tests_codestral/test_httpie_cli_argtypes_AuthCredentialsArgType___call___0_test_valid_input_username.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_cli_argtypes_AuthCredentialsArgType___call___0_test_valid_input_username.py::test_valid_input_username
============================== 1 failed in 0.15s ===============================
"""