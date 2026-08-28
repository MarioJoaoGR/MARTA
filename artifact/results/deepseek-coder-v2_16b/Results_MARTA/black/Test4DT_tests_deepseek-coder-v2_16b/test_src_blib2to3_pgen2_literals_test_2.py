
import pytest
from blib2to3.pgen2.literals import evalString

def test_valid_string():
    # Test a valid string literal
    s = "'valid string'"
    assert evalString(s) == "valid string"

