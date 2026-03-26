
import pytest
from flutes.multiproc import PoolWrapper, FuncWrapper
from unittest.mock import patch, MagicMock

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test case 1: Invalid argument type for map method
        pool = PoolWrapper()
        list(pool.map("not a function", [1, 2, 3]))
        
    with pytest.raises(TypeError):
        # Test case 2: Invalid argument type for imap_unordered method
        pool = PoolWrapper()
        list(pool.imap_unordered("not an iterable", lambda x: x))
        
    with pytest.raises(ValueError):
        # Test case 3: Invalid keyword argument passed to map_async method
        pool = PoolWrapper()
        pool.map_async([1, 2, 3], "not a function")
        
    with pytest.raises(TypeError):
        # Test case 4: Invalid argument type for starmap method
        pool = PoolWrapper()
        list(pool.starmap("not a function", [(1,), (2,)]))
        
    with pytest.raises(ValueError):
        # Test case 5: Invalid keyword argument passed to starmap_async method
        pool = PoolWrapper()
        pool.starmap_async([1, 2, 3], "not a function")

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(TypeError):
            # Test case 1: Invalid argument type for map method
            pool = PoolWrapper()
            list(pool.map("not a function", [1, 2, 3]))
    
        with pytest.raises(TypeError):
            # Test case 2: Invalid argument type for imap_unordered method
            pool = PoolWrapper()
            list(pool.imap_unordered("not an iterable", lambda x: x))
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_1_test_invalid_inputs.py:17: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolWrapper__define_method_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.58s ===============================
"""