
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
        # Additional test cases to cover uncovered lines 25-28
        ("Short description\n\nLong description", "Short description"),
        ("Short description\n:param param1: Description of param1\n:return: Return value", "Short description"),
        ("Short description with meta info\n:meta keyword: meta value", "Short description with meta info"),
    ],
)
def test_short_description(source: T.Optional[str], expected: T.Optional[str]) -> None:
    """Test parsing short description."""
    docstring = parse(source)
    assert docstring.short_description == expected
    if expected is not None:
        assert docstring.long_description is None or isinstance(docstring.long_description, str)
    else:
        assert docstring.long_description is None