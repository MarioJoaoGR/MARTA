
import pytest
from blib2to3.pytree import Base

def test_valid_case():
    with pytest.raises(AssertionError) as excinfo:
        node1 = Base()
    assert str(excinfo.value) == "Cannot instantiate Base"

def test_edge_case():
    with pytest.raises(AssertionError) as excinfo:
        node1 = Base()
    assert str(excinfo.value) == "Cannot instantiate Base"

def test_error_case():
    with pytest.raises(AssertionError) as excinfo:
        node1 = Base()
    assert str(excinfo.value) == "Cannot instantiate Base"
