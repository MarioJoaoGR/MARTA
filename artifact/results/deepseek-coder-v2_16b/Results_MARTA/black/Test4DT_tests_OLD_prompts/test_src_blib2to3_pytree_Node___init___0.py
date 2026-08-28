
import pytest
from blib2to3.pytree import Node
from typing import List, Optional, Any, Text

def test_edge_case():
    with pytest.raises(TypeError):
        none_node = Node(type=None, children=[])
