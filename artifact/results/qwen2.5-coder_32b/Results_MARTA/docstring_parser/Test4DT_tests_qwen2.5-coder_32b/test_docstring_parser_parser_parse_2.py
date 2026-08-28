
import pytest
from docstring_parser.parser import parse, Style, Docstring

def test_parse_auto_style():
    docstring = """Docstring here."""
    parsed_doc = parse(docstring)
    assert isinstance(parsed_doc, Docstring)


def test_parse_google_style():
    docstring = """Docstring in Google style.

    Args:
        param1 (int): Description of param1.
    
    Returns:
        int: Description of return value."""
    parsed_doc = parse(docstring, style=Style.google)
    assert parsed_doc.params[0].arg_name == 'param1'
    assert parsed_doc.returns.type_name == 'int'

def test_parse_numpydoc_style():
    docstring = """Docstring in NumPy style.

    Parameters
    ----------
    param1 : int
        Description of param1.
    
    Returns
    -------
    int
        Description of return value."""
    parsed_doc = parse(docstring, style=Style.numpydoc)
    assert parsed_doc.params[0].arg_name == 'param1'
    assert parsed_doc.returns.type_name == 'int'

def test_error_handling_invalid_style():
    docstring = """Docstring here."""
    with pytest.raises(KeyError):
        parse(docstring, style='invalid')