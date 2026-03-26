
import pytest
from docstring_parser.tests.test_epydoc import parse, compose, RenderingStyle

def test_compose_expanded():
    source = ''
    expected = ''
    assert compose(parse(source), rendering_style=RenderingStyle.EXPANDED) == expected
