
import pytest
from docstring_parser.tests.test_rest import parse
import typing as T

@pytest.mark.parametrize("source, expected", [
    (None, None)
])
def test_short_description(source: T.Optional[str], expected: T.Optional[str]) -> None:
    """Test parsing short description."""
    docstring = parse(source)
    assert docstring.short_description == expected
    assert docstring.description == expected
    assert docstring.long_description is None
    assert not docstring.meta
