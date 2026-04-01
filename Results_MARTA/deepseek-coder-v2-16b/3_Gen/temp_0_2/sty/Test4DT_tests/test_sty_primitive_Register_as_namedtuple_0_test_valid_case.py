
# Assuming the structure of your project is such that 'sty' is a package and 'Register' is supposed to be in 'sty.Register'
from sty import Register  # Correcting the import path based on the module structure
import pytest

def test_valid_case():
    register = Register()
    assert isinstance(register, Register)
