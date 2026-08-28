
import pytest
from sty.primitive import Register

# Test to check if the register starts unmuted
def test_initial_unmuted():
    reg = Register()
    assert not reg.is_muted, "Register should start unmuted"

# Test to check valid inputs return expected output
def test_valid_inputs_return_expected_output():
    reg = Register()
    # Assuming the methods have default implementations that can be tested for expected outputs
    assert reg.unmute() is None, "unmute should return None"

# Test to check invalid inputs raise TypeError
def test_invalid_inputs_raise_type_error():
    reg = Register()
    with pytest.raises(TypeError):
        reg.unmute("invalid input")
