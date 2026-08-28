
import pytest
from string_utils.validation import is_snake_case

def test_is_snake_case_default_separator():
    assert is_snake_case('foo_bar_baz') is True
    assert is_snake_case('FooBarBaz') is False
    assert is_snake_case('1foo_bar') is False
    assert is_snake_case('_leading_underscore') is True
    assert is_snake_case('trailing_underscore_') is True