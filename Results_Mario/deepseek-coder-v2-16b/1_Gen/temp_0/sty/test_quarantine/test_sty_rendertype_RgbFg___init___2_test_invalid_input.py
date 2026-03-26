
import pytest
from sty import rendertype

def test_rgb_fg_initialization():
    # Test valid RGB initialization
    rgb = rendertype.RgbFg(0, 255, 0)
    assert rgb.args == [0, 255, 0]
    
    # Test another valid RGB initialization
    rgb_another = rendertype.RgbFg(128, 64, 32)
    assert rgb_another.args == [128, 64, 32]
    
    # Test invalid RGB initialization (should raise an error or incorrect value)
    with pytest.raises(TypeError):
        rendertype.RgbFg("invalid", "input", "values")

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

sty/Test4DT_tests/test_sty_rendertype_RgbFg___init___2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
__________________________ test_rgb_fg_initialization __________________________

    def test_rgb_fg_initialization():
        # Test valid RGB initialization
        rgb = rendertype.RgbFg(0, 255, 0)
        assert rgb.args == [0, 255, 0]
    
        # Test another valid RGB initialization
        rgb_another = rendertype.RgbFg(128, 64, 32)
        assert rgb_another.args == [128, 64, 32]
    
        # Test invalid RGB initialization (should raise an error or incorrect value)
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

sty/Test4DT_tests/test_sty_rendertype_RgbFg___init___2_test_invalid_input.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_rendertype_RgbFg___init___2_test_invalid_input.py::test_rgb_fg_initialization
============================== 1 failed in 0.02s ===============================

"""