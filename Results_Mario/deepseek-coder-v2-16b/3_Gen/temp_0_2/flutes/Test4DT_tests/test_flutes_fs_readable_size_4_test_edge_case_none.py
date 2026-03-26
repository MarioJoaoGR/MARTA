
import pytest
from flutes.fs import readable_size

def test_edge_case_none():
    assert readable_size(0) == "0.00"
