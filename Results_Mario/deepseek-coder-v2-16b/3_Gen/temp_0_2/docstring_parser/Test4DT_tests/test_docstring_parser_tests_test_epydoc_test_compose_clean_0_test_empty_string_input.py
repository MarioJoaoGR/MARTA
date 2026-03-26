
import pytest
from docstring_parser.tests.test_epydoc import parse, compose, RenderingStyle

@pytest.fixture(params=[""])  # Using an empty string as a placeholder fixture for 'source'
def source():
    return ""

@pytest.mark.parametrize("source, expected", [("", "")])  # Parametrizing the test with an empty input and output
def test_compose_clean(source, expected):
    assert compose(parse(source), rendering_style=RenderingStyle.CLEAN) == expected
