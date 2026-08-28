
import pytest
from docstring_parser.google import GoogleParser, Section, Docstring







def test_short_description_only():
    parser = GoogleParser()
    text = 'Short description.'
    docstring = parser.parse(text)
    assert docstring.short_description == 'Short description.'
    assert docstring.long_description is None

def test_long_description_with_blank_line():
    parser = GoogleParser()
    text = (
        'Short description.\n'
        '\n'
        'Long description that explains in more detail what the function does.'
    )
    docstring = parser.parse(text)
    assert docstring.short_description == 'Short description.'
    assert docstring.long_description == 'Long description that explains in more detail what the function does.'






def test_no_sections():
    parser = GoogleParser()
    text = (
        'Short description.\n'
        '\n'
        'Long description.'
    )
    docstring = parser.parse(text)
    assert len(docstring.meta) == 0
    assert docstring.short_description == 'Short description.'
    assert docstring.long_description == 'Long description.'

def test_empty_docstring():
    parser = GoogleParser()
    text = ''
    docstring = parser.parse(text)
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert len(docstring.meta) == 0

def test_whitespace_only_docstring():
    parser = GoogleParser()
    text = '   \n\n'
    docstring = parser.parse(text)
    assert docstring.short_description is None
    assert docstring.long_description is None
    assert len(docstring.meta) == 0