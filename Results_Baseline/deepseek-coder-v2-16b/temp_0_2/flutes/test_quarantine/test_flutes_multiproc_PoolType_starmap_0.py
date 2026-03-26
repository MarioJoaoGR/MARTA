
import pytest
from flutes.multiproc import PoolType  # Corrected the import statement
from typing import Callable, Iterable, List, Any, Optional, Mapping

# Define a function that will be executed by each worker process for testing
def multiply(a, b):
    return a * b

@pytest.fixture
def pool():
    return PoolType()

def test_starmap_basic(pool):
    result = pool.starmap(multiply, [(2, 3), (4, 5)])
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_0.py F.      [100%]

=================================== FAILURES ===================================
______________________________ test_starmap_basic ______________________________

pool = <flutes.multiproc.PoolType state=RUN pool_size=128>

    def test_starmap_basic(pool):
        result = pool.starmap(multiply, [(2, 3), (4, 5)])
>       assert result == [6, 20]
E       assert None == [6, 20]

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_0.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_0.py::test_starmap_basic
========================= 1 failed, 1 passed in 0.40s ==========================
"""