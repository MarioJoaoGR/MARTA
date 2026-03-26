
import pytest
from multiprocessing import Pool
from flutes.multiproc import PoolType

def multiply(a, b):
    return a * b

@pytest.fixture
def pool():
    return PoolType()

def test_apply_async_valid_inputs(pool):
    result = pool.apply_async(multiply, (2, 3))
    assert result.get() == 6

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_apply_async_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
________________________ test_apply_async_valid_inputs _________________________

pool = <flutes.multiproc.PoolType state=RUN pool_size=128>

    def test_apply_async_valid_inputs(pool):
        result = pool.apply_async(multiply, (2, 3))
>       assert result.get() == 6
E       AttributeError: 'NoneType' object has no attribute 'get'

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_apply_async_0_test_valid_inputs.py:15: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_apply_async_0_test_valid_inputs.py::test_apply_async_valid_inputs
============================== 1 failed in 0.19s ===============================
"""