
import pytest
from apimd.parser import is_public_family




def test_private_component():
    """Test that a name with a private component returns False."""
    assert is_public_family('_private_module.function') == False

def test_local_component():
    """Test that a name with a local component returns False."""
    assert is_public_family('module._local_method') == False

def test_mixed_cases():
    """Test that a mixed case with a private component returns False."""
    assert is_public_family('public._hidden') == False
    assert is_public_family('_hidden.public') == False

def test_public_name():
    """Test that a public name returns True."""
    assert is_public_family('os.path.join') == True

def test_public_module_name():
    """Test that a public module name returns True."""
    assert is_public_family('public.module.name') == True