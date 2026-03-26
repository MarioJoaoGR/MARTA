
import pytest
from docstring_parser.tests.test_rest import parse

def test_deprecation() -> None:
    """Test parsing deprecation notes."""
    # Test with a valid deprecation note containing version and description
    docstring = parse(":deprecation: 1.1.0 this function will be removed")
    assert docstring.deprecation is not None
    assert docstring.deprecation.version == "1.1.0"
    assert docstring.deprecation.description == "this function will be removed"

    # Test with a valid deprecation note without version but with description
    docstring = parse(":deprecation: this function will be removed")
    assert docstring.deprecation is not None
    assert docstring.deprecation.version is None
    assert docstring.deprecation.description == "this function will be removed"

    # Test with an invalid deprecation note that does not match the expected format
    with pytest.raises(ValueError):
        parse(":invalid: syntax")

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_deprecation_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_deprecation _______________________________

    def test_deprecation() -> None:
        """Test parsing deprecation notes."""
        # Test with a valid deprecation note containing version and description
        docstring = parse(":deprecation: 1.1.0 this function will be removed")
        assert docstring.deprecation is not None
        assert docstring.deprecation.version == "1.1.0"
        assert docstring.deprecation.description == "this function will be removed"
    
        # Test with a valid deprecation note without version but with description
        docstring = parse(":deprecation: this function will be removed")
        assert docstring.deprecation is not None
        assert docstring.deprecation.version is None
        assert docstring.deprecation.description == "this function will be removed"
    
        # Test with an invalid deprecation note that does not match the expected format
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_deprecation_2_test_invalid_input.py:20: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_deprecation_2_test_invalid_input.py::test_deprecation
============================== 1 failed in 0.03s ===============================
"""