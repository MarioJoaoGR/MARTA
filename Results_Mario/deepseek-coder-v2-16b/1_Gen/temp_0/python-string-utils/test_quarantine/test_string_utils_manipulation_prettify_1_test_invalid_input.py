
import pytest
from string_utils.manipulation import __StringFormatter

def prettify(input_string: str) -> str:
    """
    Reformat a string by applying basic grammar and formatting rules, including capitalization of the first letter after certain punctuation marks, spacing around quotes and brackets, and ensuring proper handling of arithmetic operators.

    This function ensures that the input string adheres to specific rules for spacing, capitalization, and punctuation. It also handles special cases such as arithmetic operators, quoted text, bracketed text, and percentage signs when preceded by numbers.

    *Examples:*

    >>> prettify(' unprettified string ,, like this one,will be"prettified" .it\\' s awesome! ')
    'Unprettified string, like this one, will be "prettified". It\'s awesome!'

    :param input_string: A string that needs to be manipulated according to specified rules.
    :return: The prettified string following the applied formatting rules.
    """
    formatted = __StringFormatter(input_string).format()
    return formatted

def test_invalid_input():
    # Test with invalid input types (numbers, lists, etc.)
    assert prettify(123) == "123"  # Should handle numbers gracefully
    assert prettify(None) is None  # Should handle None gracefully
    assert prettify([]) == ""      # Should handle empty list gracefully
    assert prettify({}) == ""      # Should handle empty dictionary gracefully
    
    # Test with invalid content (multiple spaces, trailing spaces, etc.)
    assert prettify("   unprettified string  ") == "Unprettified string"
    assert prettify("unprettified string,, like this one,") == "Unprettified string, like this one,"
    assert prettify('unprettified string ,, like this one,will be"prettified" .it\\\' s awesome! ') == 'Unprettified string, like this one, will be "prettified". It\'s awesome!'
    
    # Test with invalid characters (special characters, non-printable characters)
    assert prettify("\x00\x01\x02") == ""  # Should handle non-printable characters gracefully
    assert prettify("unprettified*string") == "Unprettified*string"  # Should handle special characters gracefully

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_prettify_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test with invalid input types (numbers, lists, etc.)
>       assert prettify(123) == "123"  # Should handle numbers gracefully

python-string-utils/Test4DT_tests/test_string_utils_manipulation_prettify_1_test_invalid_input.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
python-string-utils/Test4DT_tests/test_string_utils_manipulation_prettify_1_test_invalid_input.py:19: in prettify
    formatted = __StringFormatter(input_string).format()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <string_utils.manipulation.__StringFormatter object at 0x106861690>
input_string = 123

    def __init__(self, input_string):
        if not is_string(input_string):
>           raise InvalidInputError(input_string)
E           string_utils.errors.InvalidInputError: Expected "str", received "int"

python-string-utils/string_utils/manipulation.py:215: InvalidInputError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_prettify_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.03s ===============================

"""