
from string_utils.validation import words_count, InvalidInputError
import re

# Assuming WORDS_COUNT_RE is defined somewhere in the validation module
WORDS_COUNT_RE = re.compile(r'\b\w+\b')

def test_invalid_input():
    # Test with non-string input
    try:
        words_count(12345)
    except InvalidInputError as e:
        assert str(e) == "Expected 'str', received 'int'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_words_count_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test with non-string input
        try:
>           words_count(12345)

python-string-utils/Test4DT_tests/test_string_utils_validation_words_count_2_test_invalid_input.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_string = 12345

    def words_count(input_string: str) -> int:
        """
        Returns the number of words contained into the given string.
    
        This method is smart, it does consider only sequence of one or more letter and/or numbers
        as "words", so a string like this: "! @ # % ... []" will return zero!
        Moreover it is aware of punctuation, so the count for a string like "one,two,three.stop"
        will be 4 not 1 (even if there are no spaces in the string).
    
        *Examples:*
    
        >>> words_count('hello world') # returns 2
        >>> words_count('one,two,three.stop') # returns 4
    
        :param input_string: String to check.
        :type input_string: str
        :return: Number of words.
        """
        if not is_string(input_string):
>           raise InvalidInputError(input_string)
E           string_utils.errors.InvalidInputError: Expected "str", received "int"

python-string-utils/string_utils/validation.py:596: InvalidInputError

During handling of the above exception, another exception occurred:

    def test_invalid_input():
        # Test with non-string input
        try:
            words_count(12345)
        except InvalidInputError as e:
>           assert str(e) == "Expected 'str', received 'int'"
E           assert 'Expected "st...eceived "int"' == "Expected 'st...eceived 'int'"
E             
E             - Expected 'str', received 'int'
E             ?          ^   ^           ^   ^
E             + Expected "str", received "int"
E             ?          ^   ^           ^   ^

python-string-utils/Test4DT_tests/test_string_utils_validation_words_count_2_test_invalid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_words_count_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.04s ===============================
"""