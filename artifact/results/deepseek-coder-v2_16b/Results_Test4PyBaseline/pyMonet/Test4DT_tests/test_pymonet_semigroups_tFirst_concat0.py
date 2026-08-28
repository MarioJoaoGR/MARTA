
import pytest
from pymonet.semigroups import First  # Assuming the module is correctly imported as such

# Test creating an instance with an initial value
def test_create_instance():
    f1 = First(10)
    assert f1.value == 10

# Test combining two instances to retain the first value
def test_concat_same_type():
    f1 = First(10)
    f2 = First(20)
    combined = f1.concat(f2)
    assert combined.value == 10

# Test creating an instance with a different type of value
def test_create_instance_different_type():
    f_str = First("hello")
    assert f_str.value == "hello"

# Test combining instances with values of different types, where the first type determines the result
def test_concat_different_types():
    f_int = First(10)
    f_str = First("hello")
    combined = f_int.concat(f_str)