
# Module: pytutils.files
import pytest
import os
import sys
import functools
from pytutils.files import islurp

# Mock LINEMODE for testing purposes
LINEMODE = 10

@pytest.fixture(autouse=True)
def mock_stdin():
    # Create a string to simulate stdin
    original_stdin = sys.stdin
    sys.stdin = io.StringIO("Line1\nLine2\nLine3\n")
    yield
    sys.stdin = original_stdin

def test_islurp_read_text_file_line_by_line():
    with open('example.txt', 'w') as f:
        f.write("Line1\nLine2\nLine3\n")
    lines = list(islurp('example.txt'))
    assert lines == ['Line1\n', 'Line2\n', 'Line3\n']

def test_islurp_read_binary_data_from_stdin():
    # Capture stdout to check the output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    for chunk in islurp('-', mode='rb', iter_by=1024):
        sys.stdout.write(chunk)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "Line1\nLine2\nLine3\n"

def test_islurp_read_text_file_with_specific_modes():
    with open('expanded_env_var_file.txt', 'w') as f:
        f.write("Content")
    lines = list(islurp('expanded_env_var_file.txt', expandvars=True))
    assert lines == ['Content']

def test_islurp_read_binary_file_without_expanding_environment_variables():
    with open('binary_file.bin', 'wb') as f:
        f.write(b"BinaryData")
    chunks = list(islurp('binary_file.bin', mode='rb'))
    assert chunks == [b"BinaryData"]

def test_islurp_read_from_standard_input_in_text_mode():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    for line in islurp('-', allow_stdin=True):
        sys.stdout.write(line)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == "Line1\nLine2\nLine3\n"

def test_islurp_read_file_with_user_home_directory_expansion_and_specific_iteration():
    with open('~/documents/largefile.txt', 'w') as f:
        f.write("LargeFileContent")
    chunks = list(islurp('~/documents/largefile.txt', expanduser=True, iter_by=1024*10))
    assert chunks == ['LargeFileContent']

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_files_islurp_0
pytutils/Test4DT_tests/test_pytutils_files_islurp_0.py:16:16: E0602: Undefined variable 'io' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_files_islurp_0.py:28:22: E0602: Undefined variable 'io' (undefined-variable)
pytutils/Test4DT_tests/test_pytutils_files_islurp_0.py:48:22: E0602: Undefined variable 'io' (undefined-variable)


"""