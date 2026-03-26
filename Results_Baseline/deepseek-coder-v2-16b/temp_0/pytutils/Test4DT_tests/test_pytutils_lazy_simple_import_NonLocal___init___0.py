# Module: pytutils.lazy.simple_import
# Import the function correctly from its module
from pytutils.lazy.simple_import import NonLocal

def test_nonlocal_initialization():
    # Test creating an instance with an initial value
    nl = NonLocal(10)
    assert nl.value == 10, "Expected the initial value to be set correctly"

def test_modify_value():
    # Test modifying the value of the instance
    nl = NonLocal(10)
    assert nl.value == 10, "Initial value should be 10"
    nl.value = 20
    assert nl.value == 20, "Expected the value to be modified to 20"

def test_multiple_instances():
    # Test creating multiple instances with different initial values
    nl1 = NonLocal(5)
    assert nl1.value == 5, "First instance should have a value of 5"
    
    nl2 = NonLocal(15)
    assert nl2.value == 15, "Second instance should have a value of 15"
