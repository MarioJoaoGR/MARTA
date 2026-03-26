
import pytest
from docstring_parser import numdoc

@pytest.fixture
def valid_section():
    return numdoc.Section(title="Parameters", key="params")

def test_valid_input(valid_section):
    assert valid_section.title == "Parameters"
    assert valid_section.key == "params"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_numpydoc_Section_parse_0_test_valid_input
docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_Section_parse_0_test_valid_input.py:3:0: E0611: No name 'numdoc' in module 'docstring_parser' (no-name-in-module)

"""