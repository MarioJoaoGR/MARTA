
import pytest
from unittest.mock import patch
from sty.lib import Register, mute

# Test for valid input where all objects are instances of Register
def test_valid_input():
    class RegisterMock(Register):
        pass
    
    register1 = RegisterMock()
    register2 = RegisterMock()
    
    with patch('sty.lib.Register', RegisterMock):
        mute(register1, register2)  # This should not raise an error

# Test for invalid input where at least one object is not an instance of Register

# Test for none input which should raise TypeError