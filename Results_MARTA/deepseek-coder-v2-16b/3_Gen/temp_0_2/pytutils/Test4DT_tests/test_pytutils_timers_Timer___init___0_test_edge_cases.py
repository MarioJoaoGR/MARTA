
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

    # Test with False for both name and verbose
    timer = Timer(name=False, verbose=False)
    assert timer.name is False
    assert not timer.verbose
