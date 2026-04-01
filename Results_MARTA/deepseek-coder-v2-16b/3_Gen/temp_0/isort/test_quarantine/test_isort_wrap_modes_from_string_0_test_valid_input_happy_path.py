
import pytest
from isort.wrap_modes import WrapModes, from_string

def test_valid_input_happy_path():
    # Test with a valid string representation of a wrap mode
    result = from_string("WRAP")
    assert result == WrapModes.WRAP

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

isort/Test4DT_tests/test_isort_wrap_modes_from_string_0_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        # Test with a valid string representation of a wrap mode
>       result = from_string("WRAP")

isort/Test4DT_tests/test_isort_wrap_modes_from_string_0_test_valid_input_happy_path.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

value = 'WRAP'

    def from_string(value: str) -> "WrapModes":
>       return getattr(WrapModes, str(value), None) or WrapModes(int(value))
E       ValueError: invalid literal for int() with base 10: 'WRAP'

isort/isort/wrap_modes.py:14: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_wrap_modes_from_string_0_test_valid_input_happy_path.py::test_valid_input_happy_path
============================== 1 failed in 0.10s ===============================
"""