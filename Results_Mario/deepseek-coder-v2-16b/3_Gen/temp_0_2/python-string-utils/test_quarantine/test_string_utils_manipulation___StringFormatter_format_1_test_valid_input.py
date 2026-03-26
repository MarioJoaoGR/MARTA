
import re
from string_utils.manipulation import URLS_RE, EMAILS_RE, PRETTIFY_RE
from unittest.mock import patch

class InvalidInputError(Exception):
    pass

class __StringFormatter:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise InvalidInputError(input_string)
        self.input_string = input_string

    def format(self) -> str:
        placeholders = {}
        out = self.input_string

        # looks for url or email and updates placeholders map with found values
        placeholders.update({self.__placeholder_key(): m[0] for m in URLS_RE.findall(out)})
        placeholders.update({self.__placeholder_key(): m for m in EMAILS_RE.findall(out)})

        # replace original value with the placeholder key
        for p in placeholders:
            out = out.replace(placeholders[p], p, 1)

        out = PRETTIFY_RE['UPPERCASE_FIRST_LETTER'].sub(self.__uppercase_first_char, out)
        out = PRETTIFY_RE['DUPLICATES'].sub(self.__remove_duplicates, out)
        out = PRETTIFY_RE['RIGHT_SPACE'].sub(self.__ensure_right_space_only, out)
        out = PRETTIFY_RE['LEFT_SPACE'].sub(self.__ensure_left_space_only, out)
        out = PRETTIFY_RE['SPACES_AROUND'].sub(self.__ensure_spaces_around, out)
        out = PRETTIFY_RE['SPACES_INSIDE'].sub(self.__remove_internal_spaces, out)
        out = PRETTIFY_RE['UPPERCASE_AFTER_SIGN'].sub(self.__uppercase_first_letter_after_sign, out)
        out = PRETTIFY_RE['SAXON_GENITIVE'].sub(self.__fix_saxon_genitive, out)
        out = out.strip()

        # restore placeholder keys with their associated original value
        for p in placeholders:
            out = out.replace(p, placeholders[p], 1)

        return out

    def __placeholder_key(self):
        return f"${len(placeholders)}$"

    def __uppercase_first_char(self, match):
        return match.group(0).capitalize()

    def __remove_duplicates(self, match):
        return match.group(0).replace(" ", "")

    def __ensure_right_space_only(self, match):
        return match.group(0) + " "

    def __ensure_left_space_only(self, match):
        return " " + match.group(0)

    def __ensure_spaces_around(self, match):
        return " " + match.group(0).replace(" ", " ") + " "

    def __remove_internal_spaces(self, match):
        return match.group(0).replace(" ", "")

    def __uppercase_first_letter_after_sign(self, match):
        sign = match.group(0)[-1]
        rest = match.group(0)[:-1]
        return sign + rest.capitalize()

    def __fix_saxon_genitive(self, match):
        words = match.group(0).split()
        if len(words) > 1:
            words[-1] += "'"
        return " ".join(words)

import pytest

@pytest.fixture
def formatter():
    input_string = "This is a test string with an email example@example.com and a URL http://example.com."
    return __StringFormatter(input_string)

def test_valid_input(formatter):
    formatted_string = formatter.format()
    assert isinstance(formatted_string, str), "The output should be a string"
    assert len(formatted_string) > 0, "The output string should not be empty"
    # Add more assertions to check specific parts of the formatted string if needed

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter_format_1_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_1_test_valid_input.py:44:23: E0602: Undefined variable 'placeholders' (undefined-variable)


"""