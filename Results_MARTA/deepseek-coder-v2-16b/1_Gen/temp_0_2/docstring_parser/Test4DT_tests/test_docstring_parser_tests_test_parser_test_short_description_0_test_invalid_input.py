
import pytest
from docstring_parser.tests.test_parser import parse
import typing as T

@pytest.fixture(params=[None, "", "This is a brief description."])
def source() -> T.Generator[T.Optional[str], None, None]:
    yield from (item for item in [None, "", "This is a brief description."])

@pytest.mark.parametrize("source, expected", [(None, None), ("", None), ("This is a brief description.", "This is a brief description.")])
def test_short_description(source: T.Optional[str], expected: T.Optional[str]) -> None:
    """Test parsing short description of a docstring."""
    docstring = parse(source)
    assert docstring.short_description == expected
    assert docstring.description == expected
    assert docstring.long_description is None
    assert not docstring.meta
