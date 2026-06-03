
import pytest
from unittest.mock import patch
from codetiming._timers import Timers

def test_invalid_inputs():
    timers = Timers()
    
    with pytest.raises(KeyError):
        # Test when the timer name does not exist in the dictionary
        timers.max("nonexistent_timer")
        
    with patch.object(Timers, 'apply', side_effect=KeyError('test')):
        # Mocking the apply method to raise KeyError for any call
        with pytest.raises(KeyError):
            timers.max("any_name")
