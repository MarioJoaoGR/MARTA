
import pytest
from string_utils.validation import contains_html, InvalidInputError

def test_valid_string_with_html_tags():
    assert contains_html('my string is <strong>bold</strong>') == True

def test_valid_string_without_html_tags():
    assert contains_html('my string is not bold') == False

def test_empty_string():
    assert contains_html('') == False

def test_valid_string_with_xml_tags():
    assert contains_html('<note><to>Tove</to><from>Jani</from></note>') == True

def test_invalid_input_none():
    with pytest.raises(InvalidInputError):
        contains_html(None)

def test_invalid_input_empty_list():
    with pytest.raises(InvalidInputError):
        contains_html([])

def test_invalid_input_integer():
    with pytest.raises(InvalidInputError):
        contains_html(12345)
