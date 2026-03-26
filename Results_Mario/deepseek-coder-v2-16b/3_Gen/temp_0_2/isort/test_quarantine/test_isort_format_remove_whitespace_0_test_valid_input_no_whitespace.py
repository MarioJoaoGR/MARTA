
import re

def remove_whitespace(content: str, line_separator: str = "\n") -> str:
    """
    Removes all whitespace characters from the input string, including spaces and form feed characters. The function is designed to handle various line separators such as newline ("\n"), horizontal tab ("\t"), vertical tab ("\v"), form feed ("\f"), carriage return ("\r"), and next line ("\x0b").
    
    Parameters:
        content (str): The input string from which to remove whitespace characters.
        line_separator (str, optional): A string that represents the character used to separate lines in the input content. Defaults to "\n".
        
    Returns:
        str: A new string with all whitespace characters removed.
    
    Examples:
        >>> remove_whitespace("Hello, World!")
        'Hello,World!'
        
        >>> remove_whitespace("This is a test.\nThis is only a test.", "\n")
        'Thisisatest.Thisisonlyateast.'
        
        >>> remove_whitespace("No changes here  ", " ")
        'Nochangeshere'
    """
    # Remove all whitespace characters including spaces, tabs, newlines, etc.
    content = re.sub(r'\s+', '', content)
    
    return content

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.05s =============================
"""