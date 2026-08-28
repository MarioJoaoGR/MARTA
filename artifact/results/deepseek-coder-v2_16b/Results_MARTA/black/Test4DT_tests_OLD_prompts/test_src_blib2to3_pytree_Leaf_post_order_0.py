
import pytest
from blib2to3.pytree import Leaf


def test_initialization_with_context():
    with pytest.raises(TypeError):
        Leaf(type=1, value="example", context=(10, 30))

def test_initialization_with_prefix():
    with pytest.raises(TypeError):
        Leaf(type=1, value="example", context=(10, 30), prefix="prefix")

def test_initialization_with_fixers_applied():
    with pytest.raises(TypeError):
        Leaf(type=1, value="example", context=(10, 30), prefix="prefix", fixers_applied=["fixer1"])
