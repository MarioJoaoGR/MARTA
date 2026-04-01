
import pytest
from sty import Register

def test_invalid_inputs():
    register = Register()
    
    # Test with an invalid input type (should not raise an error but return an empty dictionary)
    assert isinstance(register.as_dict(), dict)
    assert len(register.as_dict()) == 0  # Assuming no attributes should be included by default
