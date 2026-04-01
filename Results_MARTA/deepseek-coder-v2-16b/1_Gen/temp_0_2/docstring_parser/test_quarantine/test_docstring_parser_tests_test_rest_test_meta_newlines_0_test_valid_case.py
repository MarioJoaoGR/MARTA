
import pytest
from docstring_parser.tests.test_rest import parse
import typing as T

def test_meta_newlines():
    source = "This is a brief description.\n\nHere is a more detailed explanation."
    expected_short_desc = "This is a brief description."
    expected_long_desc = "Here is a more detailed explanation."
    expected_blank_short_desc = True
    expected_blank_long_desc = True
    expected_full_desc = "This is a brief description.\n\nHere is a more detailed explanation."

    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc
    assert docstring.blank_after_short_description == expected_blank_short_desc
    assert docstring.blank_after_long_description == expected_blank_long_desc

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_newlines_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
______________________________ test_meta_newlines ______________________________

    def test_meta_newlines():
        source = "This is a brief description.\n\nHere is a more detailed explanation."
        expected_short_desc = "This is a brief description."
        expected_long_desc = "Here is a more detailed explanation."
        expected_blank_short_desc = True
        expected_blank_long_desc = True
        expected_full_desc = "This is a brief description.\n\nHere is a more detailed explanation."
    
        docstring = parse(source)
        assert docstring.short_description == expected_short_desc
        assert docstring.long_description == expected_long_desc
        assert docstring.blank_after_short_description == expected_blank_short_desc
>       assert docstring.blank_after_long_description == expected_blank_long_desc
E       assert False == True
E        +  where False = <docstring_parser.common.Docstring object at 0x103abe980>.blank_after_long_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_newlines_0_test_valid_case.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_newlines_0_test_valid_case.py::test_meta_newlines
============================== 1 failed in 0.03s ===============================
"""