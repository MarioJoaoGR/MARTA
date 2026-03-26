
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError

# Mocking the required modules and functions
URLS_RE = type('URLs', (object,), {'findall': lambda self, s: []})()
EMAILS_RE = type('Emails', (object,), {'findall': lambda self, s: []})()
PRETTIFY_RE = {
    'UPPERCASE_FIRST_LETTER': type('UppercaseFirstLetter', (object,), {'sub': lambda self, func, s: func(s)})(),
    'DUPLICATES': type('Duplicates', (object,), {'sub': lambda self, func, s: func(s)})(),
    'RIGHT_SPACE': type('RightSpace', (object,), {'sub': lambda self, func, s: func(s)})(),
    'LEFT_SPACE': type('LeftSpace', (object,), {'sub': lambda self, func, s: func(s)})(),
    'SPACES_AROUND': type('SpacesAround', (object,), {'sub': lambda self, func, s: func(s)})(),
    'SPACES_INSIDE': type('SpacesInside', (object,), {'sub': lambda self, func, s: func(s)})(),
    'UPPERCASE_AFTER_SIGN': type('UppercaseAfterSign', (object,), {'sub': lambda self, func, s: func(s)})(),
    'SAXON_GENITIVE': type('SaxonGenitive', (object,), {'sub': lambda self, func, s: func(s)})()
}

def test_valid_input():
    input_string = "This is a valid string."
    formatter = __StringFormatter(input_string)
    
    assert formatter.input_string == input_string

def test_invalid_input():
    with pytest.raises(InvalidInputError):
        __StringFormatter(12345)

def test_format_valid_string():
    input_string = "This is a valid string."
    formatter = __StringFormatter(input_string)
    
    formatted_string = formatter.format()
    assert isinstance(formatted_string, str)

# Mocking the necessary methods for testing format method
class Test__StringFormatter:
    def __placeholder_key(self):
        return "$1"
    
    def __uppercase_first_char(self, s):
        return s.capitalize()
    
    def __remove_duplicates(self, s):
        return "".join(dict.fromkeys(s))
    
    def __ensure_right_space_only(self, s):
        return s.rstrip() + " "
    
    def __ensure_left_space_only(self, s):
        return " " + s.lstrip()
    
    def __ensure_spaces_around(self, s):
        return " " + s.replace(" ", "  ") + " "
    
    def __remove_internal_spaces(self, s):
        return s.replace(" ", "")
    
    def __uppercase_first_letter_after_sign(self, s):
        return s.replace(".", ". ").capitalize()
    
    def __fix_saxon_genitive(self, s):
        return s.replace("'", "'s")

# Injecting the mocked methods into the formatter for testing
formatter = Test__StringFormatter()
formatter.__placeholder_key = lambda: "$1"
formatter.__uppercase_first_char = lambda s: s.capitalize()
formatter.__remove_duplicates = lambda s: "".join(dict.fromkeys(s))
formatter.__ensure_right_space_only = lambda s: s.rstrip() + " "
formatter.__ensure_left_space_only = lambda s: " " + s.lstrip()
formatter.__ensure_spaces_around = lambda s: " " + s.replace(" ", "  ") + " "
formatter.__remove_internal_spaces = lambda s: s.replace(" ", "")
formatter.__uppercase_first_letter_after_sign = lambda s: s.replace(".", ". ").capitalize()
formatter.__fix_saxon_genitive = lambda s: s.replace("'", "'s")

# Running the tests
if __name__ == "__main__":
    pytest.main()
