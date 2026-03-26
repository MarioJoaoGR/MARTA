
# Module: sty.rendertype
# Import the function from the module
from sty.rendertype import EightbitFg
import pytest

def test_eightbitfg_initialization():
    # Test initialization with a valid 8-bit number
    color = EightbitFg(1)
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

sty/Test4DT_tests/test_sty_rendertype_EightbitFg___init___0.py .F.       [100%]

=================================== FAILURES ===================================
________________________ test_eightbitfg_invalid_input _________________________

    def test_eightbitfg_invalid_input():
        # Test initialization with an invalid 8-bit number (should raise a ValueError)
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

sty/Test4DT_tests/test_sty_rendertype_EightbitFg___init___0.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_rendertype_EightbitFg___init___0.py::test_eightbitfg_invalid_input
========================= 1 failed, 2 passed in 0.02s ==========================

"""