
import pytest
from flutes.multiproc import PoolWrapper

def test_invalid_inputs():
    pool = PoolWrapper()
    
    # Test with None as the function to map
    with pytest.raises(TypeError):
        results = pool.map(None, [1, 2, 3])
    
    # Test with None as the iterable
    with pytest.raises(TypeError):
        results = pool.map(lambda x: x * x, None)
    
    # Test with non-callable function in map
    with pytest.raises(TypeError):
        results = pool.map("not_a_function", [1, 2, 3])
    
    # Test with invalid chunksize
    with pytest.raises(ValueError):
        results = pool.map(lambda x: x * x, [1, 2, 3], chunksize=0)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        pool = PoolWrapper()
    
        # Test with None as the function to map
        with pytest.raises(TypeError):
            results = pool.map(None, [1, 2, 3])
    
        # Test with None as the iterable
        with pytest.raises(TypeError):
            results = pool.map(lambda x: x * x, None)
    
        # Test with non-callable function in map
        with pytest.raises(TypeError):
            results = pool.map("not_a_function", [1, 2, 3])
    
        # Test with invalid chunksize
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_0_test_invalid_inputs.py:21: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper_gather_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.21s ===============================
"""