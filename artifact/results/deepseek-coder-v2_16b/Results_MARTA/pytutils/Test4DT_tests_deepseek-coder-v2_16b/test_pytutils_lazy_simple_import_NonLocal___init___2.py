
import pytest
from pytutils.lazy.simple_import import NonLocal

def test_nonlocal_creation():
    nl = NonLocal(10)
    assert nl.value == 10, "The value should be initialized to the provided argument."

def test_modify_value():
    nl = NonLocal(10)
    nl.value += 1
    assert nl.value == 11, "Modifying the value directly within an instance should change its value."

def test_modify_value_in_function():
    nl = NonLocal(10)
    def modify_value():
        nonlocal nl
        nl.value += 1
        return nl.value
    
    assert modify_value() == 11, "Modifying the value within a function should change its value."
