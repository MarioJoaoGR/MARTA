
from io import StringIO, TextIO
from contextlib import contextmanager
import sys

@contextmanager
def capture_output():
    new_out = StringIO()
    old_out = sys.stdout
    try:
        sys.stdout = new_out
        yield new_out
    finally:
        sys.stdout = old_out

# Example usage
with capture_output() as output:
    print("Hello, world!")
    print("This is a test.", file=sys.stdout)

captured_output = output.getvalue()
print(captured_output)  # Output will be "Hello, world!\nThis is a test."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_api__in_memory_output_stream_context_0_test_edge_case
isort/Test4DT_tests/test_isort_api__in_memory_output_stream_context_0_test_edge_case.py:2:0: E0611: No name 'TextIO' in module 'io' (no-name-in-module)


"""