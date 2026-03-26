# Module: docstring_parser.tests.test_epydoc
import pytest
import typing as T
from docstring_parser import parse

# Test cases for short description parsing
@pytest.mark.parametrize(
    "source, expected",
    [
        (None, None),
        ("Short description here", "Short description here"),
        ("Another short description", "Another short description"),
        ("", None),
        # Add more test cases as needed to cover different scenarios and edge cases
    ],
)
def test_short_description(source: T.Optional[str], expected: T.Optional[str]) -> None:
    """Test parsing short description."""
    docstring = parse(source)
    assert docstring.short_description == expected
    assert docstring.long_description is None
    assert not docstring.meta
