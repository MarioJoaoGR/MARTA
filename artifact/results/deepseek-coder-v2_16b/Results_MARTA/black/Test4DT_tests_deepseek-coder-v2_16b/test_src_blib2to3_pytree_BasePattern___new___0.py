
import pytest
from blib2to3.pytree import BasePattern

def test_basepattern_instantiation():
    """Test that instantiating BasePattern raises an AssertionError."""
    with pytest.raises(AssertionError):
        BasePattern()
