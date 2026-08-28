
from flutils.decorators import cached_property
import pytest

# Test for edge case where accessing a non-existent attribute raises KeyError
def test_edge_case():
    class TestNoneAndEmpty:
        pass

    obj = TestNoneAndEmpty()
    with pytest.raises(KeyError):
        # Accessing the property should raise an AttributeError
        obj.__dict__['y']

# Test for invalid input where accessing a non-property attribute raises TypeError
def test_invalid_input():
    class TestTypeError:
        @cached_property
        def y(self):
            return None  # This will cause a TypeError when accessed as an attribute

    obj = TestTypeError()
    with pytest.raises(KeyError):
        # Accessing the property should raise a TypeError
        obj.__dict__['y']
