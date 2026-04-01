
from sty import rendertype

class EightbitBg:
    """
    Define an 8-bit background color for a terminal or console application using ANSI escape codes.
    
    More info about 8-bit terminal colors can be found at this link: https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit
    
    :param num: An integer representing the 8-bit color number. Valid values are from 0 to 255.
    :raises ValueError: If the provided `num` is not within the range of 0 to 255, a ValueError will be raised.
    
    Example usage:
    ```python
    # Create an 8-bit background color with the number 12
    bg_color = EightbitBg(12)
    
    # Use the color in your application
    print("\033[48;5;" + str(bg_color.num) + "m Your text here \033[0m")
    ```
    
    In this example, `\033[48;5;<num>m` is the ANSI escape code for setting a background color in an 8-bit terminal. The `<num>` should be replaced with the value of `num` from the EightbitBg instance. After printing your text, you should reset the color using `\033[0m`.
    """
    def __init__(self, num: int):
        if not (0 <= num <= 255):
            raise ValueError("num must be between 0 and 255")
        self.num = num

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.01s =============================
"""