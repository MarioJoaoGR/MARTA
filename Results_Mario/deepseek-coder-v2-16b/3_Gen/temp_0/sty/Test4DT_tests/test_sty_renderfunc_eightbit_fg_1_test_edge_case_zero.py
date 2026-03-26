
import pytest
from sty import renderfunc

def eightbit_fg(num: int) -> str:
    """
    Create a 8-bit (256-color) foreground escape sequence.
    """
    return "\033[38;5;" + str(num) + "m"

def test_edge_case_zero():
    assert eightbit_fg(0) == "\033[38;5;0m"
