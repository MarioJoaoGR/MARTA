
import pytest
from multiprocessing import Pool, TimeoutError
from flutes.multiproc import DummyPool

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test invalid initializer type
        pool = DummyPool(processes=0, initializer="not a callable")
        
    with pytest.raises(ValueError):
        # Test invalid processes value
        pool = DummyPool(processes=-1)
        
    with pytest.raises(TypeError):
        # Test invalid initargs type
        pool = DummyPool(processes=0, initargs="not an iterable")
        
    with pytest.raises(ValueError):
        # Test invalid maxtasksperchild value
        pool = DummyPool(processes=0, maxtasksperchild=-1)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_map_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(TypeError):
            # Test invalid initializer type
            pool = DummyPool(processes=0, initializer="not a callable")
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_map_0_test_invalid_inputs.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_map_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.08s ===============================

"""