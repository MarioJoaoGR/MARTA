
import pytest
from pymonet.monad_try import Try  # Assuming this is a hypothetical module

def test_valid_inputs():
    try_instance = Try('valid_value', True)
    
    assert try_instance.is_success == True
    assert try_instance.value == 'valid_value'
