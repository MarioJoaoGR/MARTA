
import pytest
from isort._vendored.tomli._parser import Flags

def test_edge_case_none():
    flags = Flags()
    assert not flags.is_((), 0)
