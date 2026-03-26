
from dataclasses_json import stringcase

def pascalcase(string):
    """Convert a given string into PascalCase. The function first converts the input string to camel case using the `camelcase` function, and then capitalizes the first letter of each word in the camel case string.

    Args:
        string (str): The input string to be converted to PascalCase.

    Returns:
        str: A PascalCase formatted string.

    Examples:
        >>> pascalcase("hello_world")
        'HelloWorld'
        
        >>> pascalcase("PYTHON programming")
        'PythonProgramming'
        
        >>> pascalcase("123abc def")
        '123AbcDef'
        
        >>> pascalcase("-START-MIDDLE-END-")
        'StartMiddleEnd'
    """
    return stringcase.pascalcase(string)

def test_valid_input_123abc_def():
    assert pascalcase("123abc def") == "123AbcDef"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_pascalcase_1_test_valid_input_123abc_def.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_123abc_def __________________________

    def test_valid_input_123abc_def():
>       assert pascalcase("123abc def") == "123AbcDef"
E       AssertionError: assert '123abcDef' == '123AbcDef'
E         
E         - 123AbcDef
E         ?    ^
E         + 123abcDef
E         ?    ^

dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_pascalcase_1_test_valid_input_123abc_def.py:29: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_pascalcase_1_test_valid_input_123abc_def.py::test_valid_input_123abc_def
============================== 1 failed in 0.03s ===============================
"""