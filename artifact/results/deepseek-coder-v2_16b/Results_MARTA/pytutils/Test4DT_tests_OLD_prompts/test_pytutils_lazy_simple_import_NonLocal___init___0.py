
import pytest
from pytutils.lazy.simple_import import NonLocal

def test_nonlocal_creation():
    nl = NonLocal(10)
    assert nl.value == 10, "The value should be initialized to the provided argument."

def test_modify_value():
    nl = NonLocal(10)
    def modify_value():
        nonlocal nl
        nl.value += 1
        return nl.value
    
    assert modify_value() == 11, "The value should be incremented by 1."

def test_modify_multiple_values():
    nl1 = NonLocal(10)
    nl2 = NonLocal(20)
    def modify_value():
        nonlocal nl1, nl2
        nl1.value += 1
        nl2.value += 2
        return nl1.value, nl2.value
    
    assert modify_value() == (11, 22), "The values should be incremented by the specified amounts."
