
import pytest
from docstring_parser.numpydoc import NumpydocParser, DEFAULT_SECTIONS, Section

def test_none_input():
    parser = NumpydocParser(sections=None)
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

docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser_add_section_0_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        parser = NumpydocParser(sections=None)
>       assert parser.sections == DEFAULT_SECTIONS
E       AssertionError: assert {'Args': <doc...2b56da0>, ...} == [<docstring_p...2b56bc0>, ...]
E         
E         Use -v to get more diff

docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser_add_section_0_test_none_input.py:7: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_numpydoc_NumpydocParser_add_section_0_test_none_input.py::test_none_input
============================== 1 failed in 0.08s ===============================
"""