
import re
from dataclasses_json.stringcase import uplowcase

def snakecase(string):
    """Convert a given string into snake case. This involves replacing hyphens, dots, and spaces with underscores and ensuring the first character is lowercase while subsequent words are joined by underscores.

    Args:
        string (str): The input string to be converted to snake case.

    Returns:
        str: The snake cased version of the input string.

    Examples:
        >>> snakecase("Hello, World!")
        'hello_world'
        
        >>> snakecase("This is a test.")
        'this_is_a_test'
        
        >>> snakecase("Convert-This-To-Snake-Case")
        'convert_to_snake_case'
        
        >>> snakecase("")
        ''
    """
    string = re.sub(r"[\-\.\s]", '_', str(string))
    if not string:
        return string
    return (uplowcase(string[0], 'low')
            + re.sub(r"[A-Z0-9]",
                     lambda matched: '_' + uplowcase(matched.group(0), 'low'),
                     string[1:]))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.03s =============================

"""