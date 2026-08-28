
import pytest
from sty.primitive import Register

# Test to check if the register starts unmuted
def test_initial_unmuted():
    register = Register()
    assert not register.is_muted, "Register should start unmuted"

# Test to check valid inputs return expected output

# Test to check invalid inputs raise TypeError