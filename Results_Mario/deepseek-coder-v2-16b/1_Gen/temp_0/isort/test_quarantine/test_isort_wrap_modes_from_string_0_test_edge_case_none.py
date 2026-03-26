
import pytest
from isort.wrap_modes import WrapModes, from_string

def test_edge_case_none():
    input_value = None
    assert from_string(input_value) is None

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

isort/Test4DT_tests/test_isort_wrap_modes_from_string_0_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        input_value = None
>       assert from_string(input_value) is None

isort/Test4DT_tests/test_isort_wrap_modes_from_string_0_test_edge_case_none.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

value = None

    def from_string(value: str) -> "WrapModes":
>       return getattr(WrapModes, str(value), None) or WrapModes(int(value))
E       TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'

isort/isort/wrap_modes.py:14: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_wrap_modes_from_string_0_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.26s ===============================
"""