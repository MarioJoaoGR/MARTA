
import pytest
from docstring_parser.numpydoc import NumpydocParser, Section, DEFAULT_SECTIONS

def test_none_input():
    parser = NumpydocParser()
    assert parser is not None
    assert len(parser.sections) == len(DEFAULT_SECTIONS)
