
import pytest
from string_utils.validation import __ISBNChecker

def test_invalid_characters_isbn_13():
    # Test with invalid characters in ISBN-13 number
    checker = __ISBNChecker("9780470059028")  # Valid ISBN-13 without hyphens
    assert not checker.is_isbn_13(), "Expected False for valid ISBN-13"
    
    checker = __ISBNChecker("978-0-470-05902-8", normalize=False)  # Invalid ISBN-13 with hyphens
    assert not checker.is_isbn_13(), "Expected False for invalid ISBN-13"
    
    checker = __ISBNChecker("9780470059028a")  # Invalid character appended to valid ISBN-13
    assert not checker.is_isbn_13(), "Expected False for invalid ISBN-13 with extra characters"
    
    checker = __ISBNChecker("")  # Empty string should be invalid
    assert not checker.is_isbn_13(), "Expected False for empty input"
