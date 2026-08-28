
import pytest
from semantic_release.helpers import format_arg

def test_format_string():
    assert format_arg("Hello, World!") == "'Hello, World!'"

def test_format_non_string():
    assert format_arg(42) == '42'
