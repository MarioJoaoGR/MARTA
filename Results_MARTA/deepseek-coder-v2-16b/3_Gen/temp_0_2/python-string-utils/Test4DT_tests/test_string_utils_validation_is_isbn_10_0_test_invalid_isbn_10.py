
import re
import pytest
from string_utils.validation import is_isbn_10

def test_invalid_isbn_10():
    # Test cases for invalid ISBN-10 numbers
    invalid_cases = [
        "123456789",          # Incorrect length (too short)
        "123456789X0",        # Incorrect length (too long)
        "123456789-X",        # Contains hyphens but incorrect length
        "123456789X-",        # Contains hyphens but incorrect length
        "12345678901 ",       # Trailing space
        " 12345678901",       # Leading space
        "123456789-0X",       # Hyphen and 'X' in the middle
        "1234567890X-",       # 'X' and hyphen at the end
        "1234567890X-1",      # Extra digit after 'X' and hyphen
        "ABCDEFGHIJ",         # All alphabetic characters
        "1234567890!",        # Invalid character (exclamation mark)
        "1234567890.",        # Invalid character (period)
    ]
    
    for case in invalid_cases:
        assert not is_isbn_10(case), f"Expected {case} to be invalid, but it was recognized as valid."
