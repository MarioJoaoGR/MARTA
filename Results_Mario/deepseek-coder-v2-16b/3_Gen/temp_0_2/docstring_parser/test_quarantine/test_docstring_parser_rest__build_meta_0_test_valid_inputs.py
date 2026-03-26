
import pytest
from docstring_parser.common import DocstringMeta, DocstringParam, ParseError
from docstring_parser.rest import _build_meta, PARAM_KEYWORDS, RETURNS_KEYWORDS, YIELDS_KEYWORDS, DEPRECATION_KEYWORDS, RAISES_KEYWORDS
import re

def test_valid_inputs():
    # Test for parameter with default value
    meta1 = _build_meta(args=["param1", "int", "p1"], desc="This is param1 which defaults to an integer.")
    assert isinstance(meta1, DocstringParam)

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

docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test for parameter with default value
        meta1 = _build_meta(args=["param1", "int", "p1"], desc="This is param1 which defaults to an integer.")
>       assert isinstance(meta1, DocstringParam)
E       assert False
E        +  where False = isinstance(<docstring_parser.common.DocstringMeta object at 0x106374c10>, DocstringParam)

docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_rest__build_meta_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.04s ===============================
"""