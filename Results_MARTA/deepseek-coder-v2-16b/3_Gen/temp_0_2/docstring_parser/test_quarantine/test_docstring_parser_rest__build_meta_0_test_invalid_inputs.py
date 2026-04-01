
import pytest
from docstring_parser.common import ParseError
from docstring_parser.rest import _build_meta, DocstringMeta, PARAM_KEYWORDS, RETURNS_KEYWORDS, YIELDS_KEYWORDS, DEPRECATION_KEYWORDS, RAISES_KEYWORDS
import re

def test_invalid_inputs():
    with pytest.raises(ParseError):
        _build_meta(["param1"], "This is param1 which defaults to an integer.")

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

docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       with pytest.raises(ParseError):
E       Failed: DID NOT RAISE <class 'docstring_parser.common.ParseError'>

docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_invalid_inputs.py:8: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.03s ===============================
"""