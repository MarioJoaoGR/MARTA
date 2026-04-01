
import pytest
from flutes.multiproc import PoolType

def multiply(a, b):
    return a * b

@pytest.fixture
def pool():
    return PoolType()

def test_valid_case(pool):
    results = pool.starmap(multiply, [(2, 3), (4, 5)])
    assert results == [6, 20]

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

pool = <flutes.multiproc.PoolType state=RUN pool_size=128>

    def test_valid_case(pool):
        results = pool.starmap(multiply, [(2, 3), (4, 5)])
>       assert results == [6, 20]
E       assert None == [6, 20]

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_0_test_valid_case.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.17s ===============================
"""