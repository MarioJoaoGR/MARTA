
import pytest
from sty import RgbBg

# Test initialization with valid RGB values
def test_rgb_bg_initialization():
    rgb_bg = RgbBg(128, 64, 32)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

sty/Test4DT_tests/test_sty_rendertype_RgbBg___init___0.py .FFF.          [100%]

=================================== FAILURES ===================================
__________________________ test_rgb_bg_invalid_values __________________________

    def test_rgb_bg_invalid_values():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

sty/Test4DT_tests/test_sty_rendertype_RgbBg___init___0.py:12: Failed
________________________ test_rgb_bg_non_integer_values ________________________

    def test_rgb_bg_non_integer_values():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

sty/Test4DT_tests/test_sty_rendertype_RgbBg___init___0.py:17: Failed
_________________________ test_rgb_bg_negative_values __________________________

    def test_rgb_bg_negative_values():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

sty/Test4DT_tests/test_sty_rendertype_RgbBg___init___0.py:22: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_rendertype_RgbBg___init___0.py::test_rgb_bg_invalid_values
FAILED sty/Test4DT_tests/test_sty_rendertype_RgbBg___init___0.py::test_rgb_bg_non_integer_values
FAILED sty/Test4DT_tests/test_sty_rendertype_RgbBg___init___0.py::test_rgb_bg_negative_values
========================= 3 failed, 2 passed in 0.02s ==========================

"""