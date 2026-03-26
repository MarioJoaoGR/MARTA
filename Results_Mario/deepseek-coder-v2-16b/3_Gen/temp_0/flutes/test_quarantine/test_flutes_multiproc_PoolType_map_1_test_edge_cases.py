
import pytest
from flutes.multiproc import PoolType

def square(x):
    return x ** 2

@pytest.fixture
def pool():
    return PoolType()

def test_map_basic(pool):
    result = pool.map(square, [1, 2, 3, 4])
    assert result == [1, 4, 9, 16]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_map_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
________________________________ test_map_basic ________________________________

pool = <flutes.multiproc.PoolType state=RUN pool_size=128>

    def test_map_basic(pool):
        result = pool.map(square, [1, 2, 3, 4])
>       assert result == [1, 4, 9, 16]
E       assert None == [1, 4, 9, 16]

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_map_1_test_edge_cases.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_map_1_test_edge_cases.py::test_map_basic
============================== 1 failed in 0.17s ===============================

"""