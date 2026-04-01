
import pytest
from pytutils.timers import Timer

def test_edge_cases():
    # Test with None for name and False for verbose
    timer = Timer(name=None, verbose=False)
    assert timer.name is None
    assert not timer.verbose

    # Test with empty string for name and True for verbose
    timer = Timer(name='', verbose=True)
    assert timer.name == ''
    assert timer.verbose

    # Test with False for verbose
    timer = Timer(name='test_timer', verbose=False)
    assert timer.name == 'test_timer'
    assert not timer.verbose

    # Test with None for name and True for verbose
    timer = Timer(name=None, verbose=True)
    assert timer.name is None
    assert timer.verbose
