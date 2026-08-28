
import pytest
from string_utils.validation import is_email

def test_is_email_basic():
    # Test a basic valid email address
    assert is_email('my.email@the-provider.com') == True
