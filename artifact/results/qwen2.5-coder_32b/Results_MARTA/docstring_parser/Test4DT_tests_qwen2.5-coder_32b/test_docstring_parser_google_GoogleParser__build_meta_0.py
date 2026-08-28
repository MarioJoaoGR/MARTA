
import pytest
from docstring_parser.google import GoogleParser, DocstringMeta, SectionType

# Assuming DEFAULT_SECTIONS and other necessary imports are defined in the module
# For the sake of this example, let's assume DEFAULT_SECTIONS is defined as follows:
DEFAULT_SECTIONS = [
    # Example sections, adjust according to actual implementation
    {"title": "Returns", "key": "returns", "type": SectionType.SINGULAR},
    {"title": "Parameters", "key": "params", "type": SectionType.SINGULAR_OR_MULTIPLE},
    {"title": "Raises", "key": "raises", "type": SectionType.SINGULAR_OR_MULTIPLE}
]

@pytest.fixture
def parser():
    return GoogleParser()

def test_happy_path_single_return(parser):
    text = 'The sum of two numbers'
    title = 'Returns'
    meta = parser._build_meta(text, title)
    assert meta.description == 'The sum of two numbers'

def test_edge_case_empty_text(parser):
    text = ''
    title = 'Returns'
    meta = parser._build_meta(text, title)
    assert meta.description == ''

def test_invalid_section_title(parser):
    text = 'The sum of two numbers'
    title = 'InvalidSection'
    with pytest.raises(KeyError):
        parser._build_meta(text, title)
