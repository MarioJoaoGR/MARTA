
import pytest
from blib2to3.pytree import Leaf, Context





def test_prefix_settable():
    leaf = Leaf(type=123, value="example_value")
    with pytest.raises(TypeError):
        leaf.prefix("new_prefix")