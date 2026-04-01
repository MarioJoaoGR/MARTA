
import pytest
from docstring_parser.tests.test_google import compose, parse

@pytest.fixture(scope="module")
def source():
    return "A brief description."

@pytest.fixture(scope="module")
def expected():
    return "A brief description."

def test_compose(source, expected):
    assert compose(parse(source)) == expected
