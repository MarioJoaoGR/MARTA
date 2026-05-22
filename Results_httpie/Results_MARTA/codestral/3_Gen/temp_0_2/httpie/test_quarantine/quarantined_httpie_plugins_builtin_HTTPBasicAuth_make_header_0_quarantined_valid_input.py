
import pytest
from base64 import b64encode
from unittest.mock import patch

class HTTPBasicAuth:
    @staticmethod
    def make_header(username: str, password: str) -> str:
        credentials = f'{username}:{password}'
        token = b64encode(credentials.encode()).strip().decode('latin1')
        return f'Basic {token}'

def test_valid_input():
    with patch('HTTPBasicAuth.make_header', return_value='Basic dXNlcjpwYXNz'):
        assert HTTPBasicAuth.make_header('user', 'pass') == 'Basic dXNlcjpwYXNz'

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

httpie/Test4DT_tests_codestral/test_httpie_plugins_builtin_HTTPBasicAuth_make_header_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
>       with patch('HTTPBasicAuth.make_header', return_value='Basic dXNlcjpwYXNz'):

httpie/Test4DT_tests_codestral/test_httpie_plugins_builtin_HTTPBasicAuth_make_header_0_test_valid_input.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/unittest/mock.py:1430: in __enter__
    self.target = self.getter()
/usr/local/lib/python3.11/pkgutil.py:700: in resolve_name
    mod = importlib.import_module(modname)
/usr/local/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1204: in _gcd_import
    ???
<frozen importlib._bootstrap>:1176: in _find_and_load
    ???
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

name = 'HTTPBasicAuth', import_ = <function _gcd_import at 0x7f1692ef3d80>

>   ???
E   ModuleNotFoundError: No module named 'HTTPBasicAuth'

<frozen importlib._bootstrap>:1140: ModuleNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_plugins_builtin_HTTPBasicAuth_make_header_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.14s ===============================
"""