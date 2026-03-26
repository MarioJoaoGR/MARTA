
import pytest
from your_module import capitalcase  # Replace 'your_module' with the actual module name where capitalcase function is defined

def test_non_string_input():
    assert capitalcase("hello, world!") == "Hello, world!"
    assert capitalcase("HELLO WORLD") == "Hello world"
    assert capitalcase("") == ""
    assert capitalcase(12345) == "12345"  # This should pass as the function returns the original string for non-string inputs

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_stringcase_capitalcase_0_test_non_string_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_capitalcase_0_test_non_string_input.py:3:0: E0401: Unable to import 'your_module' (import-error)


"""