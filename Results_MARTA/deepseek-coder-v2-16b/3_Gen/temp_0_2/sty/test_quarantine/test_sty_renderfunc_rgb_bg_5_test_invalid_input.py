
import pytest
from sty import renderfunc

def rgb_bg(r: int, g: int, b: int) -> str:
    """
    Create a 24-bit (true color) background escape sequence.
    
    This function generates an ANSI escape code that sets the background color of the terminal to the specified RGB values. The RGB values are integers ranging from 0 to 255.
    
    Parameters:
        r (int): The red component of the RGB color, ranging from 0 to 255.
        g (int): The green component of the RGB color, ranging from 0 to 255.
        b (int): The blue component of the RGB color, ranging from 0 to 255.
    
    Returns:
        str: A string representing the ANSI escape code for setting a true-color background.
    
    Example:
        To set the background color to a vibrant green (#00FF00), you can use:
        
        >>> rgb_bg(0, 255, 0)
        '\x1b[48;2;0;255;0m'
    
    Note:
        The returned string should be used in conjunction with a terminal that supports true color.
    """
    return "\x1b[48;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m"

def test_invalid_input():
    with pytest.raises(TypeError):
        rgb_bg("invalid", 255, 0)

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

sty/Test4DT_tests/test_sty_renderfunc_rgb_bg_5_test_invalid_input.py F   [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

sty/Test4DT_tests/test_sty_renderfunc_rgb_bg_5_test_invalid_input.py:31: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_renderfunc_rgb_bg_5_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.02s ===============================
"""