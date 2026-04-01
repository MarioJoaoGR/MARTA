
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_warns() -> None:
    """Test parsing warns."""
    with pytest.raises(Exception):
        docstring = parse(
            """
            Short description
            Warns
            -----
            UserWarning
                description
            """
        )

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_warns_5_test_none_input.py F [100%]

=================================== FAILURES ===================================
__________________________________ test_warns __________________________________

    def test_warns() -> None:
        """Test parsing warns."""
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_warns_5_test_none_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_warns_5_test_none_input.py::test_warns
============================== 1 failed in 0.04s ===============================
"""