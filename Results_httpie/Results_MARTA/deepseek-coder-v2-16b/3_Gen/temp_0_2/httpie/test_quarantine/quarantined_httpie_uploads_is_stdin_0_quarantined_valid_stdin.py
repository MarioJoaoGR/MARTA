
import sys
from io import StringIO
from unittest.mock import patch

def test_valid_stdin():
    with patch('sys.stdin', StringIO("Example content")):
        assert is_stdin(sys.stdin) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_uploads_is_stdin_0_test_valid_stdin
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_uploads_is_stdin_0_test_valid_stdin.py:8:15: E0602: Undefined variable 'is_stdin' (undefined-variable)


"""