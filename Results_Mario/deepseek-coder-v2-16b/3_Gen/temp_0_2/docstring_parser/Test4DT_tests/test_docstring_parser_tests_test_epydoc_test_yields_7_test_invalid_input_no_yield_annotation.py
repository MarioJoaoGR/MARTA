
import pytest
from docstring_parser.tests.test_epydoc import parse

def test_invalid_input_no_yield_annotation():
    """Test handling a docstring without any yield annotation."""
    docstring = parse(
        """
        Short description
        """
    )
    assert docstring.returns is None
