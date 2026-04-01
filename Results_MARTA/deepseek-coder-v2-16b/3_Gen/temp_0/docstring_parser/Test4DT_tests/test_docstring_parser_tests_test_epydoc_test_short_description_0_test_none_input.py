
import pytest
from docstring_parser.tests.test_epydoc import parse  # Assuming this is the correct module path
import typing as T

@pytest.fixture(params=[None])
def source(request):
    return request.param

@pytest.fixture(params=[None])
def expected(request):
    return request.param

def test_short_description(source: T.Optional[str], expected: T.Optional[str]) -> None:
    """Test parsing short description."""
    docstring = parse(source)
    assert docstring.short_description == expected
    assert docstring.long_description is None
    assert not docstring.meta
