# Module: flutils.decorators
# test_cached_property.py
from flutils.decorators import cached_property
import pytest

class MyClass:
    def __init__(self):
        self.x = 5
        
    @cached_property
    def y(self):
        return self.x + 1

@pytest.fixture
def my_instance():
    return MyClass()

def test_cached_property_initial_value(my_instance):
    assert my_instance.y == 6

def test_cached_property_cached_value(my_instance):
    # First access should set the value
    first_access = my_instance.y
    # Subsequent accesses should return the cached value
    second_access = my_instance.y
    assert first_access == 6
    assert second_access == 6

def test_cached_property_reset_on_deletion(my_instance):
    # Access the property to set its value in the instance dictionary
    initial_value = my_instance.y
    assert initial_value == 6
    
    # Delete the attribute to simulate deletion and trigger a recalculation
    del my_instance.y
    new_value = my_instance.y
    assert new_value == 6  # The value should be recalculated since it was deleted
