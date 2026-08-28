# Module: string_utils.validation
import pytest
from string_utils.validation import contains_html, InvalidInputError

def test_contains_html_with_html_tags():
    assert contains_html('my string is <strong>bold</strong>') == True

def test_contains_html_without_html_tags():
    assert contains_html('my string is not bold') == False

def test_contains_html_empty_string():
    assert contains_html('') == False

def test_contains_html_with_xml_tags():
    assert contains_html('<root><child>data</child></root>') == True

def test_contains_html_angle_brackets_no_tags():
    assert contains_html('This is < not a tag >') == False

def test_contains_html_invalid_input_type_int():
    with pytest.raises(InvalidInputError) as excinfo:
        contains_html(123)
    assert str(excinfo.value) == 'Expected "str", received "int"'

def test_contains_html_invalid_input_type_list():
    with pytest.raises(InvalidInputError) as excinfo:
        contains_html(['my string is <strong>bold</strong>'])
    assert str(excinfo.value) == 'Expected "str", received "list"'

def test_contains_html_invalid_input_type_none():
    with pytest.raises(InvalidInputError) as excinfo:
        contains_html(None)
    assert str(excinfo.value) == 'Expected "str", received "NoneType"'
