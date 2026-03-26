
import pytest
from flutes.multiproc import PoolType
from typing import Callable, Iterable, Iterator, Any, Mapping

def square(x):
    return x ** 2

@pytest.fixture
def pool():
    return PoolType()

def test_invalid_inputs(pool):
    with pytest.raises(TypeError) as e:
        result_iterator = pool.imap_unordered(None, range(5), chunksize=1)
    assert str(e.value) == "Expected a callable function"

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

pool = <flutes.multiproc.PoolType state=RUN pool_size=128>

    def test_invalid_inputs(pool):
>       with pytest.raises(TypeError) as e:
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_invalid_inputs.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.19s ===============================
"""