
import pytest
from sty.lib import Register, unmute

def test_valid_inputs():
    class SubRegister(Register):
        def unmute(self):
            pass
    
    obj1 = Register()
    obj2 = SubRegister()
    
    # Test with valid inputs
    try:
        unmute(obj1, obj2)
    except ValueError as e:
        pytest.fail(f"Unexpected ValueError: {e}")
