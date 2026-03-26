
# Module: string_utils.validation
from string_utils.validation import is_palindrome
import re

# Assuming SPACES_RE is defined somewhere in the module, we can use it for testing with spaces ignored.
SPACES_RE = re.compile(r'\s+')

def test_is_palindrome_empty_string():
    assert not is_palindrome('')  # Empty string should not be a palindrome

def test_is_palindrome_not_full_string():
    assert not is_palindrome('ab', ignore_spaces=False, ignore_case=False)  # Not full string should return False

def test_is_palindrome_with_spaces_and_case():
    assert not is_palindrome('i topi non avevano nipoti', ignore_spaces=False, ignore_case=False)  # Case and spaces matter here

def test_is_palindrome_with_spaces_ignored():
    assert is_palindrome('i topi non avevano nipoti', ignore_spaces=True, ignore_case=False)  # Spaces are ignored but case matters

def test_is_palindrome_case_insensitive():
    assert is_palindrome('Lol', ignore_spaces=False, ignore_case=True)  # Case is ignored and should return True

def test_is_palindrome_with_mixed_case():
    assert not is_palindrome('Aba', ignore_spaces=False, ignore_case=False)  # Mixed case should return False

def test_is_palindrome_with_all_lowercase():
    assert is_palindrome('aba', ignore_spaces=False, ignore_case=True)  # All lowercase and spaces ignored should return True
