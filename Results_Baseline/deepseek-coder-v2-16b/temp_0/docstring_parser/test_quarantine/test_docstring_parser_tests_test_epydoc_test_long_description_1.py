
import pytest
from docstring_parser import parse

# Test case for a typical long description with multiple lines
def test_long_description_typical():
    source = "Function with a longer description.\nThis is the short description.\n\nHere is the long description that spans multiple lines."
    parsed_docstring = parse(source)
    
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_long_description_1.py F [100%]

=================================== FAILURES ===================================
________________________ test_long_description_typical _________________________

    def test_long_description_typical():
        source = "Function with a longer description.\nThis is the short description.\n\nHere is the long description that spans multiple lines."
        parsed_docstring = parse(source)
    
>       assert parsed_docstring.short_description == "This is the short description.", f"Expected short description to be 'This is the short description.', but got {parsed_docstring.short_description}"
E       AssertionError: Expected short description to be 'This is the short description.', but got Function with a longer description.
E       assert 'Function wit... description.' == 'This is the ... description.'
E         
E         - This is the short description.
E         + Function with a longer description.

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_long_description_1.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_long_description_1.py::test_long_description_typical
============================== 1 failed in 0.02s ===============================

"""