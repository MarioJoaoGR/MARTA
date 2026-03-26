
import pytest
from docstring_parser.parser import parse_from_object, DocstringStyle
from docstring_parser.structures import Docstring
import inspect
import typing as T

def test_valid_class_input():
    class MyClass:
        """This is a class docstring."""
        def __init__(self):
            pass
    
    parsed_class = parse_from_object(MyClass)
    assert parsed_class.short_description == "This is a class docstring."

def test_valid_module_input():
    import math
    parsed_module = parse_from_object(math)
    for param in parsed_module.meta:
        print(f"Parameter: {param.arg_name}, Type: {param.type}")  # Output will list all attribute docstrings of the module

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_parser_parse_from_object_0_test_valid_class_input
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_from_object_0_test_valid_class_input.py:4:0: E0401: Unable to import 'docstring_parser.structures' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_from_object_0_test_valid_class_input.py:4:0: E0611: No name 'structures' in module 'docstring_parser' (no-name-in-module)


"""