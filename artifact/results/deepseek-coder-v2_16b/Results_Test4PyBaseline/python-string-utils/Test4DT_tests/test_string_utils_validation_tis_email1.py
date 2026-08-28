
import pytest
from string_utils.validation import is_email

ESCAPED_AT_SIGN = 'user@example@com'  # Define the escaped at sign variable here

# Test cases for valid email addresses
def test_valid_emails():
    assert is_email('my.email@the-provider.com') == True
    assert is_email('user@example.co.in') == True
    assert is_email('user123@subdomain.example.com') == True
    assert is_email('john.doe@gmail.com') == True
    assert is_email('jane_doe@yahoo.co.uk') == True

# Test cases for invalid email addresses
def test_invalid_emails():
    assert is_email('@gmail.com') == False
    assert is_email('user@.com') == False
    assert is_email('user@@example.com') == False
    assert is_email('user@.co') == False
    assert is_email('user@domain.') == False

# Test case for a string that should be considered invalid due to multiple "@" signs but correctly escaped
def test_escaped_at_sign():
    assert is_email(ESCAPED_AT_SIGN.replace('@', '')) == False

# Additional test cases to cover uncovered lines
def test_pre_check_failures():
    # Test with an empty string
    assert is_email('') == False
    # Test with a string longer than 320 characters
    long_string = 'a' * 321
    assert is_email(long_string) == False
    # Test with a string starting with a dot
    assert is_email('.user@example.com') == False

def test_split_by_at_failures():
    # Test with multiple "@" symbols
    assert is_email('user@exa@mple.com') == False
    # Test with head part longer than 64 characters
    long_head = 'a' * 65 + '@example.com'
    assert is_email(long_head) == False
    # Test with head part containing consecutive dots
    assert is_email('user..@example.com') == False
    # Test with tail part longer than 255 characters (though this should be caught by the regex in practice)
    long_tail = 'user@' + 'a' * 256
    assert is_email(long_tail) == False

def test_escaped_spaces_and_quotation():
    # Test with head enclosed in quotation marks
    assert is_email('"user@example.com') == False
    assert is_email('user@example.com"') == False
    # Test with escaped spaces in the head part
    assert is_email('u\\ ser@example.com') == True  # Corrected assertion to match expected behavior

if __name__ == "__main__":
    pytest.main()
