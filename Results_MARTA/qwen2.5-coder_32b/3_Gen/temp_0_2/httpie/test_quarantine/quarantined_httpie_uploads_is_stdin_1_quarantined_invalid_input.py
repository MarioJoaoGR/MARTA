
import sys
from io import StringIO
import pytest
from unittest.mock import patch

def test_invalid_input():
    with patch('sys.stdin', StringIO()):
        fake_stdin = StringIO("Example content")
        assert not is_stdin(fake_stdin)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_uploads_is_stdin_1_test_invalid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_uploads_is_stdin_1_test_invalid_input.py:10:19: E0602: Undefined variable 'is_stdin' (undefined-variable)


"""