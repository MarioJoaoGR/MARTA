
import pytest
from docstring_parser.google import GoogleParser, Section

# Define the default sections as expected by the GoogleParser initialization
DEFAULT_SECTIONS = [Section('Summary'), Section('Parameters')]

def test_valid_input_default_sections():
    # Test that the GoogleParser can be initialized with the default sections
    parser = GoogleParser(sections=DEFAULT_SECTIONS, title_colon=True)
    
    # Assert that the parser has been correctly initialized and contains the expected sections
    assert isinstance(parser, GoogleParser)
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
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_docstring_parser_google_GoogleParser__build_multi_meta_2_test_valid_input_default_sections.py _
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_multi_meta_2_test_valid_input_default_sections.py:6: in <module>
    DEFAULT_SECTIONS = [Section('Summary'), Section('Parameters')]
E   TypeError: SectionBase.__new__() missing 2 required positional arguments: 'key' and 'type'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_multi_meta_2_test_valid_input_default_sections.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.10s ===============================
"""