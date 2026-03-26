
# Module: docstring_parser.tests.test_parse_from_object
import pytest
from docstring_parser.tests import test_parse_from_object

def test_a_function_default():
    assert test_parse_from_object.a_function("Hello") == 'Hello 2'

def test_a_function_with_param2():
    assert test_parse_from_object.a_function("Hello", 3) == 'Hello 3'

def test_a_function_swapped_params():
    assert test_parse_from_object.a_function(param2=5, param1="Hi") == 'Hi 5'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_parse_from_object_a_function_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_a_function_0.py:7:11: E1101: Module 'docstring_parser.tests.test_parse_from_object' has no 'a_function' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_a_function_0.py:10:11: E1101: Module 'docstring_parser.tests.test_parse_from_object' has no 'a_function' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_parse_from_object_a_function_0.py:13:11: E1101: Module 'docstring_parser.tests.test_parse_from_object' has no 'a_function' member (no-member)

"""