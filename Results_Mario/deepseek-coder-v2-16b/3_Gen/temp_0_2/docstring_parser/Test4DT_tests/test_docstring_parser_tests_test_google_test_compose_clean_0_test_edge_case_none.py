
from docstring_parser.tests.test_google import compose, parse, RenderingStyle
import pytest

def test_compose_clean():
    with pytest.raises(AssertionError):
        source = "Some Google-style docstring"
        expected = "Different string that should not match the composed output"
        assert compose(parse(source), rendering_style=RenderingStyle.CLEAN) == expected
