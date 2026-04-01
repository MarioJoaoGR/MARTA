
from sty.primitive import StylingRule
from typing import Iterable

class Style:
    """
    This type stores the different styling rules for the registers and the resulting ANSI-sequence as a string.
    
    For example:
    
        fg.orange = Style(RgbFg(1,5,10), Sgr(1))
    
        isinstance(fg.orange, Style) # True
    
        isinstance(fg.orange, str) # True
    
        str(fg.orange) # '[38;2;1;5;10m[1m' (The ANSI sequence for orange and bold)
    """
    rules: Iterable[StylingRule]
    
    def __new__(cls, *rules: StylingRule, value: str = "") -> "Style":
        new_cls = str.__new__(cls, value)  # type: ignore
        setattr(new_cls, "rules", rules)
        return new_cls

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Style___new___1_test_invalid_input
sty/Test4DT_tests/test_sty_primitive_Style___new___1_test_invalid_input.py:17:27: E2513: Invalid unescaped character esc, use "\x1B" instead. (invalid-character-esc)
sty/Test4DT_tests/test_sty_primitive_Style___new___1_test_invalid_input.py:17:41: E2513: Invalid unescaped character esc, use "\x1B" instead. (invalid-character-esc)


"""