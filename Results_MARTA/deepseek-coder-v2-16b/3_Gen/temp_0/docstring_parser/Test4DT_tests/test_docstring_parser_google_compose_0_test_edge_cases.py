
import pytest
from docstring_parser.google import compose, Docstring, RenderingStyle

@pytest.mark.parametrize("rendering_style", [RenderingStyle.COMPACT, RenderingStyle.EXPANDED])
def test_compose(rendering_style):
    parsed_docstring = Docstring()  # Assuming you have a way to create or obtain a Docstring object
    result = compose(parsed_docstring, rendering_style=rendering_style)
    
    assert isinstance(result, str), "The output should be a string"
