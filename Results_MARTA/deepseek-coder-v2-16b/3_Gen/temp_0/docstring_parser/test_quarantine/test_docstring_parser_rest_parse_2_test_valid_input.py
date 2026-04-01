
import pytest
from docstring_parser.rest import parse, Docstring

def test_valid_input():
    rest_docstring = "This is a brief description.\n\nAnd this is more detailed documentation."
    parsed_docstring = parse(rest_docstring)
    
    assert parsed_docstring.short_description == "This is a brief description."
    assert parsed_docstring.long_description == "And this is more detailed documentation."
    assert len(parsed_docstring.meta) == 0, "Expected no metadata in the docstring"

def test_valid_input_with_metadata():
    rest_docstring = """This is a brief description.

:param arg1: Description of arg1
:type arg1: int
:rtype: str
"""
    parsed_docstring = parse(rest_docstring)
    
    assert parsed_docstring.short_description == "This is a brief description."
    assert parsed_docstring.long_description == ""
    assert len(parsed_docstring.meta) == 2, "Expected two metadata items in the docstring"
    assert isinstance(parsed_docstring.meta[0], DocstringParam), "First meta should be a parameter"
    assert parsed_docstring.meta[0].arg_name == "arg1", f"Arg name should be 'arg1', got {parsed_docstring.meta[0].arg_name}"
    assert parsed_docstring.meta[0].type_name == "int", f"Type for arg1 should be 'int', got {parsed_docstring.meta[0].type_name}"
    assert isinstance(parsed_docstring.meta[1], DocstringReturns), "Second meta should be a return type"
    assert parsed_docstring.meta[1].type_name == "str", f"Return type should be 'str', got {parsed_docstring.meta[1].type_name}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_rest_parse_2_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_rest_parse_2_test_valid_input.py:25:48: E0602: Undefined variable 'DocstringParam' (undefined-variable)
docstring_parser/Test4DT_tests/test_docstring_parser_rest_parse_2_test_valid_input.py:28:48: E0602: Undefined variable 'DocstringReturns' (undefined-variable)


"""