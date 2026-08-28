
import pytest
from string_utils.validation import is_snake_case

def test_is_snake_case_default_separator():
    assert is_snake_case('foo_bar_baz') is True
    assert is_snake_case('FooBarBaz') is False
    assert is_snake_case('1foo_bar') is False
    assert is_snake_case('_leading_underscore') is True
    assert is_snake_case('trailing_underscore_') is True

def test_is_snake_case_non_string_inputs():
    # Test with None
    assert is_snake_case(None) is False
    # Test with an integer
    assert is_snake_case(12345) is False
    # Test with a float
    assert is_snake_case(123.45) is False
    # Test with a list
    assert is_snake_case(['foo', 'bar']) is False
    # Test with a dictionary
    assert is_snake_case({'key': 'value'}) is False
    # Test with a tuple
    assert is_snake_case(('foo', 'bar')) is False
    # Test with a set
    assert is_snake_case({'foo', 'bar'}) is False

def test_is_snake_case_empty_string():
    assert is_snake_case('') is False

def test_is_snake_case_whitespace_only():
    assert is_snake_case(' ') is False
    assert is_snake_case('   ') is False

def test_is_snake_case_special_characters():
    assert is_snake_case('foo@bar#baz') is False
    assert is_snake_case('foo-bar-baz') is False  # Different separator, should be False without specifying separator
    assert is_snake_case('foo.bar.baz') is False

def test_is_snake_case_custom_separator():
    assert is_snake_case('foo-bar-baz', '-') is True
    assert is_snake_case('foo_bar_baz', '-') is False
    assert is_snake_case('foo.bar.baz', '.') is True
    assert is_snake_case('foo_bar_baz', '.') is False

def test_is_snake_case_no_separator():
    assert is_snake_case('foobarbaz') is False
