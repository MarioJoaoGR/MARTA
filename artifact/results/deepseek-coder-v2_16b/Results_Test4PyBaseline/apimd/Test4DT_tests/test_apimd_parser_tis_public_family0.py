
import pytest
from apimd.parser import is_public_family

# Test cases for public module paths
def test_is_public_family_public():
    assert is_public_family('os') == True