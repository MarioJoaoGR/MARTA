
import pytest
from docstring_parser.google import parse
from docstring_parser.structures import Docstring

def test_valid_input():
    text = '''
    def example():
        \"\"\"
        This is a summary.
        
        Args:
            arg1 (int): The first argument.
            arg2 (str): The second argument.
            
        Returns:
            int: The result of the function.
        \"\"\"
    '''
    parsed_docstring = parse(text)
    
    assert isinstance(parsed_docstring, Docstring)
    assert parsed_docstring.short_description == "This is a summary."
    assert len(parsed_docstring.params) == 2
    assert parsed_docstring.params[0].arg_name == "arg1"
    assert parsed_docstring.params[0].type_name == "int"
    assert parsed_docstring.params[0].description == "The first argument."
    assert parsed_docstring.params[1].arg_name == "arg2"
    assert parsed_docstring.params[1].type_name == "str"
    assert parsed_docstring.params[1].description == "The second argument."
    assert len(parsed_docstring.returns) == 1
    assert parsed_docstring.returns[0].type_name == "int"
    assert parsed_docstring.returns[0].description == "The result of the function."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_google_parse_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_google_parse_0_test_valid_input.py:4:0: E0401: Unable to import 'docstring_parser.structures' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_google_parse_0_test_valid_input.py:4:0: E0611: No name 'structures' in module 'docstring_parser' (no-name-in-module)


"""