
import pytest
from pymonet.monad_try import Try  # Assuming this is a hypothetical module, adjust accordingly

def test_valid_inputs():
    try_object1 = Try('result', True)
    try_object2 = Try('result', True)
    
    assert try_object1 == try_object2
