
import re
import pytest
from string_utils.validation import is_isbn_13

def test_valid_isbn_13():
    # Valid ISBN-13 numbers with hyphens
    assert is_isbn_13('9780312498580') == True
    assert is_isbn_13('978-0312498580') == True
    
    # Valid ISBN-13 numbers without hyphens
    assert is_isbn_13('9780312498580', normalize=False) == True
    assert is_isbn_13('978-0312498580', normalize=False) == False
    
    # Invalid ISBN-13 numbers
    assert is_isbn_13('978031249858') == False  # Missing check digit
    assert is_isbn_13('97803124985801') == False  # Invalid length and missing check digit
