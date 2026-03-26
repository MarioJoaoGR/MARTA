
import pytest
from docstring_parser.tests.test_google import parse

def test_unknown_meta() -> None:
    """Test parsing unknown meta."""
    with pytest.raises(ValueError):
        # This should raise a ValueError due to the presence of unknown metadata sections
        parse("""Short desc

        Unknown 0:
            title0: content0

        Args:
            arg0: desc0
            arg1: desc1

        Unknown1:
            title1: content1

        Unknown2:
            title2: content2""")

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_unknown_meta_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
______________________________ test_unknown_meta _______________________________

    def test_unknown_meta() -> None:
        """Test parsing unknown meta."""
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_unknown_meta_1_test_edge_case_none.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_unknown_meta_1_test_edge_case_none.py::test_unknown_meta
============================== 1 failed in 0.03s ===============================
"""