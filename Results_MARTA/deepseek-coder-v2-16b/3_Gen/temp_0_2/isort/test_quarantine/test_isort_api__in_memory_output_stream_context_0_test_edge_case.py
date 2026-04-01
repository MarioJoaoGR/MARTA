
from io import StringIO
from contextlib import contextmanager
import pytest

@contextmanager
def _in_memory_output_stream_context():
    stream = StringIO(newline=None)
    yield stream

def test_edge_case():
    with _in_memory_output_stream_context() as output_stream:
        # Perform operations on the output_stream, such as writing sorted import statements
        print("Hello, World!", file=output_stream)
        assert output_stream.getvalue() == "Hello, World!"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_api__in_memory_output_stream_context_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        with _in_memory_output_stream_context() as output_stream:
            # Perform operations on the output_stream, such as writing sorted import statements
            print("Hello, World!", file=output_stream)
>           assert output_stream.getvalue() == "Hello, World!"
E           AssertionError: assert 'Hello, World!\n' == 'Hello, World!'
E             
E             - Hello, World!
E             + Hello, World!
E             ?              +

isort/Test4DT_tests/test_isort_api__in_memory_output_stream_context_0_test_edge_case.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_api__in_memory_output_stream_context_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.10s ===============================
"""