
import pytest
from flutils.decorators import cached_property

# Scenario 1: Test standard input
def test_valid_input():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    # Ensure the property is cached and not recomputed
    obj.x = 10
    assert obj.y == 6, "Expected cached value to remain unchanged"

# Scenario 2: Test edge cases including None and empty lists
def test_edge_case():
    class MyClass:
        @cached_property
        def y(self):
            return None

    # Test with None input
    obj = MyClass()
    assert obj.y is None, "Expected cached property to handle None correctly"

    # Test with empty list input
    class MyClassWithList:
        @cached_property
        def y(self):
            return []

    obj_list = MyClassWithList()
    assert obj_list.y == [], "Expected cached property to handle empty list correctly"

# Scenario 3: Test invalid inputs and error handling
def test_invalid_input():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    with pytest.raises(TypeError):
        # Attempt to call the property without an instance should raise a TypeError
        obj.y()
