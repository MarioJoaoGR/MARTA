
import pytest
import inspect
import typing as T
from docstring_parser import Docstring, DocstringStyle, parse, add_attribute_docstrings

def test_parse_from_object_basic():
    class MyClass:
        """This is a class docstring."""
        def my_method(self):
            """This is a method docstring within the class."""
    
    parsed_doc = parse_from_object(MyClass)
    assert parsed_doc.short_description == "This is a class docstring."
    assert len(parsed_doc.params) == 1
    param = parsed_doc.params[0]
    assert param.arg_name == "self"
    assert param.type_name == "<class 'self'>"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_parser_parse_from_object_0_test_parse_from_object_basic
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_from_object_0_test_parse_from_object_basic.py:5:0: E0611: No name 'Docstring' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_from_object_0_test_parse_from_object_basic.py:5:0: E0611: No name 'DocstringStyle' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_from_object_0_test_parse_from_object_basic.py:5:0: E0611: No name 'parse' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_from_object_0_test_parse_from_object_basic.py:5:0: E0611: No name 'add_attribute_docstrings' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_parser_parse_from_object_0_test_parse_from_object_basic.py:13:17: E0602: Undefined variable 'parse_from_object' (undefined-variable)


"""