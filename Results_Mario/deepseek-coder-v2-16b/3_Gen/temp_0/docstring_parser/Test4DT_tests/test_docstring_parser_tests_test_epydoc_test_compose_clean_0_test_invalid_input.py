
import pytest
from docstring_parser.tests.test_epydoc import parse, compose, RenderingStyle

def test_invalid_input():
    with pytest.raises(Exception):
        source = "Invalid characters: @£$%^&*()"
        expected = "Expected result"
        assert compose(parse(source), rendering_style=RenderingStyle.CLEAN) == expected
