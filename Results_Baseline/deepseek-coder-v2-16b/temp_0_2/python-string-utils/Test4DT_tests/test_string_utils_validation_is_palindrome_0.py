# Module: string_utils.validation
# Import the function using its provided module name.
from string_utils.validation import is_palindrome

def test_is_palindrome_simple():
    assert is_palindrome('LOL') == True

def test_is_palindrome_case_insensitive():
    assert is_palindrome('Lol', ignore_case=True) == True

def test_is_palindrome_not_palindrome():
    assert is_palindrome('ROTFL') == False

def test_is_palindrome_with_spaces_ignored():
    assert is_palindrome('i topi non avevano nipoti', ignore_spaces=True) == True
