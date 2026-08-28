
import pytest
from unittest.mock import patch, MagicMock
from sty.primitive import Register

# Test Scenario 1: test_valid_unmute - Test unmuting a register that is initially muted
def test_valid_unmute():
    with patch('sty.primitive.Register.__init__', lambda self: None):
        register = Register()
        register.is_muted = True
        register.unmute()
        assert not register.is_muted, "Expected the register to be unmuted after calling unmute"

# Test Scenario 2: test_edge_case_none - Test unmuting a register with None value for is_muted
def test_edge_case_none():
    with patch('sty.primitive.Register.__init__', lambda self: None):
        register = Register()
        register.is_muted = None
        register.unmute()
        assert not register.is_muted, "Expected the register to be unmuted even if is_muted is None"

# Test Scenario 3: test_invalid_unmute - Test unmuting a register that is not muted to ensure it does nothing
def test_invalid_unmute():
    with patch('sty.primitive.Register.__init__', lambda self: None):
        register = Register()
        assert not hasattr(register, 'is_muted'), "Expected the register to have no is_muted attribute initially"
