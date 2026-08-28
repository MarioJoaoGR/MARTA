
import pytest
from blib2to3.pytree import Node



def test_init_with_invalid_type():
    with pytest.raises(AssertionError):
        Node(type=255, children=[])