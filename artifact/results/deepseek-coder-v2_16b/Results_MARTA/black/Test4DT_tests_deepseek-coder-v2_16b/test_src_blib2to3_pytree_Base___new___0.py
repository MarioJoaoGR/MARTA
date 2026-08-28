
import pytest
from blib2to3.pytree import Base

def test_base_instantiation():
    with pytest.raises(AssertionError) as excinfo:
        Base()
    assert str(excinfo.value) == "Cannot instantiate Base"

