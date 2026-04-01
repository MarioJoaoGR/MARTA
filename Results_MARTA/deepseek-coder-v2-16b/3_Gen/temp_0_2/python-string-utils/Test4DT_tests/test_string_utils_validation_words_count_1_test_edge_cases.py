
import pytest
from string_utils.validation import words_count, InvalidInputError

def test_edge_cases():
    # Test with a string containing no words (only punctuation)
    assert words_count("!@#$%^&*()") == 0
    
    # Test with an empty string
    assert words_count("") == 0
    
    # Test with a string containing only one letter or number without spaces
    assert words_count("hello") == 1
    assert words_count("world123") == 1
    
    # Test with a string where spaces are not used consistently for word separation
    assert words_count("one,two,three.stop") == 4
    
    # Test with a string containing multiple spaces between words
    assert words_count("one   two three") == 3
    
    # Test with a valid input string
    assert words_count("hello world") == 2
