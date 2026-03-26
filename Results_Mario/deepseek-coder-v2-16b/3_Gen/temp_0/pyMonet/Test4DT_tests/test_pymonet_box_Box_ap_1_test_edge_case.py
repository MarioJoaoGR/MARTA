
import pytest
from pymonet.box import Box

def test_edge_case():
    with pytest.raises(TypeError):
        box = Box(123)  # Creating a Box with integer value
        text_box = Box("Hello, World!")  # Creating a Box with string value
        result = box.ap(text_box)  # Attempting to apply the function inside the Box[A] structure to another applicative type
