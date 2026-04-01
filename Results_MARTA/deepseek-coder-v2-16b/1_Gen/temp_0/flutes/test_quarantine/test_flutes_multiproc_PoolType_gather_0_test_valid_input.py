
import pytest
from flutes.multiproc import PoolType

@pytest.fixture
def pool():
    return PoolType()

def test_gather(pool):
    def example_fn(x):
        yield x * 2
        yield x * 3
    
    iterable = [1, 2, 3]
    results = list(pool.gather(example_fn, iterable))
    assert results == [2, 3, 6, 4, 6, 9]

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_gather_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_________________________________ test_gather __________________________________

pool = <flutes.multiproc.PoolType state=RUN pool_size=128>

    def test_gather(pool):
        def example_fn(x):
            yield x * 2
            yield x * 3
    
        iterable = [1, 2, 3]
>       results = list(pool.gather(example_fn, iterable))
E       TypeError: 'NoneType' object is not iterable

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_gather_0_test_valid_input.py:15: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_gather_0_test_valid_input.py::test_gather
============================== 1 failed in 0.18s ===============================
"""