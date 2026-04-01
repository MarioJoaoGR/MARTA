
import pytest
from isort.io import _EmptyIO

def test_edge_case_none():
    empty_io = _EmptyIO()
    assert empty_io.write(None) is None
