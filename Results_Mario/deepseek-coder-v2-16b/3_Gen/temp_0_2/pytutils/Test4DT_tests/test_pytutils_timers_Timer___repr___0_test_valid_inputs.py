
import pytest
from pytutils.timers import Timer

def test_valid_inputs():
    # Test setup
    timer = Timer('long_operation', verbose=True)
    
    with pytest.raises(RuntimeError):  # Since we are not actually timing anything, we expect an error if it doesn't work properly
        with timer:
            raise RuntimeError("Simulated runtime error")  # Simulate a runtime error to trigger the expected exception
