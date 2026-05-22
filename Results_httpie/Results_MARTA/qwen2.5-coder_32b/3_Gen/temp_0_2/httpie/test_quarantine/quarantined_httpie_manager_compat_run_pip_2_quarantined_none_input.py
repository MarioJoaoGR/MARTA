
import pytest
from unittest.mock import patch
import sys

def run_pip(args: List[str]) -> bytes:
    if is_frozen:
        pip_executable = [_discover_system_pip()]
    else:
        pip_executable = [sys.executable, '-m', 'pip']

    return _run_pip_subprocess(pip_executable, args)

@pytest.mark.parametrize("input_value", [None])
def test_none_input(monkeypatch):
    with patch('sys.argv', ['script_name'], input=None):
        with pytest.raises(TypeError):
            run_pip([None])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_manager_compat_run_pip_2_test_none_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_compat_run_pip_2_test_none_input.py:6:18: E0602: Undefined variable 'List' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_compat_run_pip_2_test_none_input.py:7:7: E0602: Undefined variable 'is_frozen' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_compat_run_pip_2_test_none_input.py:8:26: E0602: Undefined variable '_discover_system_pip' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_manager_compat_run_pip_2_test_none_input.py:12:11: E0602: Undefined variable '_run_pip_subprocess' (undefined-variable)


"""