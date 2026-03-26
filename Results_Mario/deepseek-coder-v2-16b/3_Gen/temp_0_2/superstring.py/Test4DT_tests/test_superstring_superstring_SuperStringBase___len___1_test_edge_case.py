
from unittest.mock import MagicMock
import pytest
from superstring.superstring import SuperStringBase

class EdgeString(SuperStringBase):
    def length(self):
        return 0

def test_edge_case():
    edge_string = EdgeString()
    assert len(edge_string) == 0
