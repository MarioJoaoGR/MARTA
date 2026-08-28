
import pytest
from docstring_parser.google import parse, Docstring

def test_parse_empty_string():
    parsed_doc = parse('')
    assert isinstance(parsed_doc, Docstring)
    assert not parsed_doc.short_description
    assert not parsed_doc.long_description
    assert not parsed_doc.meta

def test_parse_simple_docstring():
    text = '''Short description.

    Long description that explains in more detail what the function does.
    
    Args:
        param1 (int): Description of param1.
        param2 (str): Description of param2.
        
    Returns:
        bool: Description of return value.'''
    parsed_doc = parse(text)
    assert parsed_doc.short_description == "Short description."
    assert parsed_doc.long_description == "Long description that explains in more detail what the function does."



def test_parse_only_short_description():
    text = '''Short description.'''
    parsed_doc = parse(text)
    assert parsed_doc.short_description == "Short description."
    assert not parsed_doc.long_description
    assert not parsed_doc.meta

def test_parse_no_long_description():
    text = '''Short description.

    Args:
        param1 (int): Description of param1.
        param2 (str): Description of param2.'''
    parsed_doc = parse(text)
    assert parsed_doc.short_description == "Short description."
    assert not parsed_doc.long_description
    assert len(parsed_doc.meta) == 2  # 2 Args