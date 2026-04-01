
import pytest
from pymonet.box import Box

def test_edge_case():
    box = Box(None)
    assert box.value is None
