
import pytest
from codetiming import _timers  # Assuming the module is named '_timers' and contains the Timers class

def test_invalid_inputs():
    timers = _timers.Timers()
    
    with pytest.raises(TypeError):
        timers['timer1'] = 1.0
