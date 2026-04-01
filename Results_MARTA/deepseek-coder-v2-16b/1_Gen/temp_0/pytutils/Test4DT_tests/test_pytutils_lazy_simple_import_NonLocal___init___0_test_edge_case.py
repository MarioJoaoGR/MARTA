
import pytest
from pytutils.lazy.simple_import import NonLocal

def test_edge_case():
    nl = NonLocal(None)
    assert nl.value is None
