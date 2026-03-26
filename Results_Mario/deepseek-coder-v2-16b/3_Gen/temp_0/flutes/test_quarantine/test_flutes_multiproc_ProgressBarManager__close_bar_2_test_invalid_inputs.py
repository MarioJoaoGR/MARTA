
import pytest
from flutes import ProgressBarManager
import time
import random

@pytest.fixture
def setup_manager():
    return ProgressBarManager(verbose=True)

def test_invalid_inputs(setup_manager):
    manager = setup_manager
    
    # Test invalid update frequency for new method
    with pytest.raises(ValueError):
        manager.proxy.new([1, 2, 3], update_frequency=-5)
        
    with pytest.raises(ValueError):
        manager.proxy.new(update_frequency=0)
    
    # Test invalid total for new method when iterable is None
    with pytest.raises(ValueError):
        manager.proxy.new(None, update_frequency=0.1)
    
    # Test invalid postfix type in update method
    with pytest.raises(TypeError):
        manager.proxy.update(postfix="invalid_type")
    
    # Test invalid message type in write method
    with pytest.raises(TypeError):
        manager.proxy.write(123)
    
    # Test calling close multiple times
    manager.proxy.close()  # First call to close should work
    with pytest.raises(RuntimeError):  # Second call should raise an error
        manager.proxy.close()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

setup_manager = <flutes.multiproc.ProgressBarManager object at 0x7f642254cfd0>

    def test_invalid_inputs(setup_manager):
        manager = setup_manager
    
        # Test invalid update frequency for new method
        with pytest.raises(ValueError):
            manager.proxy.new([1, 2, 3], update_frequency=-5)
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_2_test_invalid_inputs.py:18: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager__close_bar_2_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.13s ===============================

"""