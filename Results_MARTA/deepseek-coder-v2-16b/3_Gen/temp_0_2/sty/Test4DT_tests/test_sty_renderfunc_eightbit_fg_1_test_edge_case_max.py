
import pytest
from sty import renderfunc

def test_edge_case_max():
    """
    Test edge case with maximum value (255)
    """
    assert renderfunc.eightbit_fg(255) == "\033[38;5;255m"
