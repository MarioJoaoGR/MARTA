
import pytest
from sty import renderfunc

def test_edge_case_zero():
    assert renderfunc.eightbit_bg(0) == "\033[48;5;0m"
