
import re
from string_utils.manipulation import __StringFormatter
from unittest.mock import patch

# Define the regex patterns for URLs and emails if they are not already defined in your module
URLS_RE = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
EMAILS_RE = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

def test_format_valid_input():
    # Create a mock input string containing URLs and emails
    input_string = "Initial string with URLs and emails like http://example.com and test@test.com."
    
    # Instantiate the StringFormatter with the mock input string
    formatter = __StringFormatter(input_string)
    
    # Call the format method to get the formatted output
    formatted = formatter.format()
    
    # Assert that the output is a string
    assert isinstance(formatted, str), "The output should be a string"
    
    # Use regex to check if URLs are replaced with placeholders
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    assert pattern.search(formatted) is None, "URLs should be replaced with placeholders"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
___________________________ test_format_valid_input ____________________________

    def test_format_valid_input():
        # Create a mock input string containing URLs and emails
        input_string = "Initial string with URLs and emails like http://example.com and test@test.com."
    
        # Instantiate the StringFormatter with the mock input string
        formatter = __StringFormatter(input_string)
    
        # Call the format method to get the formatted output
        formatted = formatter.format()
    
        # Assert that the output is a string
        assert isinstance(formatted, str), "The output should be a string"
    
        # Use regex to check if URLs are replaced with placeholders
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
>       assert pattern.search(formatted) is None, "URLs should be replaced with placeholders"
E       AssertionError: URLs should be replaced with placeholders
E       assert <re.Match object; span=(41, 59), match='http://example.com'> is None
E        +  where <re.Match object; span=(41, 59), match='http://example.com'> = <built-in method search of re.Pattern object at 0x106651670>('Initial string with URLs and emails like http://example.com and test@test.com.')
E        +    where <built-in method search of re.Pattern object at 0x106651670> = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\\\(\\\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+').search

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_valid_input.py:25: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_valid_input.py::test_format_valid_input
============================== 1 failed in 0.02s ===============================
"""