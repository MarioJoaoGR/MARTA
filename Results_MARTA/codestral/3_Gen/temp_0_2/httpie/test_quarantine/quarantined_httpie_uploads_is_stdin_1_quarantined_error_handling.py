
import sys
from io import StringIO
import pytest
from unittest.mock import patch

def test_error_handling():
    with patch('sys.stdin', StringIO()):
        fake_stdin = StringIO("Example content")
        assert is_stdin(fake_stdin) == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_uploads_is_stdin_1_test_error_handling
httpie/Test4DT_tests_codestral/test_httpie_uploads_is_stdin_1_test_error_handling.py:10:15: E0602: Undefined variable 'is_stdin' (undefined-variable)


"""