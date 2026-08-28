
import pytest
from docstring_parser.numpydoc import RaisesSection, DocstringRaises

def _clean_str(value: str) -> str:
    """Helper function to clean up strings by stripping whitespace."""
    cleaned = value.strip()
    return None if not cleaned else cleaned

@pytest.fixture
def parser():
    return RaisesSection(title="Raises", key="key")

def test_valid_case(parser):
    raises_item = parser._parse_item('ValueError', 'If the input is out of range')
    assert raises_item.args == ['key', 'ValueError']
    assert raises_item.description == 'If the input is out of range'
    assert raises_item.type_name == 'ValueError'

def test_edge_case_empty_description(parser):
    raises_item = parser._parse_item('TypeError', '   ')
    assert raises_item.args == ['key', 'TypeError']
    assert raises_item.description is None
    assert raises_item.type_name == 'TypeError'

def test_invalid_case_non_string_key(parser):
    with pytest.raises(TypeError):
        parser._parse_item(123, 'If the input is out of range')
