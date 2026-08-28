
import pytest
from blib2to3.pytree import Base

def test_valid_case():
    with pytest.raises(AssertionError) as excinfo:
        base = Base()
    assert str(excinfo.value) == "Cannot instantiate Base"
