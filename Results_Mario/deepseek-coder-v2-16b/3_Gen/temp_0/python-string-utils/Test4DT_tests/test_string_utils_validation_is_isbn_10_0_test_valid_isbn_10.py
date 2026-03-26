
import re
import pytest
from string_utils.validation import is_isbn_10

def test_valid_isbn_10():
    # Test cases for valid ISBN-10 numbers with hyphens
    assert is_isbn_10('1506715214') == True
    assert is_isbn_10('150-6715214') == True
    
    # Test cases for valid ISBN-10 numbers without hyphens
    assert is_isbn_10('1506715214', normalize=False) == True
    assert is_isbn_10('150-6715214', normalize=False) == False
    
    # Additional test cases for invalid ISBN-10 numbers
    assert is_isbn_10('9780470059028') == False  # Invalid because it's an ISBN-13
    assert is_isbn_10('1506715215') == False     # Invalid because the check digit doesn't match
    assert is_isbn_10('150-6715215') == False   # Invalid because it contains hyphens and the number isn't valid
