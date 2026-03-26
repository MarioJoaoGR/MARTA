
import pytest
from flutes.multiproc import PoolWrapper

def test_invalid_inputs():
    pool = PoolWrapper()
    
    # Test with None as input for map method
    with pytest.raises(TypeError):
        list(pool.map(None, lambda x: x * x))
    
    # Test with None as input for imap method
    with pytest.raises(TypeError):
        list(pool.imap(None, lambda x: x * x))
    
    # Test with None as input for map_async method
    with pytest.raises(TypeError):
        pool.map_async(None, lambda x: x * x)
    
    # Test with None as input for imap_unordered method
    with pytest.raises(TypeError):
        list(pool.imap_unordered(None, lambda x: x * x))
    
    # Test with None as input for starmap method
    with pytest.raises(TypeError):
        list(pool.starmap(None, [(1,), (2,)]))
    
    # Test with None as input for starmap_async method
    with pytest.raises(TypeError):
        pool.starmap_async(None, [(1,), (2,)])

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper___init___0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        pool = PoolWrapper()
    
        # Test with None as input for map method
        with pytest.raises(TypeError):
            list(pool.map(None, lambda x: x * x))
    
        # Test with None as input for imap method
        with pytest.raises(TypeError):
            list(pool.imap(None, lambda x: x * x))
    
        # Test with None as input for map_async method
        with pytest.raises(TypeError):
            pool.map_async(None, lambda x: x * x)
    
        # Test with None as input for imap_unordered method
        with pytest.raises(TypeError):
            list(pool.imap_unordered(None, lambda x: x * x))
    
        # Test with None as input for starmap method
        with pytest.raises(TypeError):
            list(pool.starmap(None, [(1,), (2,)]))
    
        # Test with None as input for starmap_async method
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper___init___0_test_invalid_inputs.py:29: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper___init___0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.21s ===============================
"""