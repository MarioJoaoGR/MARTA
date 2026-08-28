
import pytest
from string_utils.validation import is_email

def test_valid_emails():
    assert is_email('my.email@the-provider.com')
    assert is_email('user.name+tag+sorting@example.com')
    assert is_email('user@sub.example.com')