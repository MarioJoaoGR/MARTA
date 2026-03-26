
import pytest
from docstring_parser import DocstringStyle, parse, add_attribute_docstrings
from docstring_parser.parser import DocstringParam
import inspect
import typing as T

def test_parse_from_object():
    class MyClass:
        """This is a class docstring."""
        def my_method(self):
            """This is a method docstring within the class."""
    
    parsed_doc = parse_from_object(MyClass)
    assert parsed_doc.short_description == "This is a class docstring."
    for param in parsed_doc.meta:
        if isinstance(param, DocstringParam):
            assert param.arg_name == "self"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_parser_parse_from_object_0_test_edge_case
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_from_object_0_test_edge_case.py:3:0: E0611: No name 'DocstringStyle' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_from_object_0_test_edge_case.py:3:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_from_object_0_test_edge_case.py:3:0: E0611: No name 'add_attribute_docstrings' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_from_object_0_test_edge_case.py:4:0: E0611: No name 'DocstringParam' in module 'docstring_parser.parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_from_object_0_test_edge_case.py:14:17: E0602: Undefined variable 'parse_from_object' (undefined-variable)


"""