
import pytest
from unittest.mock import patch
from httpie.plugins.base import TransportPlugin

class EdgeCase(TransportPlugin):
    pass

def test_edge_case():
    edge_case = EdgeCase()
    with pytest.raises(NotImplementedError):
        edge_case.get_adapter()
