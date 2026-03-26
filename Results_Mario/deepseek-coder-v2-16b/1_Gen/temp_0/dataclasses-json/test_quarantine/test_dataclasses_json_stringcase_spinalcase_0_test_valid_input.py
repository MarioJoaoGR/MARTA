
import re
from dataclasses_json import spinalcase
import pytest

def test_valid_input():
    assert spinalcase("Hello, World!") == "hello-world"
    assert spinalcase("This is a test.") == "this-is-a-test"
    assert spinalcase("Convert_This_To_Spinal_Case") == "convert-this-to-spinal-case"
    assert spinalcase("") == ""

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_stringcase_spinalcase_0_test_valid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_stringcase_spinalcase_0_test_valid_input.py:3:0: E0611: No name 'spinalcase' in module 'dataclasses_json' (no-name-in-module)

"""