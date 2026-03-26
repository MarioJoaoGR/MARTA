
from string_utils.validation import is_isogram

def test_empty_string():
    assert not is_isogram("")
