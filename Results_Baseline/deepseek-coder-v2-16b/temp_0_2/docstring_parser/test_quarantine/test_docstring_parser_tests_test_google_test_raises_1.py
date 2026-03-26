
# Module: docstring_parser.tests.test_google
from docstring_parser import parse  # Corrected import statement
import pytest

def test_raises():
    """Test parsing raises."""
    # Test case 1: No Raises section in the docstring
    with pytest.raises(ValueError) as exc_info:
        parse("""Short description""")
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_raises_1.py F [100%]

=================================== FAILURES ===================================
_________________________________ test_raises __________________________________

    def test_raises():
        """Test parsing raises."""
        # Test case 1: No Raises section in the docstring
>       with pytest.raises(ValueError) as exc_info:
E       Failed: DID NOT RAISE <class 'ValueError'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_raises_1.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_raises_1.py::test_raises
============================== 1 failed in 0.02s ===============================

"""