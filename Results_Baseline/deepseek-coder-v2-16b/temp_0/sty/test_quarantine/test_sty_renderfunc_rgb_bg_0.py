
# Module: sty.renderfunc
# Import the function correctly using its module name
from sty.renderfunc import rgb_bg
import pytest

# Test cases for rgb_bg function
def test_rgb_bg_valid():
    """Test that a valid RGB input returns the correct ANSI escape code."""
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

sty/Test4DT_tests/test_sty_renderfunc_rgb_bg_0.py .F.                    [100%]

=================================== FAILURES ===================================
__________________________ test_rgb_bg_invalid_range ___________________________

    def test_rgb_bg_invalid_range():
        """Test that an invalid RGB input raises a ValueError."""
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

sty/Test4DT_tests/test_sty_renderfunc_rgb_bg_0.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_renderfunc_rgb_bg_0.py::test_rgb_bg_invalid_range
========================= 1 failed, 2 passed in 0.02s ==========================

"""