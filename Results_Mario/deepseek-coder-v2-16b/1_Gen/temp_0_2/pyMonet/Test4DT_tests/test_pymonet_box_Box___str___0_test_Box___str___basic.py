
import pytest
from pymonet.box import Box

def test_Box___str___basic():
    box = Box(42)
    assert str(box) == "Box[value=42]"
