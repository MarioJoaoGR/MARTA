# Module: apimd.parser
import pytest
from apimd.parser import esc_underscore

def test_esc_underscore_no_underscores():
    assert esc_underscore("example") == "example"

def test_esc_underscore_single_underscore():
    assert esc_underscore("ex_example") == "ex_example"

def test_esc_underscore_multiple_underscores():
    assert esc_underscore("multi__example") == "multi\\_\\_example"

def test_esc_underscore_empty_string():
    assert esc_underscore("") == ""

def test_esc_underscore_only_underscores():
    assert esc_underscore("__") == "\\_\\_"

def test_esc_underscore_single_character_no_underscore():
    assert esc_underscore("a") == "a"

def test_esc_underscore_single_character_underscore():
    assert esc_underscore("_") == "_"

def test_esc_underscore_multiple_consecutive_underscores_long_string():
    assert esc_underscore("very__long__string__with__multiple__underscores") == "very\\_\\_long\\_\\_string\\_\\_with\\_\\_multiple\\_\\_underscores"
