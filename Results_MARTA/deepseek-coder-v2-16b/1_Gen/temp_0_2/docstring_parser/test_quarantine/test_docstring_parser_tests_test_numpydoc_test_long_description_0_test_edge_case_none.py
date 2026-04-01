
from docstring_parser.common import Docstring
from docstring_parser.tests.test_numpydoc import parse

def test_edge_case_none():
    source = None
    expected_short_desc = ""
    expected_long_desc = ""
    expected_blank = False

    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc
    assert docstring.blank_after_short_description == expected_blank
    assert not docstring.meta

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_long_description_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        source = None
        expected_short_desc = ""
        expected_long_desc = ""
        expected_blank = False
    
        docstring = parse(source)
>       assert docstring.short_description == expected_short_desc
E       AssertionError: assert None == ''
E        +  where None = <docstring_parser.common.Docstring object at 0x101c32470>.short_description

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_long_description_0_test_edge_case_none.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_long_description_0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.03s ===============================
"""