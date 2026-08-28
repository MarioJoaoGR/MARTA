
import pytest
from apimd.parser import is_public_family




def test_private_module():
    """Test a private module name."""
    assert is_public_family('_private_module.function') == False

def test_private_method():
    """Test a private method name."""
    assert is_public_family('module._private_method') == False

def test_mixed_case_with_private():
    """Test a mixed case with a private component."""
    assert is_public_family('public._hidden') == False

def test_mixed_case_with_hidden():
    """Test a mixed case with a hidden component."""
    assert is_public_family('_hidden.public') == False

def test_public_module_name():
    """Test a public module name."""
    assert is_public_family('os.path.join') == True

def test_public_module():
    """Test another public module name."""
    assert is_public_family('public.module.name') == True