
import pytest
from docstring_parser.tests.test_google import compose, parse

@pytest.fixture
def source_docstring():
    return "A brief description."

@pytest.fixture
def expected_output():
    return "A brief description."

def test_compose(source_docstring, expected_output):
    assert compose(parse(source_docstring)) == expected_output
