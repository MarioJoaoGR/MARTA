
import pytest
from string_utils.manipulation import booleanize

def test_invalid_inputs():
    # Test cases for invalid inputs
    assert not booleanize(""), "Empty string should return False"
    assert not booleanize("false"), "String 'false' should return False"
    assert not booleanize("0"), "String '0' should return False"
    assert not booleanize("no"), "String 'no' should return False"
    assert not booleanize("n"), "String 'n' should return False"
    assert not booleanize("False"), "String 'False' should return False (case sensitive)"
    assert not booleanize("NO"), "String 'NO' should return False (case sensitive)"
