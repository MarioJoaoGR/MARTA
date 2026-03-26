
import pytest
from pytutils.lazy.simple_import import NonLocal

def test_valid_input():
    nl = NonLocal(10)
    assert nl.value == 10
    nl.value = 20
    assert nl.value == 20
