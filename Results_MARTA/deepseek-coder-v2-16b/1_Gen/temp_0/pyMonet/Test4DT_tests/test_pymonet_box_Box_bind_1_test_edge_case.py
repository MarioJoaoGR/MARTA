
import pytest
from pymonet.box import Box

def test_edge_case():
    box = Box(None)
    assert box.bind(lambda x: None) is None
