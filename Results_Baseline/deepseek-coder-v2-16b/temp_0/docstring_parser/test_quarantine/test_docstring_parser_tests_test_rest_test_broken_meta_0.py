
import pytest
from docstring_parser import ParseError
from docstring_parser.tests.test_rest import test_broken_meta

def test_parse():
    with pytest.raises(ParseError):
        test_broken_meta()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_broken_meta_0.py . [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________________________ test_parse __________________________________

    def test_parse():
>       with pytest.raises(ParseError):
E       Failed: DID NOT RAISE <class 'docstring_parser.common.ParseError'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_broken_meta_0.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_broken_meta_0.py::test_parse
========================= 1 failed, 1 passed in 0.02s ==========================

"""