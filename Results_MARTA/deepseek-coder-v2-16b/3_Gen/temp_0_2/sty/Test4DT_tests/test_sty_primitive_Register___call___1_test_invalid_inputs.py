
import pytest
from sty.primitive import Register

def test_invalid_inputs():
    custom_register = Register()
    
    # Test invalid input for fg and bg calls (should raise an error)
    with pytest.raises(AttributeError):
        custom_register("invalid_input")  # This should raise a TypeError
