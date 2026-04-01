
import pytest
import os
from pytutils.env import expand

@pytest.mark.parametrize("input_str, expected", [
    ("~/Documents", "/home/user/Documents"),
    ("$HOME/Projects", f"{os.getenv('HOME')}/Projects"),
    ("~", os.path.expanduser("~"))
])
def test_valid_input_happy_path(input_str, expected):
    # Mock the environment variable for $HOME
    with pytest.MonkeyPatch.context() as mp:
        mp.setenv('HOME', '/home/user')
        assert expand(input_str) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

pytutils/Test4DT_tests/test_pytutils_env_expand_0_test_valid_input_happy_path.py . [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
___ test_valid_input_happy_path[$HOME/Projects-/home/joaovitorino/Projects] ____

input_str = '$HOME/Projects', expected = '/home/joaovitorino/Projects'

    @pytest.mark.parametrize("input_str, expected", [
        ("~/Documents", "/home/user/Documents"),
        ("$HOME/Projects", f"{os.getenv('HOME')}/Projects"),
        ("~", os.path.expanduser("~"))
    ])
    def test_valid_input_happy_path(input_str, expected):
        # Mock the environment variable for $HOME
        with pytest.MonkeyPatch.context() as mp:
            mp.setenv('HOME', '/home/user')
>           assert expand(input_str) == expected
E           AssertionError: assert '/home/user/Projects' == '/home/joaovitorino/Projects'
E             
E             - /home/joaovitorino/Projects
E             + /home/user/Projects

pytutils/Test4DT_tests/test_pytutils_env_expand_0_test_valid_input_happy_path.py:15: AssertionError
______________ test_valid_input_happy_path[~-/home/joaovitorino] _______________

input_str = '~', expected = '/home/joaovitorino'

    @pytest.mark.parametrize("input_str, expected", [
        ("~/Documents", "/home/user/Documents"),
        ("$HOME/Projects", f"{os.getenv('HOME')}/Projects"),
        ("~", os.path.expanduser("~"))
    ])
    def test_valid_input_happy_path(input_str, expected):
        # Mock the environment variable for $HOME
        with pytest.MonkeyPatch.context() as mp:
            mp.setenv('HOME', '/home/user')
>           assert expand(input_str) == expected
E           AssertionError: assert '/home/user' == '/home/joaovitorino'
E             
E             - /home/joaovitorino
E             + /home/user

pytutils/Test4DT_tests/test_pytutils_env_expand_0_test_valid_input_happy_path.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_env_expand_0_test_valid_input_happy_path.py::test_valid_input_happy_path[$HOME/Projects-/home/joaovitorino/Projects]
FAILED pytutils/Test4DT_tests/test_pytutils_env_expand_0_test_valid_input_happy_path.py::test_valid_input_happy_path[~-/home/joaovitorino]
========================= 2 failed, 1 passed in 0.05s ==========================
"""