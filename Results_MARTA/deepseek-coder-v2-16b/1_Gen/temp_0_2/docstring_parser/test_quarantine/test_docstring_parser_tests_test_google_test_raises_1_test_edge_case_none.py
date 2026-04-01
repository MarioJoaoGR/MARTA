
import pytest
from docstring_parser.tests.test_google import parse

def test_raises() -> None:
    """Test parsing raises."""
    with pytest.raises(Exception):
        parse("Short description")

    parsed_docstring = parse("Short description\nRaises:\n    ValueError: description")
    assert len(parsed_docstring.raises) == 1
    assert parsed_docstring.raises[0].type_name == "ValueError"
    assert parsed_docstring.raises[0].description == "description"

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_raises_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_________________________________ test_raises __________________________________

    def test_raises() -> None:
        """Test parsing raises."""
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_raises_1_test_edge_case_none.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_raises_1_test_edge_case_none.py::test_raises
============================== 1 failed in 0.03s ===============================
"""