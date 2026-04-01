
import pytest
from string_utils.manipulation import InvalidInputError, URLS_RE, EMAILS_RE, PRETTIFY_RE

class __StringFormatter:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise InvalidInputError(f"Expected a string but got {type(input_string).__name__}")
        self.input_string = input_string

    def format(self) -> str:
        placeholders = {}
        out = self.input_string

        placeholders.update({self.__placeholder_key(): m[0] for m in URLS_RE.findall(out)})
        placeholders.update({self.__placeholder_key(): m for m in EMAILS_RE.findall(out)})

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

        for p in placeholders:
            out = out.replace(p, placeholders[p], 1)

        return out

    def __placeholder_key(self):
        return f"${{{''.join(random.choices(string.ascii_lowercase + string.digits, k=20))}}}$"

    def __uppercase_first_char(self, match):
        return match.group(0).capitalize()

    def __remove_duplicates(self, match):
        return ''.join(dict.fromkeys(match.group(0)))

    def __ensure_right_space_only(self, match):
        return match.group(0) + ' ' if match.end() == len(match.string) or not match.string[match.end()].isspace() else match.group(0)

    def __ensure_left_space_only(self, match):
        return ' ' + match.group(0) if match.start() == 0 or not match.string[match.start() - 1].isspace() else match.group(0)

    def __ensure_spaces_around(self, match):
        return ' ' + match.group(0).replace(' ', ' ') + ' '

    def __remove_internal_spaces(self, match):
        return match.group(0).replace(' ', '')

    def __uppercase_first_letter_after_sign(self, match):
        sign = match.string[match.start() - 1]
        rest = match.group(0)[1:]
        return f"{sign}{rest.capitalize()}"

    def __fix_saxon_genitive(self, match):
        words = match.group(0).split()
        if len(words) > 1:
            words[-1] += "'"
        return ' '.join(words)

@pytest.mark.parametrize("input_string", [None])
def test_edge_case_none(input_string):
    with pytest.raises(InvalidInputError):
        formatter = __StringFormatter(input_string)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter_format_1_test_edge_case_none
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_1_test_edge_case_none.py:37:29: E0602: Undefined variable 'random' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_1_test_edge_case_none.py:37:44: E0602: Undefined variable 'string' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_1_test_edge_case_none.py:37:69: E0602: Undefined variable 'string' (undefined-variable)


"""