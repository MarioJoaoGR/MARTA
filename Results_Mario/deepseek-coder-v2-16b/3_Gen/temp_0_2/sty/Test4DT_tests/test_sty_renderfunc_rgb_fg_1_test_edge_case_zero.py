
import pytest
from sty import renderfunc

def test_edge_case_zero():
    assert renderfunc.rgb_fg(0, 0, 0) == '\x1b[38;2;0;0;0m'
