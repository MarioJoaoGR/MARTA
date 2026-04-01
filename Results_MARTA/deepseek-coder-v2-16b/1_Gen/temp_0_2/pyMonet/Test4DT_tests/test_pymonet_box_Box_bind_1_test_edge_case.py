
import pytest
from pymonet.box import Box  # Assuming the correct import path is used

def test_bind():
    box = Box(10)
    mapped_value = box.bind(lambda x: x * 2)
    assert mapped_value == 20
