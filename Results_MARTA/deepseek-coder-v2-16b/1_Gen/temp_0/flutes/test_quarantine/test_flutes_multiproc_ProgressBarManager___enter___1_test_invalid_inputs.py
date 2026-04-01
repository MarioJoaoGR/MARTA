
import pytest
from flutes.multiproc import ProgressBarManager

def test_invalid_inputs():
    manager = ProgressBarManager(verbose=False)
    
    # Test with None iterable
    with pytest.raises(ValueError):
        manager.new(iterable=None, update_frequency=1)
    
    # Test with negative update frequency
    with pytest.raises(ValueError):
        manager.new(iterable=[1, 2, 3], update_frequency=-1)
    
    # Test with zero update frequency
    with pytest.raises(ValueError):
        manager.new(iterable=[1, 2, 3], update_frequency=0)
    
    # Test with float update frequency but no total specified
    with pytest.raises(ValueError):
        manager.new(iterable=[1, 2, 3], update_frequency=0.5)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager___enter___1_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_invalid_inputs.py:10:8: E1101: Instance of 'ProgressBarManager' has no 'new' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_invalid_inputs.py:14:8: E1101: Instance of 'ProgressBarManager' has no 'new' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_invalid_inputs.py:18:8: E1101: Instance of 'ProgressBarManager' has no 'new' member (no-member)
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___enter___1_test_invalid_inputs.py:22:8: E1101: Instance of 'ProgressBarManager' has no 'new' member (no-member)


"""