
import pytest
from codetiming import _timers  # Assuming the module is named '_timers' and contains the Timers class

def test_invalid_inputs():
    timers = _timers.Timers()
    
    with pytest.raises(TypeError):
        timers['test'] = 'value'  # This should raise a TypeError as per the __setitem__ method implementation
