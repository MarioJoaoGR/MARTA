
import re
import pytest
from string_utils.validation import is_isbn_13

def test_valid_isbn_13():
    # Valid ISBN-13 numbers with hyphens
    assert is_isbn_13('9780312498580') == True
    assert is_isbn_13('978-0312498580') == True
    
    # Valid ISBN-13 numbers without hyphens
    assert is_isbn_13('9780312498580', normalize=False) == True
    
    # Invalid ISBN-13 numbers (wrong length, wrong format)
    assert is_isbn_13('978031249858') == False
    assert is_isbn_13('978-031249858') == False
    assert is_isbn_13('978031249858a') == False
    assert is_isbn_13('978-031249858a') == False
