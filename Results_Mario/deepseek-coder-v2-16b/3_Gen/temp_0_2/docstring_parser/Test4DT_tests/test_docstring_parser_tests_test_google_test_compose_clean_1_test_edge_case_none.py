
import pytest
from docstring_parser.tests.test_google import parse, compose, RenderingStyle

def test_compose_clean():
    source = None
    expected = ''
    assert (
        compose(parse(source), rendering_style=RenderingStyle.CLEAN) == expected
    )
