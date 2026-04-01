
from string_utils.manipulation import slugify, InvalidInputError

def test_edge_case_none():
    try:
        result = slugify(None)
        assert result is None
    except InvalidInputError as e:
        assert str(e) == "Expected 'str', received 'NoneType'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_slugify_2_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        try:
>           result = slugify(None)

python-string-utils/Test4DT_tests/test_string_utils_manipulation_slugify_2_test_edge_case_none.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_string = None, separator = '-'

    def slugify(input_string: str, separator: str = '-') -> str:
        """
        Converts a string into a "slug" using provided separator.
        The returned string has the following properties:
    
        - it has no spaces
        - all letters are in lower case
        - all punctuation signs and non alphanumeric chars are removed
        - words are divided using provided separator
        - all chars are encoded as ascii (by using `asciify()`)
        - is safe for URL
    
        *Examples:*
    
        >>> slugify('Top 10 Reasons To Love Dogs!!!') # returns: 'top-10-reasons-to-love-dogs'
        >>> slugify('Mönstér Mägnët') # returns 'monster-magnet'
    
        :param input_string: String to convert.
        :type input_string: str
        :param separator: Sign used to join string tokens (default to "-").
        :type separator: str
        :return: Slug string
        """
        if not is_string(input_string):
>           raise InvalidInputError(input_string)
E           string_utils.errors.InvalidInputError: Expected "str", received "NoneType"

python-string-utils/string_utils/manipulation.py:486: InvalidInputError

During handling of the above exception, another exception occurred:

    def test_edge_case_none():
        try:
            result = slugify(None)
            assert result is None
        except InvalidInputError as e:
>           assert str(e) == "Expected 'str', received 'NoneType'"
E           assert 'Expected "st...ed "NoneType"' == "Expected 'st...ed 'NoneType'"
E             
E             - Expected 'str', received 'NoneType'
E             ?          ^   ^           ^        ^
E             + Expected "str", received "NoneType"
E             ?          ^   ^           ^        ^

python-string-utils/Test4DT_tests/test_string_utils_manipulation_slugify_2_test_edge_case_none.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_slugify_2_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.03s ===============================
"""