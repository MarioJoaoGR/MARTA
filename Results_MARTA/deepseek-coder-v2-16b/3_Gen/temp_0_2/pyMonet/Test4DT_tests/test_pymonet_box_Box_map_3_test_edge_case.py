
import pytest
from pymonet.box import Box

def test_edge_case():
    box = Box(None)
    mapped_box = box.map(lambda x: str(x))
    assert isinstance(mapped_box, Box)
    assert mapped_box.value == "None"
