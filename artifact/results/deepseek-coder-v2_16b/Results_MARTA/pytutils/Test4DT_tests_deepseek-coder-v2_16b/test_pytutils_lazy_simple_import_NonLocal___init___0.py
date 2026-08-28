
import pytest
from pytutils.lazy.simple_import import NonLocal  # Replace 'your_module' with the actual module name where NonLocal is defined

def test_nonlocal_creation():
    nl = NonLocal(10)
    assert hasattr(nl, 'value'), "NonLocal instance should have a 'value' attribute"
    assert nl.value == 10, "The initial value of the NonLocal instance should be 10"

def test_nonlocal_modification():
    nl = NonLocal(10)
    def modify_value():
        nonlocal nl
        nl.value += 1
        return nl.value
    
    assert modify_value() == 11, "Modifying the value should increment it by 1"

def test_nonlocal_multiple_instances():
    nl1 = NonLocal(10)
    nl2 = NonLocal(20)
    def modify_values():
        nonlocal nl1, nl2
        nl1.value += 1
        nl2.value += 2
        return nl1.value, nl2.value
    
    value1, value2 = modify_values()
    assert value1 == 11, "The first instance's value should be incremented by 1"
    assert value2 == 22, "The second instance's value should be incremented by 2"
