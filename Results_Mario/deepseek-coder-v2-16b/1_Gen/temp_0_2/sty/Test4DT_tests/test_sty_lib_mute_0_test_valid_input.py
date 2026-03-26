
import pytest
from unittest.mock import MagicMock, patch
from sty.lib import Register, mute

@pytest.fixture
def valid_register():
    return Register()

def test_valid_input(valid_register):
    # Create a mock register object
    mock_register = MagicMock(spec=Register)
    
    # Call the mute function with the mock register
    mute(mock_register, valid_register)
    
    # Assert that the mute method was called on the mock register
    assert mock_register.mute.call_count == 1
