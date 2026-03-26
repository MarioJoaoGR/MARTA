
import pytest
from docstring_parser.numpydoc import Section, DocstringMeta

def _clean_str(text):
    return text.strip()

@pytest.fixture
def valid_section():
    return Section(title="Parameters", key="param")

def test_valid_input(valid_section):
    # Test the parse method with a sample input
    parsed_section = valid_section.parse("  param1: description of param1\n  param2: description of param2  ")
    
    # Check that two DocstringMeta objects are returned
    assert len(list(parsed_section)) == 2
    
    # Check the content of the first parsed object
    meta_objects = list(parsed_section)
    assert meta_objects[0].args == ['param']
    assert meta_objects[0].description == 'description of param1'
    
    # Check the content of the second parsed object
    assert meta_objects[1].args == ['param']
    assert meta_objects[1].description == 'description of param2'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_Section_parse_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

valid_section = <docstring_parser.numpydoc.Section object at 0x10279d3f0>

    def test_valid_input(valid_section):
        # Test the parse method with a sample input
        parsed_section = valid_section.parse("  param1: description of param1\n  param2: description of param2  ")
    
        # Check that two DocstringMeta objects are returned
>       assert len(list(parsed_section)) == 2
E       assert 1 == 2
E        +  where 1 = len([<docstring_parser.common.DocstringMeta object at 0x10279d360>])
E        +    where [<docstring_parser.common.DocstringMeta object at 0x10279d360>] = list(<generator object Section.parse at 0x10276d8c0>)

docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_Section_parse_0_test_valid_input.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_Section_parse_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""