
from string_utils.validation import InvalidInputError, is_string
import re

WORDS_COUNT_RE = re.compile(r'\b\w+\b')

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
        raise InvalidInputError(input_string)
    
    return len(WORDS_COUNT_RE.findall(input_string))

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
============================ no tests ran in 0.02s =============================
"""