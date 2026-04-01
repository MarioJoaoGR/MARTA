
import pytest
from sty import renderfunc

def eightbit_fg(num: int) -> str:
    """
    Create a 8-bit (256-color) foreground escape sequence.
    
    This function generates an ANSI escape code for setting the foreground color in a terminal or console to an 8-bit color specified by `num`. The `num` parameter should be an integer between 0 and 255, where each value corresponds to a specific color in the 256-color palette.
    
    Parameters:
        num (int): An integer representing the color index in the 256-color palette. Must be within the range of 0 to 255 inclusive.
        
    Returns:
        str: A string containing the ANSI escape code for setting the foreground color.
    
    Example:
        To set the foreground color to a specific value, you can call the function like this:
        
        >>> eightbit_fg(123)
        '\033[38;5;123m'
        
        This will change the foreground color of your terminal or console output to the color corresponding to index 123 in the 256-color palette.
    """
    if not (0 <= num <= 255):
        raise ValueError("num must be between 0 and 255")
    return "\033[38;5;" + str(num) + "m"

def test_invalid_input():
    # Test with invalid string input
    with pytest.raises(ValueError):
        eightbit_fg("invalid")

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
        # Test with invalid string input
        with pytest.raises(ValueError):
>           eightbit_fg("invalid")

sty/Test4DT_tests/test_sty_renderfunc_eightbit_fg_2_test_invalid_input.py:32: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

num = 'invalid'

    def eightbit_fg(num: int) -> str:
        """
        Create a 8-bit (256-color) foreground escape sequence.
    
        This function generates an ANSI escape code for setting the foreground color in a terminal or console to an 8-bit color specified by `num`. The `num` parameter should be an integer between 0 and 255, where each value corresponds to a specific color in the 256-color palette.
    
        Parameters:
            num (int): An integer representing the color index in the 256-color palette. Must be within the range of 0 to 255 inclusive.
    
        Returns:
            str: A string containing the ANSI escape code for setting the foreground color.
    
        Example:
            To set the foreground color to a specific value, you can call the function like this:
    
            >>> eightbit_fg(123)
            '\033[38;5;123m'
    
            This will change the foreground color of your terminal or console output to the color corresponding to index 123 in the 256-color palette.
        """
>       if not (0 <= num <= 255):
E       TypeError: '<=' not supported between instances of 'int' and 'str'

sty/Test4DT_tests/test_sty_renderfunc_eightbit_fg_2_test_invalid_input.py:25: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_renderfunc_eightbit_fg_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.02s ===============================

"""