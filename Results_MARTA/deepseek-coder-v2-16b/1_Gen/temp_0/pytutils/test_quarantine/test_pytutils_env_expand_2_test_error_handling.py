
import os
from pytutils.env import expand
import pytest
from unittest.mock import patch

@pytest.mark.parametrize("input_val, expected", [
    ("$USER/Desktop", "/home/admin/Desktop"),
    ("~/Documents", "/home/user/Documents"),
    ("~", "/home/user"),
    ("$HOME/Projects", "/root/Projects"),
    ("$VAR/test", "$VAR/test")  # Assuming $VAR is not set, so it should remain unchanged
])
@patch('os.environ', {'USER': 'admin', 'HOME': '/home/admin'})
def test_error_handling(input_val, expected):
    with patch('os.environ', {'USER': 'admin', 'HOME': '/home/admin'}):
        assert expand(input_val) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

pytutils/Test4DT_tests/test_pytutils_env_expand_2_test_error_handling.py F [ 20%]
FFF.                                                                     [100%]

=================================== FAILURES ===================================
____________ test_error_handling[$USER/Desktop-/home/admin/Desktop] ____________

input_val = '$USER/Desktop', expected = '/home/admin/Desktop'

    @pytest.mark.parametrize("input_val, expected", [
        ("$USER/Desktop", "/home/admin/Desktop"),
        ("~/Documents", "/home/user/Documents"),
        ("~", "/home/user"),
        ("$HOME/Projects", "/root/Projects"),
        ("$VAR/test", "$VAR/test")  # Assuming $VAR is not set, so it should remain unchanged
    ])
    @patch('os.environ', {'USER': 'admin', 'HOME': '/home/admin'})
    def test_error_handling(input_val, expected):
        with patch('os.environ', {'USER': 'admin', 'HOME': '/home/admin'}):
>           assert expand(input_val) == expected
E           AssertionError: assert 'admin/Desktop' == '/home/admin/Desktop'
E             
E             - /home/admin/Desktop
E             ? ------
E             + admin/Desktop

pytutils/Test4DT_tests/test_pytutils_env_expand_2_test_error_handling.py:17: AssertionError
____________ test_error_handling[~/Documents-/home/user/Documents] _____________

input_val = '~/Documents', expected = '/home/user/Documents'

    @pytest.mark.parametrize("input_val, expected", [
        ("$USER/Desktop", "/home/admin/Desktop"),
        ("~/Documents", "/home/user/Documents"),
        ("~", "/home/user"),
        ("$HOME/Projects", "/root/Projects"),
        ("$VAR/test", "$VAR/test")  # Assuming $VAR is not set, so it should remain unchanged
    ])
    @patch('os.environ', {'USER': 'admin', 'HOME': '/home/admin'})
    def test_error_handling(input_val, expected):
        with patch('os.environ', {'USER': 'admin', 'HOME': '/home/admin'}):
>           assert expand(input_val) == expected
E           AssertionError: assert '/home/admin/Documents' == '/home/user/Documents'
E             
E             - /home/user/Documents
E             ?       ^^^^
E             + /home/admin/Documents
E             ?       ^^^^^

pytutils/Test4DT_tests/test_pytutils_env_expand_2_test_error_handling.py:17: AssertionError
______________________ test_error_handling[~-/home/user] _______________________

input_val = '~', expected = '/home/user'

    @pytest.mark.parametrize("input_val, expected", [
        ("$USER/Desktop", "/home/admin/Desktop"),
        ("~/Documents", "/home/user/Documents"),
        ("~", "/home/user"),
        ("$HOME/Projects", "/root/Projects"),
        ("$VAR/test", "$VAR/test")  # Assuming $VAR is not set, so it should remain unchanged
    ])
    @patch('os.environ', {'USER': 'admin', 'HOME': '/home/admin'})
    def test_error_handling(input_val, expected):
        with patch('os.environ', {'USER': 'admin', 'HOME': '/home/admin'}):
>           assert expand(input_val) == expected
E           AssertionError: assert '/home/admin' == '/home/user'
E             
E             - /home/user
E             + /home/admin

pytutils/Test4DT_tests/test_pytutils_env_expand_2_test_error_handling.py:17: AssertionError
______________ test_error_handling[$HOME/Projects-/root/Projects] ______________

input_val = '$HOME/Projects', expected = '/root/Projects'

    @pytest.mark.parametrize("input_val, expected", [
        ("$USER/Desktop", "/home/admin/Desktop"),
        ("~/Documents", "/home/user/Documents"),
        ("~", "/home/user"),
        ("$HOME/Projects", "/root/Projects"),
        ("$VAR/test", "$VAR/test")  # Assuming $VAR is not set, so it should remain unchanged
    ])
    @patch('os.environ', {'USER': 'admin', 'HOME': '/home/admin'})
    def test_error_handling(input_val, expected):
        with patch('os.environ', {'USER': 'admin', 'HOME': '/home/admin'}):
>           assert expand(input_val) == expected
E           AssertionError: assert '/home/admin/Projects' == '/root/Projects'
E             
E             - /root/Projects
E             + /home/admin/Projects

pytutils/Test4DT_tests/test_pytutils_env_expand_2_test_error_handling.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_env_expand_2_test_error_handling.py::test_error_handling[$USER/Desktop-/home/admin/Desktop]
FAILED pytutils/Test4DT_tests/test_pytutils_env_expand_2_test_error_handling.py::test_error_handling[~/Documents-/home/user/Documents]
FAILED pytutils/Test4DT_tests/test_pytutils_env_expand_2_test_error_handling.py::test_error_handling[~-/home/user]
FAILED pytutils/Test4DT_tests/test_pytutils_env_expand_2_test_error_handling.py::test_error_handling[$HOME/Projects-/root/Projects]
========================= 4 failed, 1 passed in 0.06s ==========================
"""