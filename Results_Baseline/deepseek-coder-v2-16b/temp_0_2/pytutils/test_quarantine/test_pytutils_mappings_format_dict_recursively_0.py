
# Module: pytutils.mappings
import pytest
from pytutils.mappings import format_dict_recursively

# Example 1: Basic Usage
def test_format_dict_recursively_basic():
    c = dict(wat='wat{omg}', omg=True)
    formatted_dict = format_dict_recursively(c)
    assert formatted_dict == {'omg': True, 'wat': 'watTrue'}

# Example 2: Handling Missing Keys
def test_format_dict_recursively_missing_keys():
    c = dict(wat='wat{omg}', omg=True, fail='no{whale}')
    with pytest.raises(ValueError) as excinfo:
        format_dict_recursively(c)
    assert str(excinfo.value) == "Impossible to format dict due to missing elements: {'fail': ['whale']}"

# Handling Missing Keys without raising error
def test_format_dict_recursively_missing_keys_no_raise():
    c = dict(wat='wat{omg}', omg=True, fail='no{whale}')
    formatted_dict = format_dict_recursively(c, raise_unresolvable=False)
    assert formatted_dict == {'fail': 'no{whale}', 'omg': True, 'wat': 'watTrue'}

# Stripping out unresolvable keys
def test_format_dict_recursively_strip_unresolvable():
    c = dict(wat='wat{omg}', omg=True, fail='no{whale}')
    formatted_dict = format_dict_recursively(c, raise_unresolvable=False, strip_unresolvable=True)
    assert formatted_dict == {'omg': True, 'wat': 'watTrue'}

# Example 3: Using Conversions
def test_format_dict_recursively_conversions():
    c = dict(num='{omg} is {True}')
    formatted_dict = format_dict_recursively(c, conversions={'True': True})
    assert formatted_dict == {'num': 'True is True'}

# Test with a nested dictionary
def test_format_dict_recursively_nested():
    c = dict(outer=dict(inner='{omg} is {True}'))
    formatted_dict = format_dict_recursively(c, conversions={'True': True})
    assert formatted_dict == {'outer': {'inner': 'True is True'}}

# Test with a dictionary containing multiple placeholders and nested structures
def test_format_dict_recursively_complex():
    c = dict(top=dict(middle='{omg} {wat}', omg='{nested}', wat='is {value}'))
    nested_dict = {'nested': 'nested value'}
    formatted_dict = format_dict_recursively(c, conversions={'True': True}, mapping=nested_dict)
    assert formatted_dict == {'top': {'middle': 'True is nested value', 'omg': 'nested value', 'wat': 'is {value}'}}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_mappings_format_dict_recursively_0
pytutils/Test4DT_tests/test_pytutils_mappings_format_dict_recursively_0.py:47:21: E1124: Argument 'mapping' passed by position and keyword in function call (redundant-keyword-arg)


"""