
import pytest
from typesystem.fields import String
import re
import typing

# Assuming the module has a predefined dictionary called FORMATS for format serialization
FORMATS = {}  # Placeholder for actual implementation of FORMATS

def test_string_init():
    str_field = String(allow_blank=True, trim_whitespace=True)
    assert str_field.allow_blank == True
    assert str_field.trim_whitespace == True
    assert str_field.max_length is None
    assert str_field.min_length is None
    assert str_field.pattern is None
    assert str_field.format is None

def test_string_init_with_max_length():
    str_max_length = String(max_length=10)
    assert str_max_length.allow_blank == False
    assert str_max_length.trim_whitespace == True
    assert str_max_length.max_length == 10
    assert str_max_length.min_length is None
    assert str_max_length.pattern is None
    assert str_max_length.format is None

def test_string_init_with_min_length():
    str_min_length = String(min_length=5)
    assert str_min_length.allow_blank == False
    assert str_min_length.trim_whitespace == True
    assert str_min_length.max_length is None
    assert str_min_length.min_length == 5
    assert str_min_length.pattern is None
    assert str_min_length.format is None

def test_string_init_with_pattern():
    str_pattern = String(pattern=r"^[a-zA-Z0-9]+$")
    assert str_pattern.allow_blank == False
    assert str_pattern.trim_whitespace == True
    assert str_pattern.max_length is None
    assert str_pattern.min_length is None