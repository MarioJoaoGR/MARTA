
import pytest
from superstring.superstring import SuperStringSubstring, SuperStringConcatenation

def test_valid_case():
    left_substr = SuperStringSubstring('Hello', 0, 5)
    right_substr = SuperStringSubstring('World!', 0, 5)
    concatenated = SuperStringConcatenation(left_substr, right_substr)
    
    assert concatenated.length() == 10
