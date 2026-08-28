
import pytest
from docstring_parser.parser import parse, Style, Docstring, ParseError

def test_parse_auto_style():
    text = '"""This is a sample docstring."""'
    parsed_doc = parse(text)
    assert isinstance(parsed_doc, Docstring)

def test_parse_google_style():
    text = '''"""Docstring in Google style.

Args:
    param1 (int): Description of param1.
Returns:
    int: Description of return value."""
'''
    parsed_doc = parse(text, style=Style.google)
    assert isinstance(parsed_doc, Docstring)
    assert len(parsed_doc.params) == 1
    assert parsed_doc.params[0].arg_name == 'param1'

def test_parse_rest_style():
    text = '''"""Docstring in reST style.

:param param1: Description of param1.
:type param1: int
:return: Description of return value.
:rtype: int"""
'''
    parsed_doc = parse(text, style=Style.rest)
    assert isinstance(parsed_doc, Docstring)
    assert len(parsed_doc.params) == 1
    assert parsed_doc.params[0].arg_name == 'param1'

def test_parse_numpydoc_style():
    text = '''"""Docstring in NumPy style.

Parameters
----------
param1 : int
    Description of param1.
Returns
-------
int
    Description of return value."""
'''
    parsed_doc = parse(text, style=Style.numpydoc)
    assert isinstance(parsed_doc, Docstring)
    assert len(parsed_doc.params) == 1
    assert parsed_doc.params[0].arg_name == 'param1'
