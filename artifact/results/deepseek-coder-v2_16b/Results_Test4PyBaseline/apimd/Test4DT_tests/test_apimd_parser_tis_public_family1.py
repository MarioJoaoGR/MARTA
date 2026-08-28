
import pytest
from apimd.parser import is_public_family

# Test cases for public module paths
def test_is_public_family_public():
    assert is_public_family('os') == True

# Test case to check if a name with dots but no magic or private names returns True
def test_is_public_family_with_dots():
    assert is_public_family('sys.platform') == True

# Test case for a name starting with an underscore, which should return False
def test_is_public_family_starts_with_underscore():
    assert is_public_family('_hidden') == False

# Test case to check if a name containing magic names (like __) returns True after skipping them
def test_is_public_family_contains_magic():
    assert is_public_family('os.path.__name__') == True

# Test case for a completely private name path, should return False immediately
def test_is_public_family_completely_private():
    assert is_public_family('_sys._platform') == False
