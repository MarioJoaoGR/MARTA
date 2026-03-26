
import pytest
from docstring_parser.google import GoogleParser, Section, DEFAULT_SECTIONS

def test_edge_case_none():
    parser = GoogleParser(sections=None)
    assert parser.sections == DEFAULT_SECTIONS

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

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser_add_section_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        parser = GoogleParser(sections=None)
>       assert parser.sections == DEFAULT_SECTIONS
E       AssertionError: assert {'Args': Sect...LAR: 0>), ...} == [Section(titl...PLE: 1>), ...]
E         
E         Use -v to get more diff

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser_add_section_1_test_edge_case_none.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser_add_section_1_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.03s ===============================
"""