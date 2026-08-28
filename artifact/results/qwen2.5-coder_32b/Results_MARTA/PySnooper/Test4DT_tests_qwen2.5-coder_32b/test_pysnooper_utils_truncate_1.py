
import pytest
from pysnooper.utils import truncate

def test_truncate_long_string():
    result = truncate("Hello, world!", 10)
    assert result == "Hel...rld!"

def test_truncate_short_string():
    result = truncate("Short", 10)
    assert result == "Short"

def test_no_truncation_with_none_max_length():
    result = truncate("Another example", None)
    assert result == "Another example"

def test_boundary_case():
    result = truncate("Boundary!", 9)
    assert result == "Boundary!"


def test_empty_string():
    result = truncate("", 5)
    assert result == ""
