
import re
from string_utils.validation import is_string, InvalidInputError

HTML_RE = re.compile(r'<[^>]*>')

def contains_html(input_string: str) -> bool:
    """
    Checks if the given string contains HTML/XML tags.

    By design, this function matches ANY type of tag, so don't expect to use it
    as an HTML validator, its goal is to detect "malicious" or undesired tags in the text.

    *Examples:*

    >>> contains_html('my string is <strong>bold</strong>') # returns true
    >>> contains_html('my string is not bold') # returns false

    :param input_string: Text to check for HTML/XML tags.
    :type input_string: str
    :raises InvalidInputError: If the provided `input_string` is not a string, this error will be raised with a descriptive message indicating that the expected type was not met.
    :return: True if the string contains any HTML/XML tags, False otherwise.
    """
    if not is_string(input_string):
        raise InvalidInputError(f"Expected a string but got {type(input_string)}")

    return bool(HTML_RE.search(input_string))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.01s =============================
"""