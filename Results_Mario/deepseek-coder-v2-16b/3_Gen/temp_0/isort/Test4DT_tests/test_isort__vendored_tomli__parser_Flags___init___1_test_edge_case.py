
from isort._vendored.tomli._parser import Flags
import pytest
from typing import Dict

def test_edge_case():
    flags = Flags()
    assert hasattr(flags, '_flags')
    assert isinstance(flags._flags, dict)
    assert flags._flags == {}
