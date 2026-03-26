
from pymonet.box import Box  # Assuming this is the correct module path
import pytest

def test_valid_input():
    box = Box(10)
    mapped_value = box.bind(lambda x: x * 2)
    assert mapped_value == 20
