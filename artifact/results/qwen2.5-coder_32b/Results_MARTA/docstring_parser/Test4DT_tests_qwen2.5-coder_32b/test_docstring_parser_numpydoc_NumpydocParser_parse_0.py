
import pytest
from docstring_parser.numpydoc import NumpydocParser




def test_parse_empty_string():
    parser = NumpydocParser()
    parsed_doc = parser.parse("")
    assert parsed_doc.short_description is None
    assert parsed_doc.long_description is None
    assert not parsed_doc.meta

def test_parse_no_parameters_section():
    parser = NumpydocParser()
    docstring_text = """
    This function does nothing.

    Returns
    -------
    None
        No return value.
    """
    parsed_doc = parser.parse(docstring_text)
    assert parsed_doc.short_description == "This function does nothing."
    assert len(parsed_doc.meta) == 1

def test_parse_no_return_section():
    parser = NumpydocParser()
    docstring_text = """
    This function prints a message.

    Parameters
    ----------
    message : str
        The message to print.
    """
    parsed_doc = parser.parse(docstring_text)
    assert parsed_doc.short_description == "This function prints a message."
    assert len(parsed_doc.meta) == 1