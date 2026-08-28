
# Module: string_utils.validation
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

if __name__ == "__main__":
    pytest.main()
