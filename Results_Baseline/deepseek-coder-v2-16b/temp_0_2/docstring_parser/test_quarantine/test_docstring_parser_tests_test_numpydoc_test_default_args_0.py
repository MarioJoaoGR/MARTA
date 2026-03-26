
from docstring_parser import parse
import pytest

# Test Case 1
def example_function(arg1: int = None): pass

@pytest.mark.parametrize("expected_is_optional, expected_type_name, expected_default", [
    (False, "int", "None")
])
def test_example_function(expected_is_optional, expected_type_name, expected_default):
    docstring = parse(example_function.__doc__).params[0]
    assert docstring.is_optional == expected_is_optional
    assert docstring.type_name == expected_type_name
    assert str(docstring.default) == expected_default

# Test Case 2
def another_function(arg2: str): pass

@pytest.mark.parametrize("expected_is_optional, expected_type_name, expected_default", [
    (False, "str", None)
])
def test_another_function(expected_is_optional, expected_type_name, expected_default):
    docstring = parse(another_function.__doc__).params[0]
    assert docstring.is_optional == expected_is_optional
    assert docstring.type_name == expected_type_name
    assert docstring.default is None

# Test Case 3
def third_function(arg3: float = 1.5): pass

@pytest.mark.parametrize("expected_is_optional, expected_type_name, expected_default", [
    (False, "float", "1.5")
])
def test_third_function(expected_is_optional, expected_type_name, expected_default):
    docstring = parse(third_function.__doc__).params[0]
    assert docstring.is_optional == expected_is_optional
    assert docstring.type_name == expected_type_name
    assert str(docstring.default) == expected_default

# Test Case 4
def fourth_function(arg4: str = 'hello'): pass

@pytest.mark.parametrize("expected_is_optional, expected_type_name, expected_default", [
    (True, "str", "'hello'")
])
def test_fourth_function(expected_is_optional, expected_type_name, expected_default):
    docstring = parse(fourth_function.__doc__).params[0]
    assert docstring.is_optional == expected_is_optional
    assert docstring.type_name == expected_type_name
    assert str(docstring.default) == expected_default

# Test Case 5
def multi_param_func(arg1: int, arg2: str = 'default', arg3: float): pass

@pytest.mark.parametrize("expected_is_optional, expected_type_name, expected_default", [
    (True, "str", "'default'")
])
def test_multi_param_func(expected_is_optional, expected_type_name, expected_default):
    docstring = parse(multi_param_func.__doc__).params[1]
    assert docstring.is_optional == expected_is_optional
    assert docstring.type_name == expected_type_name
    assert str(docstring.default) == expected_default

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_default_args_0
docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_default_args_0.py:54:56: E0001: Parsing failed: 'non-default argument follows default argument (Test4DT_tests.test_docstring_parser_tests_test_numpydoc_test_default_args_0, line 54)' (syntax-error)

"""