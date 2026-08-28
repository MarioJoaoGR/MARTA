
import pytest
from semantic_release.helpers import format_arg

def test_format_arg_string():
    assert format_arg("Hello, World!") == "'Hello, World!'"

def test_format_arg_number():
    assert format_arg(42) == "42"

def test_format_arg_boolean():
    assert format_arg(True) == "True"

def test_format_arg_none():
    assert format_arg(None) == "None"
