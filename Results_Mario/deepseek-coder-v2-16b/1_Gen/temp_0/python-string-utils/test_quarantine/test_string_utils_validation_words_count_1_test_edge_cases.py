
import re
from string_utils.validation import is_string, InvalidInputError

WORDS_COUNT_RE = re.compile(r'\b\w+\b')

def words_count(input_string: str) -> int:
    """
    Returns the number of words contained into the given string.
    
    This method considers sequences of one or more letters and/or numbers as "words", ignoring punctuation and other non-alphanumeric characters. It is aware that a sequence of alphanumeric characters separated by punctuation can be considered a word.
    
    *Examples:*
    
    - For the string `'hello world'`, the function will return `2`.
    - For the string `'one,two,three.stop'`, the function will return `4`.
    
    :param input_string: The string to analyze for word count. This should be a sequence of letters and/or numbers with optional punctuation in between.
    :type input_string: str
    :return: The number of words identified in the input string based on the criteria described.
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