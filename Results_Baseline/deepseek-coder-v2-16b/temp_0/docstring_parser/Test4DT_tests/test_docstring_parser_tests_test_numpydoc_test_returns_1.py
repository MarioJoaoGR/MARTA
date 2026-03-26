
# Module: docstring_parser.tests.test_numpydoc
from docstring_parser import parse
import pytest

def test_empty_docstring():
    """Test case to check when there is no return specified in an empty docstring."""
    docstring = parse("")
    assert docstring.returns is None
    assert docstring.many_returns is not None
    assert len(docstring.many_returns) == 0

def test_no_return_section():
    """Test case to check when there is no 'Returns' or equivalent section in the docstring."""
    docstring = parse("Short description")
    assert docstring.returns is None
    assert docstring.many_returns is not None