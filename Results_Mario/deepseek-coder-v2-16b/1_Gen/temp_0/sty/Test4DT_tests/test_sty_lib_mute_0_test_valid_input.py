
import pytest
from unittest.mock import Mock
from sty.lib import mute, Register

def test_valid_input():
    # Create mocks for Register objects
    register1 = Mock(spec=Register)
    register2 = Mock(spec=Register)
    
    # Call the mute function with valid inputs
    mute(register1, register2)
    
    # Assert that the mute method was called on each object
    register1.mute.assert_called_once()
    register2.mute.assert_called_once()
