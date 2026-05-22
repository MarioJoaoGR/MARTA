
import pytest
from httpie.manager.compat import run_pip, PipError
from unittest.mock import patch

@pytest.mark.parametrize("args", [["invalid_command"]])
def test_invalid_command(args):
    with pytest.raises(PipError) as excinfo:
        run_pip(args)
    assert "Invalid command" in str(excinfo.value)

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_compat_run_pip_1_test_invalid_command.py F [100%]

=================================== FAILURES ===================================
_________________________ test_invalid_command[args0] __________________________

args = ['invalid_command']

    @pytest.mark.parametrize("args", [["invalid_command"]])
    def test_invalid_command(args):
        with pytest.raises(PipError) as excinfo:
            run_pip(args)
>       assert "Invalid command" in str(excinfo.value)
E       assert 'Invalid command' in '(b\'\', b\'ERROR: unknown command "invalid_command"\\n\')'
E        +  where '(b\'\', b\'ERROR: unknown command "invalid_command"\\n\')' = str(PipError(b'', b'ERROR: unknown command "invalid_command"\n'))
E        +    where PipError(b'', b'ERROR: unknown command "invalid_command"\n') = <ExceptionInfo PipError(b'', b'ERROR: unknown command "invalid_command"\n') tblen=3>.value

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_compat_run_pip_1_test_invalid_command.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_manager_compat_run_pip_1_test_invalid_command.py::test_invalid_command[args0]
============================== 1 failed in 0.26s ===============================
"""