
import pytest
from docstring_parser import parse

def test_meta_newlines():
    with pytest.raises(Exception):
        parsed = parse("""Example docstring
                        with multiple lines
                        and no meta information.""")

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_meta_newlines_1.py F [100%]

=================================== FAILURES ===================================
______________________________ test_meta_newlines ______________________________

    def test_meta_newlines():
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_meta_newlines_1.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_meta_newlines_1.py::test_meta_newlines
============================== 1 failed in 0.02s ===============================

"""