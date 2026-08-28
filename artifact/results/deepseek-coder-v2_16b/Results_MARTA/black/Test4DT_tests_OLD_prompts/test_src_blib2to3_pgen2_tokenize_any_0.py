
import pytest
from unittest.mock import patch
from blib2to3.pgen2.tokenize import any

def test_any_functionality():
    # Test the functionality of the `any` function with different choices
    assert any("apple", "banana", "cherry") == "(apple|banana|cherry)*"
    assert any("a", "b", "c", "d") == "(a|b|c|d)*"
    assert any("1", "2", "3", "4", "5") == "(1|2|3|4|5)*"
