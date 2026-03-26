
import subprocess
import pytest

def test_empty_list_input():
    with pytest.raises(subprocess.CalledProcessError):
        get_output([])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_hooks_get_output_4_test_empty_list_input
isort/Test4DT_tests/test_isort_hooks_get_output_4_test_empty_list_input.py:7:8: E0602: Undefined variable 'get_output' (undefined-variable)


"""