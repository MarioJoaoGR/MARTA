
import pytest
from docstring_parser.google import GoogleParser, Section

# Assuming DEFAULT_SECTIONS contains the expected default sections
DEFAULT_SECTIONS = ["Summary", "Args", "Returns", "Raises"]

def test_GoogleParser_custom_sections():
    """Test initialization of GoogleParser with custom sections."""
    sec1 = Section("CustomSection", "This is a custom section.")
    parser = GoogleParser([sec1], title_colon=True)
    assert isinstance(parser.sections, dict)
    assert parser.title_colon is True
    assert list(parser.sections.keys()) == ["CustomSection"]

def test_GoogleParser_no_sections():
    """Test initialization of GoogleParser with no sections."""
    parser = GoogleParser(sections=None, title_colon=True)
    assert isinstance(parser.sections, dict)
    assert parser.title_colon is True
    assert list(parser.sections.keys()) == DEFAULT_SECTIONS

def test_GoogleParser_default_sections():
    """Test initialization of GoogleParser with default sections."""
    parser = GoogleParser()
    assert isinstance(parser.sections, dict)
    assert parser.title_colon is True
    assert list(parser.sections.keys()) == DEFAULT_SECTIONS

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_multi_meta_0_test_edge_case.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________ test_GoogleParser_custom_sections _______________________

    def test_GoogleParser_custom_sections():
        """Test initialization of GoogleParser with custom sections."""
>       sec1 = Section("CustomSection", "This is a custom section.")
E       TypeError: SectionBase.__new__() missing 1 required positional argument: 'type'

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_multi_meta_0_test_edge_case.py:10: TypeError
________________________ test_GoogleParser_no_sections _________________________

    def test_GoogleParser_no_sections():
        """Test initialization of GoogleParser with no sections."""
        parser = GoogleParser(sections=None, title_colon=True)
        assert isinstance(parser.sections, dict)
        assert parser.title_colon is True
>       assert list(parser.sections.keys()) == DEFAULT_SECTIONS
E       AssertionError: assert ['Arguments',...eptions', ...] == ['Summary', '...ns', 'Raises']
E         
E         At index 0 diff: 'Arguments' != 'Summary'
E         Left contains 8 more items, first extra item: 'Raises'
E         Use -v to get more diff

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_multi_meta_0_test_edge_case.py:21: AssertionError
______________________ test_GoogleParser_default_sections ______________________

    def test_GoogleParser_default_sections():
        """Test initialization of GoogleParser with default sections."""
        parser = GoogleParser()
        assert isinstance(parser.sections, dict)
        assert parser.title_colon is True
>       assert list(parser.sections.keys()) == DEFAULT_SECTIONS
E       AssertionError: assert ['Arguments',...eptions', ...] == ['Summary', '...ns', 'Raises']
E         
E         At index 0 diff: 'Arguments' != 'Summary'
E         Left contains 8 more items, first extra item: 'Raises'
E         Use -v to get more diff

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_multi_meta_0_test_edge_case.py:28: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_multi_meta_0_test_edge_case.py::test_GoogleParser_custom_sections
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_multi_meta_0_test_edge_case.py::test_GoogleParser_no_sections
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_multi_meta_0_test_edge_case.py::test_GoogleParser_default_sections
============================== 3 failed in 0.04s ===============================
"""