
import pytest
from pytutils.lazy.simple_import import NonLocal  # Assuming this is the correct module path

def test_nonlocal_initialization():
    nl = NonLocal(10)
    assert nl.value == 10, "Initialization with value should set the value correctly."

def test_nonlocal_modification():
    nl = NonLocal(10)
    nl.value = 20
    assert nl.value == 20, "Modifying the value should change it accordingly."
