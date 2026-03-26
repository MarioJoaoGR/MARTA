
# Module: docstring_parser.tests.test_parse_from_object
# test_parse_from_object.py
import pytest
from docstring_parser import parse_from_object

def a_function(param1: str, param2: int = 2):
    """Short description
    Args:
        param1: Description for param1
        param2: Description for param2
    """
    return f"{param1} {param2}"

# Test case to cover the function definition line (92)
def test_function_definition():
    assert callable(a_function)

# Test case to cover the parsing call (100)
def test_parse_from_object():
    docstring = parse_from_object(a_function)
    assert docstring.short_description == "Short description"
    assert docstring.description == "Short description"
    assert len(docstring.params) == 2
    assert docstring.params[0].arg_name == "param1"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "Description for param1"
    assert docstring.params[1].arg_name == "param2"
    assert docstring.params[1].type_name is None
    assert docstring.params[1].description == "Description for param2"

# Test case to cover the assertion for short description (102)
def test_short_description():
    docstring = parse_from_object(a_function)
    assert docstring.short_description == "Short description"

# Test case to cover the assertion for long description (103)
def test_long_description():
    docstring = parse_from_object(a_function)
    assert docstring.description == "Short description"

# Test case to cover the assertion for number of parameters (104)
def test_number_of_params():
    docstring = parse_from_object(a_function)
    assert len(docstring.params) == 2

# Test case to cover the first parameter's name and description (105-107)
def test_first_param():
    docstring = parse_from_object(a_function)
    assert docstring.params[0].arg_name == "param1"
    assert docstring.params[0].type_name is None
    assert docstring.params[0].description == "Description for param1"

# Test case to cover the second parameter's name and description (108-110)
def test_second_param():
    docstring = parse_from_object(a_function)
    assert docstring.params[1].arg_name == "param2"
    assert docstring.params[1].type_name is None
    assert docstring.params[1].description == "Description for param2"
