
from docstring_parser.tests.test_google import parse
import pytest

@pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank", [
    (
        "Invalid string",
        "Expected short desc",
        "",
        True
    )
])
def test_invalid_input(source, expected_short_desc, expected_long_desc, expected_blank):
    with pytest.raises(Exception):
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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_long_description_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
_________ test_invalid_input[Invalid string-Expected short desc--True] _________

source = 'Invalid string', expected_short_desc = 'Expected short desc'
expected_long_desc = '', expected_blank = True

    @pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank", [
        (
            "Invalid string",
            "Expected short desc",
            "",
            True
        )
    ])
    def test_invalid_input(source, expected_short_desc, expected_long_desc, expected_blank):
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_long_description_0_test_invalid_input.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_long_description_0_test_invalid_input.py::test_invalid_input[Invalid string-Expected short desc--True]
============================== 1 failed in 0.03s ===============================
"""