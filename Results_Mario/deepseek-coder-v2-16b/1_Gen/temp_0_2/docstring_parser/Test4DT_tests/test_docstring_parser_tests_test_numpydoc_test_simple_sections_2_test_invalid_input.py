
from docstring_parser.tests.test_numpydoc import parse

def test_invalid_input() -> None:
    """Test parsing invalid input."""
    # Test with an empty string, which should not raise any errors and result in no meta objects
    docstring = parse("")
    assert len(docstring.meta) == 0

    # Test with a non-empty string that does not follow the numpy-style docstring format
    docstring = parse("Invalid input")
    assert len(docstring.meta) == 0
