
import pytest
from apimd.parser import is_public_family

def test_valid_public_name():
    assert is_public_family('os') == True
    assert is_public_family('os.path') == True

def test_invalid_private_name():
    assert is_public_family('_collections') == False
    assert is_public_family('sys._abc') == False
