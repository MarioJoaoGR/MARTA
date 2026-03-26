
import pytest
from pytutils.timers import Timer

def test_valid_inputs():
    # Test initializing Timer with default values
    timer = Timer()
    assert timer.name == ''
    assert not timer.verbose

    # Test initializing Timer with custom name and verbose set to True
    timer = Timer(name='test_timer', verbose=True)
    assert timer.name == 'test_timer'
    assert timer.verbose
