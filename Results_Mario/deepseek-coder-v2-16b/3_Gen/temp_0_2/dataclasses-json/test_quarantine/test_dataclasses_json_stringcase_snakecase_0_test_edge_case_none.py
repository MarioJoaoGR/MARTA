
import re
from dataclasses_json import stringcase

def snakecase(string):
    """Convert a given string into snake case. This involves replacing hyphens, dots, and spaces with underscores and ensuring the first character is lowercase while subsequent words are joined by underscores.

    Args:
        string (str): The input string to be converted into snake case.

    Returns:
        str: The snake cased version of the input string. If the input string is empty, it returns an empty string.

    Example:
        >>> snakecase("HelloWorld")
        'hello_world'
        
        >>> snakecase("Hello-World")
        'hello_world'
        
        >>> snakecase("Hello World")
        'hello_world'
        
        >>> snakecase("")
        ''
    """
    if not string:
        return string
    
    # Replace hyphens, dots, and spaces with underscores
    string = re.sub(r"[\-\.\s]", '_', str(string))
    
    # Convert the first character to lowercase
    result = string[0].lower() + re.sub(r"[A-Z]", lambda matched: '_' + matched.group(0).lower(), string[1:])
    
    return result

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
============================ no tests ran in 0.02s =============================
"""