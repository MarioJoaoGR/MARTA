
# Module: isort.parse
# test_isort_parse.py
from isort.parse import normalize_line
import re

def test_normalize_line_simple():
    normalized_line, raw_line = normalize_line("from .cimport numpy")
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_parse_normalize_line_0.py F               [100%]

=================================== FAILURES ===================================
__________________________ test_normalize_line_simple __________________________

    def test_normalize_line_simple():
        normalized_line, raw_line = normalize_line("from .cimport numpy")
>       assert normalized_line == 'from  cimport numpy'
E       AssertionError: assert 'from . cimport numpy' == 'from  cimport numpy'
E         
E         - from  cimport numpy
E         + from . cimport numpy
E         ?      +

isort/Test4DT_tests/test_isort_parse_normalize_line_0.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_parse_normalize_line_0.py::test_normalize_line_simple
============================== 1 failed in 0.10s ===============================
"""