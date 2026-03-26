
import pytest
from pytutils.timers import Timer

def test_timer_init():
    # Test default initialization
    timer = Timer()
    assert timer.name == ''
    assert not timer.verbose

    # Test with name only
    timer = Timer(name='test_name')
    assert timer.name == 'test_name'
    assert not timer.verbose

    # Test with verbose set to True
    timer = Timer(verbose=True)
    assert timer.name == ''
    assert timer.verbose
