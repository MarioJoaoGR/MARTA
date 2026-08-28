# Module: apimd.parser
# test_esc_underscore.py
from apimd.parser import esc_underscore

def test_single_underscore():
    assert esc_underscore("single_name") == "single_name"

def test_multiple_underscores():
    assert esc_underscore("multiple__underscores") == "multiple\\_\\_underscores"

def test_no_underscores():
    assert esc_underscore("nounderscore") == "nounderscore"

def test_empty_string():
    assert esc_underscore("") == ""

def test_string_with_spaces():
    assert esc_underscore("name with spaces") == "name with spaces"
