
import pytest
from docstring_parser.tests.test_google import parse, test_short_description

def test_none_input():
    with pytest.raises(AssertionError):
        test_short_description(None, None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 7 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_1_test_none_input.py . [ 14%]
.....F                                                                   [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
>       with pytest.raises(AssertionError):
E       Failed: DID NOT RAISE <class 'AssertionError'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_1_test_none_input.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_short_description_1_test_none_input.py::test_none_input
========================= 1 failed, 6 passed in 0.03s ==========================

"""