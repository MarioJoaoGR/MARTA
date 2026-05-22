
import sys
from io import StringIO
import pytest
from unittest.mock import patch

def test_error_handling():
    with patch('sys.stdin', StringIO("Example content")):
        fake_stdin = StringIO("Example content")
        assert is_stdin(fake_stdin) == False
        
    with patch('sys.stdin', StringIO("Another example")):
        real_stdin = sys.stdin
        assert is_stdin(real_stdin) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_uploads_is_stdin_0_test_error_handling
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_uploads_is_stdin_0_test_error_handling.py:10:15: E0602: Undefined variable 'is_stdin' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_uploads_is_stdin_0_test_error_handling.py:14:15: E0602: Undefined variable 'is_stdin' (undefined-variable)


"""