
import pytest
from pymonet.box import Box

def test_valid_input():
    box = Box(123)
    assert str(box) == 'Box[value=123]'
