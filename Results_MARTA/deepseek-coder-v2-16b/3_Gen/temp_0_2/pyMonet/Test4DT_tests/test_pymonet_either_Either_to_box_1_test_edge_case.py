
from pymonet.either import Either
from pymonet.box import Box
import pytest

def test_edge_case():
    # Create an Either instance with a value
    either = Either(10)
    
    # Convert the Either to a Box
    box = either.to_box()
    
    # Check if the converted Box has the correct value
    assert isinstance(box, Box)
    assert box.value == 10
