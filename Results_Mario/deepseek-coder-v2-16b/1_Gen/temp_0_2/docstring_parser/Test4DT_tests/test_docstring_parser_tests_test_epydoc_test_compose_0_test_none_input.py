
import pytest
from docstring_parser.tests.test_epydoc import compose, parse

@pytest.fixture(params=[None])
def source(request):
    return request.param

@pytest.fixture(params=["Expected result."])
def expected(request):
    return request.param

def test_compose(source: str, expected: str) -> None:
    """Test compose in default mode."""
    if source is not None:
        assert compose(parse(source)) == expected
