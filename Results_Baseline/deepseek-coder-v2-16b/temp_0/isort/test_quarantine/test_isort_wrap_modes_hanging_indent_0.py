
import pytest
from isort.wrap_modes import hanging_indent as target_function

# Test cases for the hanging_indent function

def test_hanging_indent_basic():
    result = target_function(imports=['import os', 'import sys'], statement='')
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

isort/Test4DT_tests/test_isort_wrap_modes_hanging_indent_0.py F          [100%]

=================================== FAILURES ===================================
__________________________ test_hanging_indent_basic ___________________________

    def test_hanging_indent_basic():
>       result = target_function(imports=['import os', 'import sys'], statement='')

isort/Test4DT_tests/test_isort_wrap_modes_hanging_indent_0.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

interface = {'imports': ['import os', 'import sys'], 'statement': ''}

    @_wrap_mode
    def hanging_indent(**interface: Any) -> str:
        if not interface["imports"]:
            return ""
    
>       line_length_limit = interface["line_length"] - 3
E       KeyError: 'line_length'

isort/isort/wrap_modes.py:122: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_wrap_modes_hanging_indent_0.py::test_hanging_indent_basic
============================== 1 failed in 0.10s ===============================
"""