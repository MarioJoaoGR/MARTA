# Module: blib2to3.pytree
import pytest
from blib2to3.pytree import Base

# Test case for ensuring the base class 'Base' cannot be instantiated
def test_base_instantiation():
    with pytest.raises(AssertionError):
        Base()
