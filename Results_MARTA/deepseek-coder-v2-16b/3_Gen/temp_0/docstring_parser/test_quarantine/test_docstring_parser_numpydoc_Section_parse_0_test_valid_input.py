
import pytest
from docstring_parser.numpydoc import Section, DocstringMeta

def test_valid_input():
    section = Section(title="Parameters", key="params")
    
    assert section.title == "Parameters"
    assert section.key == "params"
    
    parsed_meta = list(section.parse("  param1: description of param1\n  param2: description of param2  "))
    
    # Check that the number of parsed metadata objects is correct
    assert len(parsed_meta) == 2
    for meta in parsed_meta:
        assert isinstance(meta, DocstringMeta)

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

    def test_valid_input():
        section = Section(title="Parameters", key="params")
    
        assert section.title == "Parameters"
        assert section.key == "params"
    
        parsed_meta = list(section.parse("  param1: description of param1\n  param2: description of param2  "))
    
        # Check that the number of parsed metadata objects is correct
>       assert len(parsed_meta) == 2
E       assert 1 == 2
E        +  where 1 = len([<docstring_parser.common.DocstringMeta object at 0x105bc49d0>])

docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_Section_parse_0_test_valid_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_Section_parse_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.04s ===============================
"""