
import pytest
from unittest.mock import patch, MagicMock
from pip._internal.exceptions import PipError

def run_pip(args: List[str]) -> bytes:
    if is_frozen:
        pip_executable = [_discover_system_pip()]
    else:
        pip_executable = [sys.executable, '-m', 'pip']

    return _run_pip_subprocess(pip_executable, args)

def test_invalid_input():
    with patch('pip._internal.exceptions.PipError', side_effect=PipError("Mocked PipError")):
        with pytest.raises(PipError):
            run_pip(['invalid_arg'])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_manager_compat_run_pip_3_test_invalid_input
httpie/Test4DT_tests_codestral/test_httpie_manager_compat_run_pip_3_test_invalid_input.py:6:18: E0602: Undefined variable 'List' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_manager_compat_run_pip_3_test_invalid_input.py:7:7: E0602: Undefined variable 'is_frozen' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_manager_compat_run_pip_3_test_invalid_input.py:8:26: E0602: Undefined variable '_discover_system_pip' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_manager_compat_run_pip_3_test_invalid_input.py:10:26: E0602: Undefined variable 'sys' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_manager_compat_run_pip_3_test_invalid_input.py:12:11: E0602: Undefined variable '_run_pip_subprocess' (undefined-variable)


"""