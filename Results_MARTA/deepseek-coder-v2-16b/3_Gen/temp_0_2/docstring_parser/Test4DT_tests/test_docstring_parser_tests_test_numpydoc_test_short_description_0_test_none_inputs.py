
import pytest
from docstring_parser.tests.test_numpydoc import parse  # Assuming this is the correct module path
import typing as T

@pytest.fixture(params=[None, "A function that does something useful."])
def source_expected_pairs(request):
    return request.param, request.param

def test_short_description(source_expected_pairs: tuple[T.Optional[str], T.Optional[str]]) -> None:
    source, expected = source_expected_pairs
    docstring = parse(source)
    assert docstring.short_description == expected
    assert docstring.long_description is None
    assert not docstring.meta
