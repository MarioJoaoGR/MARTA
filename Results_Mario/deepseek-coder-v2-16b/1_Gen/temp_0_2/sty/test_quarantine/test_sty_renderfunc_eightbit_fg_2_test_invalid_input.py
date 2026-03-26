
import pytest
from sty import renderfunc

def test_invalid_input():
    with pytest.raises(ValueError):
        # Test non-integer values
        assert renderfunc.eightbit_fg("not a number") is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

sty/Test4DT_tests/test_sty_renderfunc_eightbit_fg_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(ValueError):
            # Test non-integer values
>           assert renderfunc.eightbit_fg("not a number") is None
E           AssertionError: assert '\x1b[38;5;not a numberm' is None
E            +  where '\x1b[38;5;not a numberm' = <function eightbit_fg at 0x105154670>('not a number')
E            +    where <function eightbit_fg at 0x105154670> = renderfunc.eightbit_fg

sty/Test4DT_tests/test_sty_renderfunc_eightbit_fg_2_test_invalid_input.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_renderfunc_eightbit_fg_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.02s ===============================
"""