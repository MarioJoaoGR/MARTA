
import pytest
from isort.wrap_modes import _hanging_indent_end_line

def test_none_input():
    with pytest.raises(TypeError):
        _hanging_indent_end_line(None)

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

isort/Test4DT_tests/test_isort_wrap_modes__hanging_indent_end_line_1_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        with pytest.raises(TypeError):
>           _hanging_indent_end_line(None)

isort/Test4DT_tests/test_isort_wrap_modes__hanging_indent_end_line_1_test_none_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

line = None

    def _hanging_indent_end_line(line: str) -> str:
>       if not line.endswith(" "):
E       AttributeError: 'NoneType' object has no attribute 'endswith'

isort/isort/wrap_modes.py:112: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_wrap_modes__hanging_indent_end_line_1_test_none_input.py::test_none_input
============================== 1 failed in 0.11s ===============================
"""