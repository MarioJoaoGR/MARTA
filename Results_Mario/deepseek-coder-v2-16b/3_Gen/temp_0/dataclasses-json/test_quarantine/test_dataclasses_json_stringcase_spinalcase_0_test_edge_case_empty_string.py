
import re
from dataclasses_json import stringcase

def spinalcase(string):
    """Convert a given string into spinal case. This involves replacing spaces, dots, and underscores with hyphens and ensuring the first character is lowercase while subsequent words are joined by hyphens.

    Args:
        string (str): The input string to be converted to spinal case.

    Returns:
        str: The spinal cased version of the input string.

    Examples:
        >>> spinalcase("Hello, World!")
        'hello-world'
        
        >>> spinalcase("This is a test.")
        'this-is-a-test'
        
        >>> spinalcase("Convert_This_To_Spinal_Case")
        'convert-this-to-spinal-case'
        
        >>> spinalcase("")
        ''
    """
    if not string:
        return ""
    # Convert the string to snake case first, then replace underscores with hyphens
    snake_case_string = re.sub(r"_", "-", stringcase(string))
    return snake_case_string

import pytest

@pytest.mark.parametrize("input_string, expected_output", [
    ("Hello, World!", "hello-world"),
    ("This is a test.", "this-is-a-test"),
    ("Convert_This_To_Spinal_Case", "convert-this-to-spinal-case"),
    ("", "")
])
def test_edge_case_empty_string(input_string, expected_output):
    assert spinalcase(input_string) == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_stringcase_spinalcase_0_test_edge_case_empty_string
dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_spinalcase_0_test_edge_case_empty_string.py:30:42: E1102: stringcase is not callable (not-callable)


"""