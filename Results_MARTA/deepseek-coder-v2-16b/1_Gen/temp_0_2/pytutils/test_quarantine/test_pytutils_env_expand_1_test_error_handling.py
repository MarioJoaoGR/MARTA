
import pytest
from unittest.mock import patch
import os
from pytutils.env import expand

@pytest.mark.parametrize("input_string, expected", [
    ("~/Documents", "/home/user/Documents"),
    ("$HOME/Projects", "/home/user/Projects"),
    ("~", "/home/user"),
    ("invalid_var", "invalid_var"),  # Invalid variable should remain unchanged
    ("$INVALID_VAR/Projects", "$INVALID_VAR/Projects"),  # Invalid environment variable should remain unchanged
])
def test_error_handling(input_string, expected):
    with patch('os.path.expandvars') as mock_expandvars:
        with patch('os.path.expanduser') as mock_expanduser:
            mock_expandvars.return_value = input_string
            mock_expanduser.return_value = input_string
            assert expand(input_string) == expected

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

pytutils/Test4DT_tests/test_pytutils_env_expand_1_test_error_handling.py F [ 20%]
FF..                                                                     [100%]

=================================== FAILURES ===================================
____________ test_error_handling[~/Documents-/home/user/Documents] _____________

input_string = '~/Documents', expected = '/home/user/Documents'

    @pytest.mark.parametrize("input_string, expected", [
        ("~/Documents", "/home/user/Documents"),
        ("$HOME/Projects", "/home/user/Projects"),
        ("~", "/home/user"),
        ("invalid_var", "invalid_var"),  # Invalid variable should remain unchanged
        ("$INVALID_VAR/Projects", "$INVALID_VAR/Projects"),  # Invalid environment variable should remain unchanged
    ])
    def test_error_handling(input_string, expected):
        with patch('os.path.expandvars') as mock_expandvars:
            with patch('os.path.expanduser') as mock_expanduser:
                mock_expandvars.return_value = input_string
                mock_expanduser.return_value = input_string
>               assert expand(input_string) == expected
E               AssertionError: assert '~/Documents' == '/home/user/Documents'
E                 
E                 - /home/user/Documents
E                 + ~/Documents

pytutils/Test4DT_tests/test_pytutils_env_expand_1_test_error_handling.py:19: AssertionError
___________ test_error_handling[$HOME/Projects-/home/user/Projects] ____________

input_string = '$HOME/Projects', expected = '/home/user/Projects'

    @pytest.mark.parametrize("input_string, expected", [
        ("~/Documents", "/home/user/Documents"),
        ("$HOME/Projects", "/home/user/Projects"),
        ("~", "/home/user"),
        ("invalid_var", "invalid_var"),  # Invalid variable should remain unchanged
        ("$INVALID_VAR/Projects", "$INVALID_VAR/Projects"),  # Invalid environment variable should remain unchanged
    ])
    def test_error_handling(input_string, expected):
        with patch('os.path.expandvars') as mock_expandvars:
            with patch('os.path.expanduser') as mock_expanduser:
                mock_expandvars.return_value = input_string
                mock_expanduser.return_value = input_string
>               assert expand(input_string) == expected
E               AssertionError: assert '$HOME/Projects' == '/home/user/Projects'
E                 
E                 - /home/user/Projects
E                 + $HOME/Projects

pytutils/Test4DT_tests/test_pytutils_env_expand_1_test_error_handling.py:19: AssertionError
______________________ test_error_handling[~-/home/user] _______________________

input_string = '~', expected = '/home/user'

    @pytest.mark.parametrize("input_string, expected", [
        ("~/Documents", "/home/user/Documents"),
        ("$HOME/Projects", "/home/user/Projects"),
        ("~", "/home/user"),
        ("invalid_var", "invalid_var"),  # Invalid variable should remain unchanged
        ("$INVALID_VAR/Projects", "$INVALID_VAR/Projects"),  # Invalid environment variable should remain unchanged
    ])
    def test_error_handling(input_string, expected):
        with patch('os.path.expandvars') as mock_expandvars:
            with patch('os.path.expanduser') as mock_expanduser:
                mock_expandvars.return_value = input_string
                mock_expanduser.return_value = input_string
>               assert expand(input_string) == expected
E               AssertionError: assert '~' == '/home/user'
E                 
E                 - /home/user
E                 + ~

pytutils/Test4DT_tests/test_pytutils_env_expand_1_test_error_handling.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_env_expand_1_test_error_handling.py::test_error_handling[~/Documents-/home/user/Documents]
FAILED pytutils/Test4DT_tests/test_pytutils_env_expand_1_test_error_handling.py::test_error_handling[$HOME/Projects-/home/user/Projects]
FAILED pytutils/Test4DT_tests/test_pytutils_env_expand_1_test_error_handling.py::test_error_handling[~-/home/user]
========================= 3 failed, 2 passed in 0.07s ==========================
"""