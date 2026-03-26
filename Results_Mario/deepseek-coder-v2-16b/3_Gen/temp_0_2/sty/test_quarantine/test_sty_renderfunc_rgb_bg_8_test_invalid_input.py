
import pytest
from sty.renderfunc import rgb_bg

def test_invalid_input():
    with pytest.raises(ValueError):
        # Invalid red value (should be between 0 and 255)
        rgb_bg(-1, 0, 0)
        
        # Invalid green value (should be between 0 and 255)
        rgb_bg(0, -1, 0)
        
        # Invalid blue value (should be between 0 and 255)
        rgb_bg(0, 0, -1)
        
        # Invalid red value (out of range)
        rgb_bg(256, 0, 0)
        
        # Invalid green value (out of range)
        rgb_bg(0, 256, 0)
        
        # Invalid blue value (out of range)
        rgb_bg(0, 0, 256)

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

sty/Test4DT_tests/test_sty_renderfunc_rgb_bg_8_test_invalid_input.py F   [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

sty/Test4DT_tests/test_sty_renderfunc_rgb_bg_8_test_invalid_input.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_renderfunc_rgb_bg_8_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.02s ===============================
"""