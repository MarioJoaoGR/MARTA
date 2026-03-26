
import re
from dataclasses_json.stringcase import camelcase as dc_camelcase

def camelcase(string):
    """ Convert a given string into camel case.

    Args:
        string (str): The input string to be converted to camel case.

    Returns:
        str: A camel case version of the input string.

    Examples:
        >>> camelcase("hello_world")
        'HelloWorld'
        
        >>> camelcase("camelCaseExample")
        'CamelCaseExample'
        
        >>> camelcase("snake_case_to_camel_case")
        'SnakeCaseToCamelCase'
        
        >>> camelcase("")
        ''
    """
    return dc_camelcase(string)

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