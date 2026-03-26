
import pytest
from flutes.multiproc import PoolType

def square(x):
    return x ** 2

@pytest.fixture
def pool():
    return PoolType()

def test_imap_valid_inputs(pool):
    iterable = [1, 2, 3, 4]
    result_iterator = pool.imap(square, iterable)
    
    results = list(result_iterator)
    
    assert results == [1, 4, 9, 16]

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
____________________________ test_imap_valid_inputs ____________________________

pool = <flutes.multiproc.PoolType state=RUN pool_size=128>

    def test_imap_valid_inputs(pool):
        iterable = [1, 2, 3, 4]
        result_iterator = pool.imap(square, iterable)
    
>       results = list(result_iterator)
E       TypeError: 'NoneType' object is not iterable

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_0_test_valid_inputs.py:16: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_0_test_valid_inputs.py::test_imap_valid_inputs
============================== 1 failed in 0.18s ===============================
"""