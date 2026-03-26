
import pytest
from docstring_parser import parse
from docstring_parser.common import ParseError

def test_broken_meta():
    """
    Test parsing broken meta information by passing incorrect or malformed arguments to _build_meta().
    This should raise a ParseError.
    """
    # Empty docstring should raise ParseError
    with pytest.raises(ParseError):
        parse("Args:")
    
    # Incorrectly indented docstring should raise ParseError
    with pytest.raises(ParseError):
        parse("Args:\n    herp derp")

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

docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_broken_meta _______________________________

    def test_broken_meta():
        """
        Test parsing broken meta information by passing incorrect or malformed arguments to _build_meta().
        This should raise a ParseError.
        """
        # Empty docstring should raise ParseError
>       with pytest.raises(ParseError):
E       Failed: DID NOT RAISE <class 'docstring_parser.common.ParseError'>

docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0.py::test_broken_meta
============================== 1 failed in 0.02s ===============================

"""