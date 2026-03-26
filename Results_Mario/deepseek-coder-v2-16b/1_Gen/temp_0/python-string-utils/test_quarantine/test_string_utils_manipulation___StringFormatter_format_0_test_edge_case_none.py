
import pytest
from string_utils.manipulation import InvalidInputError, is_string

class __StringFormatter:
    """
    A class for formatting and validating input strings.

    The `__StringFormatter` class is designed to handle string inputs, ensuring they are valid strings before proceeding with any operations. It raises an `InvalidInputError` if the provided input is not a string.

    Parameters:
        input_string (str): A string that needs to be validated and potentially formatted. This parameter is required for instantiation of the class.

    Raises:
        InvalidInputError: If the provided `input_string` is not a string, this error will be raised with an appropriate message indicating the type of received data.

    Example Usage:
        >>> formatter = __StringFormatter("valid string")
        >>> print(formatter.input_string)  # Outputs: valid string
        
        >>> try:
        ...     bad_formatter = __StringFormatter(12345)  # This will raise InvalidInputError
        ... except InvalidInputError as e:
        ...     print(e)  # Outputs: Expected "str", received "int"
    """
    def __init__(self, input_string):
        if not is_string(input_string):
            raise InvalidInputError(input_string)

        self.input_string = input_string

    def format(self) -> str:
        # map of temporary placeholders
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

def test_edge_case_none():
    with pytest.raises(InvalidInputError):
        formatter = __StringFormatter(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:38:29: E1101: Instance of '__StringFormatter' has no '__placeholder_key' member (no-member)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:38:69: E0602: Undefined variable 'URLS_RE' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:39:29: E1101: Instance of '__StringFormatter' has no '__placeholder_key' member (no-member)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:39:66: E0602: Undefined variable 'EMAILS_RE' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:45:14: E0602: Undefined variable 'PRETTIFY_RE' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:45:56: E1101: Instance of '__StringFormatter' has no '__uppercase_first_char' member (no-member)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:46:14: E0602: Undefined variable 'PRETTIFY_RE' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:46:44: E1101: Instance of '__StringFormatter' has no '__remove_duplicates' member (no-member)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:47:14: E0602: Undefined variable 'PRETTIFY_RE' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:47:45: E1101: Instance of '__StringFormatter' has no '__ensure_right_space_only' member (no-member)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:48:14: E0602: Undefined variable 'PRETTIFY_RE' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:48:44: E1101: Instance of '__StringFormatter' has no '__ensure_left_space_only' member (no-member)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:49:14: E0602: Undefined variable 'PRETTIFY_RE' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:49:47: E1101: Instance of '__StringFormatter' has no '__ensure_spaces_around' member (no-member)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:50:14: E0602: Undefined variable 'PRETTIFY_RE' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:50:47: E1101: Instance of '__StringFormatter' has no '__remove_internal_spaces' member (no-member)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:51:14: E0602: Undefined variable 'PRETTIFY_RE' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:51:54: E1101: Instance of '__StringFormatter' has no '__uppercase_first_letter_after_sign' member (no-member)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:52:14: E0602: Undefined variable 'PRETTIFY_RE' (undefined-variable)
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_edge_case_none.py:52:48: E1101: Instance of '__StringFormatter' has no '__fix_saxon_genitive' member (no-member)

"""