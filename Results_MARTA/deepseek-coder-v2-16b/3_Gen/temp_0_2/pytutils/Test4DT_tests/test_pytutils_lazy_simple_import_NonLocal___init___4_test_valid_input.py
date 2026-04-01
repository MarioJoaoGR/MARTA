
import pytest
from pytutils.lazy.simple_import import NonLocal

def test_valid_input():
    nl = NonLocal(10)
    assert nl.value == 10, "Expected initial value to be 10"
    
    def modify_value():
        nonlocal nl
        nl.value += 5
    
    modify_value()
    assert nl.value == 15, "Expected value after modification to be 15"
