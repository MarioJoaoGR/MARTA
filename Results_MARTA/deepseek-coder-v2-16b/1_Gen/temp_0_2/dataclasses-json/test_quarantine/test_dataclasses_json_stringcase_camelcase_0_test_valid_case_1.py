
import re
from stringcase import camelcase as str_camelcase

def camelcase(string):
    """ Convert a given string into camel case format.

    Args:
        string (str): The input string to be converted to camel case.

    Returns:
        str: A camel case formatted string.

    Examples:
        >>> camelcase("hello_world")
        'HelloWorld'
        
        >>> camelcase("PYTHON programming")
        'PythonProgramming'
        
        >>> camelcase("123abc def")
        '123AbcDef'
        
        >>> camelcase("-START-MIDDLE-END-")
        'StartMiddleEnd'
    """
    return str_camelcase(string)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_stringcase_camelcase_0_test_valid_case_1
dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_camelcase_0_test_valid_case_1.py:3:0: E0401: Unable to import 'stringcase' (import-error)


"""