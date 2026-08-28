
import pytest
from unittest.mock import patch
from docstring_parser.numpydoc import NumpydocParser, Section, DEFAULT_SECTIONS
from docstring_parser.common import Docstring

# Test default initialization with no custom sections

# Test custom sections provided
def test_custom_sections_provided():
    custom_sections = {
        'Parameters': Section('Parameters', r'^\s*Parameters\b'),
        'Returns': Section('Returns', r'^\s*Returns\b')
    }
    with patch.object(NumpydocParser, '_setup'):  # Mock the _setup method to avoid actual setup
        parser = NumpydocParser(sections=custom_sections)
        assert hasattr(parser, 'sections')
        assert isinstance(parser.sections, dict)
        assert len(parser.sections) == 2

# Test parsing an empty docstring

# Test parsing a full docstring with custom sections