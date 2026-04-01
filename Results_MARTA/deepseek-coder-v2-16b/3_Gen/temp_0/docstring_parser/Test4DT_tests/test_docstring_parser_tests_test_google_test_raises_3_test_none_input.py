
import pytest
from docstring_parser.tests.test_google import parse

def test_none_input():
    """Test parsing raises in a Google-style docstring with None input."""
    # Test when the docstring is None
    docstring = parse(None)
    assert len(docstring.raises) == 0
