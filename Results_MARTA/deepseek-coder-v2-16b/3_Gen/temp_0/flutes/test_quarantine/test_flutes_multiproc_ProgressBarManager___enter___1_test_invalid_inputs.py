
import pytest
from flutes.multiproc import ProgressBarManager

def test_invalid_inputs():
    manager = ProgressBarManager(verbose=False)
    
    # Test with invalid update frequency (should raise ValueError)
    with pytest.raises(ValueError):
        manager.new([1, 2, 3], update_frequency=-5)
    
    # Test with invalid total in kwargs (should raise ValueError)
    with pytest.raises(ValueError):
        manager.new(range(10), update_frequency=0.1, total=None)
    
    # Test with both iterable and total specified inconsistently (should raise ValueError)
    with pytest.raises(ValueError):
        manager.new([1, 2, 3], update_frequency=0.1, total=len([1, 2, 3]))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager___enter___1_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_invalid_inputs.py:10:8: E1101: Instance of 'ProgressBarManager' has no 'new' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_invalid_inputs.py:14:8: E1101: Instance of 'ProgressBarManager' has no 'new' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_invalid_inputs.py:18:8: E1101: Instance of 'ProgressBarManager' has no 'new' member (no-member)


"""