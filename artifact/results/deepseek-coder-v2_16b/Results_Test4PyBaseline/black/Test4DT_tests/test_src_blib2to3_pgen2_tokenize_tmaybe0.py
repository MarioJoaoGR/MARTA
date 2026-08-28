
import pytest
from blib2to3.pgen2.tokenize import maybe

# Test cases for the maybe function

def test_basic_usage():
    result = maybe("apple", "banana", "cherry")
    assert result == '(apple|banana|cherry)?'

def test_single_choice():
    result = maybe("orange")