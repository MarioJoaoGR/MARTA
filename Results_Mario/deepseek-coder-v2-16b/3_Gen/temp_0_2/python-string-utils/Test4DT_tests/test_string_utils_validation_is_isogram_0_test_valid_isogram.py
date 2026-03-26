
from string_utils.validation import is_isogram

def test_valid_isogram():
    assert is_isogram('dermatoglyphics') == True
    assert is_isogram('hello') == False
