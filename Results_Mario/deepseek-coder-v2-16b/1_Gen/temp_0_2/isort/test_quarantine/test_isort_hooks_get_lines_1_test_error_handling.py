
import subprocess
import pytest
from unittest.mock import patch, MagicMock

@pytest.fixture(autouse=True)
def mock_subprocess_run():
    with patch('subprocess.run', side_effect=OSError("Command failed")):
        yield

def test_error_handling():
    command = ['ls', '-l']
    with pytest.raises(OSError):
        get_lines(command)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_hooks_get_lines_1_test_error_handling
isort/Test4DT_tests/test_isort_hooks_get_lines_1_test_error_handling.py:14:8: E0602: Undefined variable 'get_lines' (undefined-variable)


"""