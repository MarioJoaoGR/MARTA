
from docstring_parser import parse, compose
import pytest

def test_short_rtype():
    """Test abbreviated docstring with only return type information."""
    string = "Short description.\n\n@rtype: float"
    parsed_docstring = parse(string)
    assert compose(parsed_docstring).strip() == string.replace("@rtype:", "").strip()

def test_short_rtype_no_description():
    """Test case with no description but only return type information."""
    string = "@rtype: float"
    parsed_docstring = parse(string)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_short_rtype_1.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_short_rtype _______________________________

    def test_short_rtype():
        """Test abbreviated docstring with only return type information."""
        string = "Short description.\n\n@rtype: float"
        parsed_docstring = parse(string)
>       assert compose(parsed_docstring).strip() == string.replace("@rtype:", "").strip()
E       AssertionError: assert 'Short descri...@rtype: float' == 'Short description.\n\n float'
E         
E           Short description.
E           
E         -  float
E         + @rtype: float

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_short_rtype_1.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_short_rtype_1.py::test_short_rtype
========================= 1 failed, 1 passed in 0.02s ==========================

"""