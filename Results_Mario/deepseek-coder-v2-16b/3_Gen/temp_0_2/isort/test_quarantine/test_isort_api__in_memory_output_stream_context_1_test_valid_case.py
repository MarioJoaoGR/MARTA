
from io import StringIO, TextIO
from contextlib import contextmanager
from typing import Iterator

@contextmanager
def _in_memory_output_stream_context() -> Iterator[TextIO]:
    stream = StringIO(newline=None)
    yield stream  # Yield the StringIO object directly as a TextIO type

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_api__in_memory_output_stream_context_1_test_valid_case
isort/Test4DT_tests/test_isort_api__in_memory_output_stream_context_1_test_valid_case.py:2:0: E0611: No name 'TextIO' in module 'io' (no-name-in-module)


"""