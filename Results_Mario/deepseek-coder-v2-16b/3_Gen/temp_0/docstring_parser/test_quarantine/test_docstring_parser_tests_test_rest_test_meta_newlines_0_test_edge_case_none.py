
import pytest
from docstring_parser.tests.test_rest import parse

@pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc", [
    (None, None, None, False, False, None)
])
def test_meta_newlines(source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc):
    """Test parsing newlines around description sections."""
    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc
    assert docstring.blank_after_short_description == expected_blank_short_desc
    assert docstring.blank_after_long_description == expected_blank_long_desc
    assert docstring.description == expected_full_desc
    assert len(docstring.meta) == 1

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_newlines_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________ test_meta_newlines[None-None-None-False-False-None] ______________

source = None, expected_short_desc = None, expected_long_desc = None
expected_blank_short_desc = False, expected_blank_long_desc = False
expected_full_desc = None

    @pytest.mark.parametrize("source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc", [
        (None, None, None, False, False, None)
    ])
    def test_meta_newlines(source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc, expected_full_desc):
        """Test parsing newlines around description sections."""
        docstring = parse(source)
        assert docstring.short_description == expected_short_desc
        assert docstring.long_description == expected_long_desc
        assert docstring.blank_after_short_description == expected_blank_short_desc
        assert docstring.blank_after_long_description == expected_blank_long_desc
        assert docstring.description == expected_full_desc
>       assert len(docstring.meta) == 1
E       assert 0 == 1
E        +  where 0 = len([])
E        +    where [] = <docstring_parser.common.Docstring object at 0x102ff6440>.meta

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_newlines_0_test_edge_case_none.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_meta_newlines_0_test_edge_case_none.py::test_meta_newlines[None-None-None-False-False-None]
============================== 1 failed in 0.05s ===============================
"""