
import pytest
from docstring_parser import parse

def test_deprecation():
    """Test parsing deprecation notes."""
    source = """
    Some function to demonstrate deprecation.
    
    Deprecated since version 1.0.0: Use another_function instead.
    """
    expected_depr_version = "1.0.0"
    expected_depr_desc = "Use another_function instead."
    
    docstring = parse(source)
    
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_deprecation _______________________________

    def test_deprecation():
        """Test parsing deprecation notes."""
        source = """
        Some function to demonstrate deprecation.
    
        Deprecated since version 1.0.0: Use another_function instead.
        """
        expected_depr_version = "1.0.0"
        expected_depr_desc = "Use another_function instead."
    
        docstring = parse(source)
    
>       assert docstring.deprecation is not None, "Deprecation information should be present"
E       AssertionError: Deprecation information should be present
E       assert None is not None
E        +  where None = <docstring_parser.common.Docstring object at 0x1047b9210>.deprecation

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0.py::test_deprecation
============================== 1 failed in 0.02s ===============================

"""