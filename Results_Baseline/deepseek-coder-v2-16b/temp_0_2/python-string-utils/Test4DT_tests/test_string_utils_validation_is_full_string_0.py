# Module: string_utils.validation
# test_string_utils.py
from string_utils.validation import is_full_string
import pytest
from typing import Any

def test_is_full_string_with_none():
    result = is_full_string(None)
    assert not result, "Expected False when input is None"

def test_is_full_string_with_empty_string():
    result = is_full_string('')
    assert not result, "Expected False when input is an empty string"

def test_is_full_string_with_whitespace_string():
    result = is_full_string(' ')
    assert not result, "Expected False when input consists only of spaces"

def test_is_full_string_with_non_empty_string():
    result = is_full_string('hello')
    assert result, "Expected True when input is a non-empty string"
