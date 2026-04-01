
import pytest
from isort.wrap_modes import formatter_from_string, grid

def test_none_input():
    # Test when input name is None
    assert callable(formatter_from_string(None))
    assert isinstance(formatter_from_string(None), type(grid))

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

isort/Test4DT_tests/test_isort_wrap_modes_formatter_from_string_0_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        # Test when input name is None
>       assert callable(formatter_from_string(None))

isort/Test4DT_tests/test_isort_wrap_modes_formatter_from_string_0_test_none_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

name = None

    def formatter_from_string(name: str) -> Callable[..., str]:
>       return _wrap_modes.get(name.upper(), grid)
E       AttributeError: 'NoneType' object has no attribute 'upper'

isort/isort/wrap_modes.py:18: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_wrap_modes_formatter_from_string_0_test_none_input.py::test_none_input
============================== 1 failed in 0.11s ===============================
"""