
import pytest
from docstring_parser.tests.test_google import parse

def test_raises() -> None:
    """Test parsing raises."""
    with pytest.raises(ValueError):
        # Test case where no raises section is present
        docstring = parse("Short description")
        assert len(docstring.raises) == 0
        
        # Test case where a raises section with ValueError is present
        docstring = parse("Short description\nRaises:\n    ValueError: description")
        assert len(docstring.raises) == 1
        assert docstring.raises[0].type_name == "ValueError"
        assert docstring.raises[0].description == "description"

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_raises_8_test_invalid_input_error_handling.py F [100%]

=================================== FAILURES ===================================
_________________________________ test_raises __________________________________

    def test_raises() -> None:
        """Test parsing raises."""
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_raises_8_test_invalid_input_error_handling.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_raises_8_test_invalid_input_error_handling.py::test_raises
============================== 1 failed in 0.04s ===============================
"""