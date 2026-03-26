# Module: pytutils.lazy.simple_import
import pytest
from pytutils.lazy.simple_import import NonLocal

# Test initialization of NonLocal class
def test_nonlocal_initialization():
    nl = NonLocal(10)
    assert nl.value == 10, "Initialization with value 10 failed"

# Test using the instance in a function
def test_outer_function():
    nl = NonLocal(10)
    def outer_function():
        nonlocal_var = 5
        def inner_function():
            nonlocal nl
            print(nl.value)  # Outputs the initial value of `value` which is 10
            nl.value += 1     # Increments the `value` by 1
        inner_function()
        assert nl.value == 11, "Value was not incremented correctly in inner function"
        print(nonlocal_var)  # Outputs the initial value of `nonlocal_var` which is 5
    outer_function()

# Test accessing the Value Attribute
def test_accessing_value():
    nl = NonLocal(10)
    assert nl.value == 10, "Accessing value failed"

# Test modifying the Value Attribute
def test_modifying_value():
    nl = NonLocal(10)
    def modify_value():
        nonlocal nl
        print("Initial value:", nl.value)  # Outputs: Initial value: 10
        nl.value += 1
        assert nl.value == 11, "Value was not modified correctly"
        print("Modified value:", nl.value)  # Outputs: Modified value: 11
    modify_value()

# Run the tests
if __name__ == "__main__":
    pytest.main()
