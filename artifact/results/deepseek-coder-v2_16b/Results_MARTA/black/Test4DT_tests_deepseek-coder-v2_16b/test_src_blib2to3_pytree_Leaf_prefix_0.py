
import pytest
from blib2to3.pytree import Leaf


def test_invalid_type():
    with pytest.raises(AssertionError):
        Leaf(type=256, value='example_value')

def test_no_context():
    leaf_node = Leaf(type=123, value='example_value')
    
    assert leaf_node._prefix == ''
    assert leaf_node.lineno == 0
    assert leaf_node.column == 0