
from io import StringIO, TextIO
from contextlib import contextmanager
import sys
from typing import Iterator
import pytest

def _in_memory_output_stream_context() -> Iterator[TextIO]:
    yield StringIO(newline=None)

@pytest.fixture
def capture_output():
    @contextmanager
    def capturer():
        new_out = StringIO()
        old_out = sys.stdout
        try:
            sys.stdout = new_out
            yield new_out
        finally:
            sys.stdout = old_out
    return capturer

def test_valid_case(capture_output):
    with capture_output() as output:
        print("Hello, world!")
        print("This is a test.", file=sys.stdout)
    
    captured_output = output.getvalue()
    assert captured_output == "Hello, world!\nThis is a test.\n"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_api__in_memory_output_stream_context_0_test_valid_case
isort/Test4DT_tests/test_isort_api__in_memory_output_stream_context_0_test_valid_case.py:2:0: E0611: No name 'TextIO' in module 'io' (no-name-in-module)


"""