
import pytest
from docstring_parser.tests.test_rest import parse

def test_edge_case_none():
    source = None
    expected_short_desc = None
    expected_long_desc = None
    expected_blank_short_desc = False
    expected_blank_long_desc = False
    expected_full_desc = None

    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc
    assert docstring.blank_after_short_description == expected_blank_short_desc
    assert docstring.blank_after_long_description == expected_blank_long_desc
    assert docstring.description == expected_full_desc
    assert len(docstring.meta) == 0
