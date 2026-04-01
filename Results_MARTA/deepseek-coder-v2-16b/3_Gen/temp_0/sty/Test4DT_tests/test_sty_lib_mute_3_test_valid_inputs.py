
import pytest
from unittest.mock import Mock
from sty.lib import mute, Register

@pytest.fixture
def valid_registers():
    reg1 = Mock(spec=Register)
    reg2 = Mock(spec=Register)
    return reg1, reg2

def test_valid_inputs(valid_registers):
    reg1, reg2 = valid_registers
    mute(reg1, reg2)
    
    # Assertions to ensure the mocks are called correctly
    reg1.mute.assert_called_once()
    reg2.mute.assert_called_once()
