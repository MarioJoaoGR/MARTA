
import pytest
from blib2to3.pytree import Node


def test_edge_case():
    empty_list_node = Node(type=256, children=[])
    with pytest.raises(TypeError):
        none_input_node = Node(type=257, children=None)