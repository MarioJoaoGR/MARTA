
import re
import pytest
from string_utils.validation import is_email, EMAIL_RE, ESCAPED_AT_SIGN

def test_invalid_length():
    # Test case for a local part that exceeds the maximum length allowed (64 characters)
    assert not is_email('a' * 65 + '@gmail.com')
    
    # Test case for an invalid email due to multiple "@" signs
    assert not is_email('my@email@provider.com')
    
    # Test case for an invalid email due to starting with a dot
    assert not is_email('.myemail@provider.com')
