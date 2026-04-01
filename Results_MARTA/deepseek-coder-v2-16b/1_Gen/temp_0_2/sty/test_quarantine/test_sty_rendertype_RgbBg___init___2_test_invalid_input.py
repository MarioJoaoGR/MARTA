
import pytest
from sty.rendertype import RgbBg

def test_invalid_input():
    with pytest.raises(TypeError):
        # This should raise a TypeError because the constructor expects integers, not strings or other invalid types
        RgbBg("invalid", "input", "types")

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
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

sty/Test4DT_tests/test_sty_rendertype_RgbBg___init___2_test_invalid_input.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_rendertype_RgbBg___init___2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.02s ===============================
"""