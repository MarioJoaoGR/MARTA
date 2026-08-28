
import pytest
from docstring_parser.numpydoc import RaisesSection, DocstringRaises

def test_parse_item_valid_exception():
    parser = RaisesSection(title="Raises", key="raises")
    raises_info = parser._parse_item("ValueError", "    If the input is negative    ")
    assert raises_info.type_name == "ValueError"
    assert raises_info.description == "If the input is negative"
    assert raises_info.args == ["raises", "ValueError"]

def test_parse_item_no_whitespace():
    parser = RaisesSection(title="Raises", key="raises")
    raises_info = parser._parse_item("TypeError", "When an incorrect data type is provided")
    assert raises_info.type_name == "TypeError"
    assert raises_info.description == "When an incorrect data type is provided"
    assert raises_info.args == ["raises", "TypeError"]

def test_parse_item_empty_description():
    parser = RaisesSection(title="Raises", key="raises")
    raises_info = parser._parse_item("KeyError", "")
    assert raises_info.type_name == "KeyError"