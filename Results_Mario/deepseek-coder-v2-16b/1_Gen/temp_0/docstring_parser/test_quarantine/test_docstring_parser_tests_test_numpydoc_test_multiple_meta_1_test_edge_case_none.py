
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_multiple_meta() -> None:
    """Test parsing multiple meta."""
    with pytest.raises(Exception):
        # This should raise an exception because the current implementation does not handle multi-line descriptions correctly in parameters and raises sections.
        docstring = parse(
            """
            Short description

            Parameters
            ----------
            spam
                asd
                1
                    2
                3

            Raises
            ------
            bla
                herp
            yay
                derp
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_multiple_meta_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
______________________________ test_multiple_meta ______________________________

    def test_multiple_meta() -> None:
        """Test parsing multiple meta."""
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_multiple_meta_1_test_edge_case_none.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_multiple_meta_1_test_edge_case_none.py::test_multiple_meta
============================== 1 failed in 0.03s ===============================

"""