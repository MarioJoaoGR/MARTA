
import pytest
from docstring_parser.tests.test_rest import parse

@pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc", [
    ("Invalid docstring", None, None, False, False, "Invalid docstring"),
])
def test_invalid_input(source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc):
    with pytest.raises(Exception):
        parse(source)

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_newlines_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
_ test_invalid_input[Invalid docstring-None-None-False-False-Invalid docstring] _

source = 'Invalid docstring', expected_short_desc = None
expected_long_desc = None, expected_blank_short_desc = False
expected_blank_long_desc = False, expected_full_desc = 'Invalid docstring'

    @pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc", [
        ("Invalid docstring", None, None, False, False, "Invalid docstring"),
    ])
    def test_invalid_input(source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc):
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_newlines_0_test_invalid_input.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_newlines_0_test_invalid_input.py::test_invalid_input[Invalid docstring-None-None-False-False-Invalid docstring]
============================== 1 failed in 0.03s ===============================
"""