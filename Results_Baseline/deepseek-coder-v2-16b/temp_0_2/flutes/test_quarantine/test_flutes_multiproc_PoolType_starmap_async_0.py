
import pytest
from flutes.multiproc import PoolType
from typing import Callable, Iterable, List, Optional, Any, Mapping
import multiprocessing as mp

# Fixture to create a PoolType instance for testing
@pytest.fixture
def pool():
    return PoolType()

# Test function to multiply two numbers
def multiply(a: int, b: int) -> int:
    return a * b

# Define the test cases
def test_starmap_async_basic(pool):
    """Test starmap_async with basic arguments."""
    result = pool.starmap_async(multiply, [(2, 3), (4, 5)]).get()
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

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_async_0.py F [100%]

=================================== FAILURES ===================================
___________________________ test_starmap_async_basic ___________________________

pool = <flutes.multiproc.PoolType state=RUN pool_size=128>

    def test_starmap_async_basic(pool):
        """Test starmap_async with basic arguments."""
>       result = pool.starmap_async(multiply, [(2, 3), (4, 5)]).get()
E       AttributeError: 'NoneType' object has no attribute 'get'

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_async_0.py:19: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_async_0.py::test_starmap_async_basic
============================== 1 failed in 0.18s ===============================
"""