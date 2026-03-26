
import pytest
from sty.lib import Register, mute

def test_valid_inputs():
    # Create a mock Register class for testing
    class MockRegister(Register):
        def mute(self):
            pass
    
    # Valid inputs - should not raise an error
    register1 = MockRegister()
    register2 = MockRegister()
    assert mute(register1, register2) is None  # Ensure the function returns None for valid inputs

    # Invalid input - should raise a ValueError
    with pytest.raises(ValueError):
        invalid_object = "not a Register"
        mute(invalid_object)
