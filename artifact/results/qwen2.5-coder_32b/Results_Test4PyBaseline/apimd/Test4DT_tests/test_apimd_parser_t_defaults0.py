
import pytest
from apimd.parser import _defaults
from ast import Constant

def test_defaults_with_mixed_values():
    default_values = [
        Constant(value=1),
        None,
        Constant(value="example|text"),
    ]
    expected_output = ['`1`', ' ', "<code>'example&#124;text'</code>"]
    assert list(_defaults(default_values)) == expected_output

def test_defaults_with_empty_sequence():
    empty_defaults = []
    expected_output = []
    assert list(_defaults(empty_defaults)) == expected_output

def test_defaults_with_all_none_values():
    all_none_defaults = [None, None]
    expected_output = [' ', ' ']
    assert list(_defaults(all_none_defaults)) == expected_output

def test_defaults_with_string_only():
    string_defaults = [
        Constant(value="hello"),
        Constant(value="world|with|pipes"),
    ]
    expected_output = ["`'hello'`", "<code>'world&#124;with&#124;pipes'</code>"]
    assert list(_defaults(string_defaults)) == expected_output

def test_defaults_with_numeric_only():
    numeric_defaults = [
        Constant(value=3.14),
        Constant(value=-42),
    ]
    expected_output = ['`3.14`', '`-42`']
    assert list(_defaults(numeric_defaults)) == expected_output

def test_defaults_with_boolean_values():
    boolean_defaults = [
        Constant(value=True),
        Constant(value=False),
    ]
    expected_output = ['`True`', '`False`']
    assert list(_defaults(boolean_defaults)) == expected_output
