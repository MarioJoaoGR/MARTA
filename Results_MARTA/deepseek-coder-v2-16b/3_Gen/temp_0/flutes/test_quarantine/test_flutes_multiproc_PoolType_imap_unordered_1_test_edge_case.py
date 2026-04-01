
import pytest
from flutes.multiproc import PoolType

def square(x):
    return x ** 2

@pytest.fixture
def pool():
    return PoolType()

def test_edge_case(pool):
    result_iterator = pool.imap_unordered(square, range(5), chunksize=1)
    assert list(result_iterator) == [0, 1, 4, 9, 16]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

pool = <flutes.multiproc.PoolType state=RUN pool_size=128>

    def test_edge_case(pool):
        result_iterator = pool.imap_unordered(square, range(5), chunksize=1)
>       assert list(result_iterator) == [0, 1, 4, 9, 16]
E       TypeError: 'NoneType' object is not iterable

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_1_test_edge_case.py:14: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.19s ===============================

"""