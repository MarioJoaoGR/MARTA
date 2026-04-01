
import pytest
from flutes.multiproc import PoolType

def example_function(a, b):
    return a + b

@pytest.fixture
def pool():
    return PoolType()

def test_apply(pool):
    result = pool.apply(example_function, args=(1, 2))
    assert result == 3

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_apply_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
__________________________________ test_apply __________________________________

pool = <flutes.multiproc.PoolType state=RUN pool_size=128>

    def test_apply(pool):
        result = pool.apply(example_function, args=(1, 2))
>       assert result == 3
E       assert None == 3

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_apply_0_test_edge_case.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_apply_0_test_edge_case.py::test_apply
============================== 1 failed in 0.18s ===============================
"""