
import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def test_valid_inputs():
    # Arrange
    args = (r'\d+',)
    kwargs = {'flags': 0}
    lazy_regex = LazyRegex(args, kwargs)
    
    # Act
    state = lazy_regex.__getstate__()
    
    # Assert
    assert state == {"args": args, "kwargs": kwargs}
