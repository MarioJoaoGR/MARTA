
import pytest
from unittest.mock import patch
from httpie.internal.daemon_runner import is_daemon_mode

@pytest.mark.parametrize("args", [None, [], ['config.txt'], ['--other', 'config.txt']])
def test_invalid_input(args):
    with patch('builtins.isinstance', return_value=False):
        assert not is_daemon_mode(args)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_daemon_runner_is_daemon_mode_5_test_invalid_input.py F [ 25%]
...                                                                      [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_input[None] ___________________________

args = None

    @pytest.mark.parametrize("args", [None, [], ['config.txt'], ['--other', 'config.txt']])
    def test_invalid_input(args):
        with patch('builtins.isinstance', return_value=False):
>           assert not is_daemon_mode(args)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_daemon_runner_is_daemon_mode_5_test_invalid_input.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

args = None

    def is_daemon_mode(args: List[str]) -> bool:
>       return '--daemon' in args
E       TypeError: argument of type 'NoneType' is not iterable

httpie/httpie/internal/daemon_runner.py:38: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_internal_daemon_runner_is_daemon_mode_5_test_invalid_input.py::test_invalid_input[None]
========================= 1 failed, 3 passed in 0.17s ==========================
"""