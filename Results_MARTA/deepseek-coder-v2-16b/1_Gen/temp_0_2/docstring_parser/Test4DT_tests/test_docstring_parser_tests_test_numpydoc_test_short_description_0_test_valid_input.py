
from docstring_parser.tests.test_numpydoc import parse  # Assuming this is the correct import path
import typing as T

def test_short_description(source: T.Optional[str] = None, expected: T.Optional[str] = None) -> None:
    """Test parsing short description."""
    docstring = parse(source)
    assert docstring.short_description == expected
    assert docstring.long_description is None
    assert not docstring.meta
