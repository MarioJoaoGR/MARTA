
from io import TextIOBase
from tempfile import TemporaryFile
from contextlib import contextmanager
from unittest.mock import patch
import sys
from isort.api import _in_memory_output_stream_context

@contextmanager
def capture_output():
    out = StringIO()
    with patch('sys.stdout', new=out):
        yield out

def test_valid_case():
    expected_output = "Hello, World!\n"
    with _in_memory_output_stream_context() as stream:
        print("Hello, World!", file=stream)
        captured_output = stream.getvalue()
        assert captured_output == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_api__in_memory_output_stream_context_0_test_valid_case
isort/Test4DT_tests/test_isort_api__in_memory_output_stream_context_0_test_valid_case.py:11:10: E0602: Undefined variable 'StringIO' (undefined-variable)


"""