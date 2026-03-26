
from docstring_parser.tests.test_numpydoc import parse

def test_invalid_input_none():
    """Test parsing attributes from a numpy-style docstring with invalid input (None)."""
    # Test with None input, which should not raise an error and result in no parameters parsed
    docstring = parse(None)
    assert len(docstring.params) == 0
