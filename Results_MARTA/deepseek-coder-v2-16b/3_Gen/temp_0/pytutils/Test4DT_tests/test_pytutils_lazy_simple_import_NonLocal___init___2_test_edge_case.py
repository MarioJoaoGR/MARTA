
import pytest
from pytutils.lazy.simple_import import NonLocal  # Correctly specify the module and class

def test_edge_case():
    nl = NonLocal(10)
    assert nl.value == 10
    nl.value = 20
    assert nl.value == 20
