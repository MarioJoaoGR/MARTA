
import pytest
from pytutils.lazy.lazy_regex import LazyRegex

def test_valid_inputs():
    # Test with valid inputs
    regex = LazyRegex(args=("pattern",), kwargs={"flags": 0})
    state = regex.__getstate__()
    
    assert isinstance(state, dict)
    assert "args" in state
    assert "kwargs" in state
    assert state["args"] == ("pattern",)
    assert state["kwargs"] == {"flags": 0}
