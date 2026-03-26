
from docstring_parser.google import GoogleParser, Section
import pytest

def test_valid_input_custom_sections():
    custom_sections = [Section('Summary'), Section('Parameters')]
    parser = GoogleParser(custom_sections, title_colon=False)
    
    assert isinstance(parser, GoogleParser)
    assert not parser.title_colon
    assert len(parser.sections) == 2
    assert 'Summary' in parser.sections
    assert 'Parameters' in parser.sections

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

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_single_meta_2_test_valid_input_custom_sections.py F [100%]

=================================== FAILURES ===================================
_______________________ test_valid_input_custom_sections _______________________

    def test_valid_input_custom_sections():
>       custom_sections = [Section('Summary'), Section('Parameters')]
E       TypeError: SectionBase.__new__() missing 2 required positional arguments: 'key' and 'type'

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_single_meta_2_test_valid_input_custom_sections.py:6: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_single_meta_2_test_valid_input_custom_sections.py::test_valid_input_custom_sections
============================== 1 failed in 0.04s ===============================
"""