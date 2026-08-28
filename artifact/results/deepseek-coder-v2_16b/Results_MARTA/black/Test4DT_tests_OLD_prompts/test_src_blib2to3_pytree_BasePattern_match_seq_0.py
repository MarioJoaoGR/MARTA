
import pytest
from blib2to3.pytree import NodePattern, BasePattern



def test_invalid_input_multiple_nodes():
    with pytest.raises(TypeError):
        pattern = NodePattern(type=[1, 2, 3])