
import pytest
from sty import renderfunc

def test_edge_case_zero():
    assert renderfunc.sgr(0) == "\033[0m"
