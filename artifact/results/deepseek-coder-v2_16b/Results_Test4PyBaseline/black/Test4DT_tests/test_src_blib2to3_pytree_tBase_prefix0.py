
import pytest
from blib2to3.pytree import Base

def test_base():
    with pytest.raises(AssertionError):
        base = Base()
