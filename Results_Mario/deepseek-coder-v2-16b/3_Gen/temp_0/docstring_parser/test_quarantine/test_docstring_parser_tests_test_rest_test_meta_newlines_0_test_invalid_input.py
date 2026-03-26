
import pytest
from docstring_parser.tests.test_rest import parse

@pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc", [
    ("Invalid docstring", None, "Invalid docstring", True, True, "Invalid docstring")
])
def test_invalid_input(source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc):
    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc
    assert docstring.blank_after_short_description == expected_blank_short_desc
    assert docstring.blank_after_long_description == expected_blank_long_desc
    assert docstring.description == expected_full_desc

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
_ test_invalid_input[Invalid docstring-None-Invalid docstring-True-True-Invalid docstring] _

source = 'Invalid docstring', expected_short_desc = None
expected_long_desc = 'Invalid docstring', expected_blank_short_desc = True
expected_blank_long_desc = True, expected_full_desc = 'Invalid docstring'

    @pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc", [
        ("Invalid docstring", None, "Invalid docstring", True, True, "Invalid docstring")
    ])
    def test_invalid_input(source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc):
        docstring = parse(source)
>       assert docstring.short_description == expected_short_desc
E       AssertionError: assert 'Invalid docstring' == None
E        +  where 'Invalid docstring' = <docstring_parser.common.Docstring object at 0x1048ca0e0>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_newlines_0_test_invalid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_newlines_0_test_invalid_input.py::test_invalid_input[Invalid docstring-None-Invalid docstring-True-True-Invalid docstring]
============================== 1 failed in 0.05s ===============================
"""