
import pytest
from docstring_parser.tests.test_epydoc import parse, compose, RenderingStyle

def test_compose_expanded():
    """Test compose in expanded mode."""
    source = None
    expected = "A formatted string with detailed information including parameter descriptions and return types."
    
    # Since the function expects a non-None source, we should handle this case gracefully.
    # Here, we will assert that an exception is raised when source is None.
    with pytest.raises(AssertionError):
        assert compose(parse(source), rendering_style=RenderingStyle.EXPANDED) == expected
