
import pytest
from docstring_parser.google import GoogleParser, Section

def test_valid_input_custom_sections():
    from docstring_parser.google import DEFAULT_SECTIONS, RETURNS_KEYWORDS, YIELDS_KEYWORDS, RAISES_KEYWORDS, EXAMPLES_KEYWORDS, PARAM_KEYWORDS
    
    custom_sections = [Section('Args', ['arg1', 'arg2'], 'Arguments for the function.')]
    parser = GoogleParser(custom_sections, title_colon=False)
    
    assert isinstance(parser.sections, dict)
    assert len(parser.sections) == 1
    assert list(parser.sections.keys())[0] == 'Args'
    assert parser.title_colon is False
