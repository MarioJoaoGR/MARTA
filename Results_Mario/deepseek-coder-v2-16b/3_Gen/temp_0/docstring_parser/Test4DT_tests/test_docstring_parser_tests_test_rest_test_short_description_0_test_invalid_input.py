
import pytest
from docstring_parser.tests.test_rest import parse  # Assuming this is the correct module path
import typing as T

@pytest.fixture(scope="module")
def source():
    return "This is a brief description."

@pytest.fixture(scope="module")
def expected():
    return "This is a brief description."

def test_short_description(source: T.Optional[str], expected: T.Optional[str]) -> None:
    """Test parsing short description."""
    docstring = parse(source)
    assert docstring.short_description == expected
    assert docstring.description == expected
    assert docstring.long_description is None
    assert not docstring.meta
