
import pytest
from string_utils.validation import is_email

def test_valid_emails():
    assert is_email('my.email@the-provider.com')
    assert is_email('user.name+tag+sorting@example.com')
    assert is_email('user@sub.example.com')

def test_invalid_emails():
    # Basic checks
    assert not is_email('')
    assert not is_email('@gmail.com')
    assert not is_email('.startwithdot@domain.com')
    assert not is_email('toolong' * 32 + '@example.com')  # > 320 characters

    # Head and tail constraints
    assert not is_email('a' * 65 + '@example.com')  # head too long
    assert not is_email('user@' + 'a' * 256)  # tail too long
    assert not is_email('dot.@domain.com')
    assert not is_email('double..dot@domain.com')

    # Escaping and quoting
    assert is_email('first\\ last@example.com')  # escaped space in head
    assert is_email('"first last"@example.com')  # quoted local part with spaces

    # Multiple '@' signs
    assert not is_email('user@domain@com')
    assert not is_email('user\\@domain@com')  # escaped '@'
    assert not is_email('user@domain\\@com')  # escaped '@' in tail

def test_regex_matching():
    # Test cases based on EMAIL_RE pattern
    assert is_email('valid.email+tag@sub.domain.com')
    assert not is_email('invalid-email@domain,com')  # invalid character ',' in domain part

# Additional test cases to cover uncovered lines

def test_uncovered_line_221():
    # Test non-string input
    assert not is_email(None)
    assert not is_email(0)
    assert not is_email([])
    assert not is_email({})

    # Test string with length > 320
    assert not is_email('a' * 321 + '@example.com')

    # Test string starting with a dot
    assert not is_email('.invalid@domain.com')

def test_uncovered_line_229():
    # Test head too long
    assert not is_email('a' * 65 + '@example.com')

    # Test tail too long
    assert not is_email('user@' + 'a' * 256)

    # Test head ending with a dot
    assert not is_email('dot.@domain.com')

    # Test head with consecutive dots