
import pytest
from sty.rendertype import RgbBg

def test_invalid_input():
    with pytest.raises(ValueError):
        # Test case for invalid input where r, g, b are not integers or out of the valid range (0-255)
        RgbBg("not an integer", 64, 32)
        # This should raise a ValueError because 'not an integer' is not an integer.
        
    with pytest.raises(ValueError):
        # Test case for invalid input where r, g, b are out of the valid range (0-255)
        RgbBg(256, 64, 32)
        # This should raise a ValueError because 256 is not within the valid range.
        
    with pytest.raises(ValueError):
        # Test case for invalid input where r, g, b are out of the valid range (0-255)
        RgbBg(-1, 64, 32)
        # This should raise a ValueError because -1 is not within the valid range.

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

sty/Test4DT_tests/test_sty_rendertype_RgbBg___init___2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

sty/Test4DT_tests/test_sty_rendertype_RgbBg___init___2_test_invalid_input.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_rendertype_RgbBg___init___2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.02s ===============================
"""