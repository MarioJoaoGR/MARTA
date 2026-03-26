
import pytest
from sty import rendertype

def test_rgb_fg_initialization():
    # Test initialization with valid RGB values
    rgb = rendertype.RgbFg(0, 255, 0)
    assert rgb.args == [0, 255, 0]
    
    # Test initialization with another set of valid RGB values
    rgb_blue = rendertype.RgbFg(0, 0, 255)
    assert rgb_blue.args == [0, 0, 255]
    
    # Test initialization with invalid RGB values (out of range)
    with pytest.raises(ValueError):
        rendertype.RgbFg(-1, 255, 0)  # Invalid red value
        
    with pytest.raises(ValueError):
        rendertype.RgbFg(256, 255, 0)  # Invalid red value
        
    with pytest.raises(ValueError):
        rendertype.RgbFg(0, -1, 0)  # Invalid green value
        
    with pytest.raises(ValueError):
        rendertype.RgbFg(0, 256, 0)  # Invalid green value
        
    with pytest.raises(ValueError):
        rendertype.RgbFg(0, 0, -1)  # Invalid blue value
        
    with pytest.raises(ValueError):
        rendertype.RgbFg(0, 0, 256)  # Invalid blue value

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
        # Test initialization with valid RGB values
        rgb = rendertype.RgbFg(0, 255, 0)
        assert rgb.args == [0, 255, 0]
    
        # Test initialization with another set of valid RGB values
        rgb_blue = rendertype.RgbFg(0, 0, 255)
        assert rgb_blue.args == [0, 0, 255]
    
        # Test initialization with invalid RGB values (out of range)
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

sty/Test4DT_tests/test_sty_rendertype_RgbFg___init___2_test_invalid_input.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_rendertype_RgbFg___init___2_test_invalid_input.py::test_rgb_fg_initialization
============================== 1 failed in 0.02s ===============================
"""