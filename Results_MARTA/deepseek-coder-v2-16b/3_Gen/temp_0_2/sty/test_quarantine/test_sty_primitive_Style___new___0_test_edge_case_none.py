
from sty import StylingRule, RgbFg, Sgr  # Importing from module 'sty.primitive'
from typing import Iterable

class Style:
    """
    A class representing a style with multiple styling rules and an ANSI sequence.
    
    Attributes:
        rules (Iterable[StylingRule]): An iterable of StylingRule objects that define the style rules.
    
    Methods:
        __new__(cls, *rules: StylingRule, value: str = ""): Creates a new instance of Style with given rules and optional ANSI sequence value.
    
    Examples:
        Creating a Style object with specific rules:
            style = Style(RgbFg(1, 5, 10), Sgr(1))
        
        Checking the type of the created object:
            isinstance(style, Style) # True
            isinstance(style, str) # True
        
        Converting the Style object to a string representation (ANSI sequence):
            str_representation = str(style)  # '[38;2;1;5;10m[1m'
    
    Note:
        The `__new__` method is overridden to create an instance of the class itself, which behaves like a string (ANSI sequence). This allows for easy conversion and manipulation as a string while carrying the styling rules.
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
************* Module Test4DT_tests.test_sty_primitive_Style___new___0_test_edge_case_none
sty/Test4DT_tests/test_sty_primitive_Style___new___0_test_edge_case_none.py:24:49: E2513: Invalid unescaped character esc, use "\x1B" instead. (invalid-character-esc)
sty/Test4DT_tests/test_sty_primitive_Style___new___0_test_edge_case_none.py:24:63: E2513: Invalid unescaped character esc, use "\x1B" instead. (invalid-character-esc)
sty/Test4DT_tests/test_sty_primitive_Style___new___0_test_edge_case_none.py:2:0: E0611: No name 'StylingRule' in module 'sty' (no-name-in-module)


"""