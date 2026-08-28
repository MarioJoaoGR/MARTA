
import pytest
from apimd.parser import is_public_family



def test_valid_public_module():
    name = 'os'
    result = is_public_family(name)
    assert result == True, f"Expected True for valid public module '{name}', but got {result}"

def test_valid_hierarchical_public_module():
    name = 'os.path'
    result = is_public_family(name)
    assert result == True, f"Expected True for valid hierarchical public module '{name}', but got {result}"

def test_invalid_private_module():
    name = 'sys._abc'
    result = is_public_family(name)
    assert result == False, f"Expected False for invalid private module '{name}', but got {result}"

def test_invalid_local_module():
    name = '_collections'
    result = is_public_family(name)
    assert result == False, f"Expected False for invalid local module '{name}', but got {result}"