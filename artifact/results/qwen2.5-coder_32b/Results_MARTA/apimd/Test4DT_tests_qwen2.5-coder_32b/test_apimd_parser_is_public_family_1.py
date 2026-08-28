
import pytest
from apimd.parser import is_public_family




def test_private_module():
    """Test that a private module name returns False."""
    assert is_public_family('_private_module.function') == False

def test_private_method():
    """Test that a private method name returns False."""
    assert is_public_family('module._private_method') == False

def test_mixed_case_with_hidden():
    """Test that a mixed case with hidden component returns False."""
    assert is_public_family('public._hidden') == False

def test_hidden_then_public():
    """Test that a hidden then public component returns False."""
    assert is_public_family('_hidden.public') == False

def test_public_module_name():
    """Test that a public module name returns True."""
    assert is_public_family('os.path.join') == True

def test_public_module_with_dots():
    """Test that a public module name with dots returns True."""
    assert is_public_family('public.module.name') == True