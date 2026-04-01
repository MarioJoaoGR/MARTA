
import pytest
from pymonet.box import Box

def test_edge_case():
    # Test with None input to check error handling
    box = Box(None)
    assert box.value is None
