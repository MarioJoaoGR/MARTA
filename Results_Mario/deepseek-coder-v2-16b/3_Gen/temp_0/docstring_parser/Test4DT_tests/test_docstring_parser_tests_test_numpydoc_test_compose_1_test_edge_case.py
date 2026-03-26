
import pytest
from docstring_parser.tests.test_numpydoc import parse, compose

@pytest.fixture
def source():
    return "A brief description of what this function does."

@pytest.fixture
def expected():
    return "A brief description of what this function does."

def test_compose(source, expected):
    """Test compose in default mode."""
    assert compose(parse(source)) == expected
