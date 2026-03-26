
import pytest
from docstring_parser.google import GoogleParser, Section

def test_valid_input_custom_sections():
    from docstring_parser.google import DEFAULT_SECTIONS
    
    # Arrange
    custom_sections = [Section('Summary', 'summary'), Section('Parameters', 'parameters')]
    parser = GoogleParser(sections=custom_sections, title_colon=True)
    
    # Act and Assert (if necessary for further checks)
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

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_multi_meta_2_test_valid_input_custom_sections.py F [100%]

=================================== FAILURES ===================================
_______________________ test_valid_input_custom_sections _______________________

    def test_valid_input_custom_sections():
        from docstring_parser.google import DEFAULT_SECTIONS
    
        # Arrange
>       custom_sections = [Section('Summary', 'summary'), Section('Parameters', 'parameters')]
E       TypeError: SectionBase.__new__() missing 1 required positional argument: 'type'

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_multi_meta_2_test_valid_input_custom_sections.py:9: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_multi_meta_2_test_valid_input_custom_sections.py::test_valid_input_custom_sections
============================== 1 failed in 0.04s ===============================
"""