
import pytest
from flutils.decorators import cached_property

# Test for edge case where property is deleted and then recomputed
def test_edge_case():
    class MyClassEdgeCase:
        def __init__(self):
            self.x = 5
        
        @cached_property
        def y(self):
            return self.x + 1
    
    obj = MyClassEdgeCase()
    assert obj.y == 6, "Initial computation of cached property should be correct"
    
    del obj.__dict__['y']
    assert obj.y == 6, "Recomputation after deleting the attribute should yield the same result"

# Test for invalid input where a function without @cached_property is used as a property
def test_invalid_input():
    class InvalidClass:
        pass
    
    with pytest.raises(AttributeError):
        @cached_property
        def x(): return 1
        
        obj = InvalidClass()
        print(obj.x)  # This should raise a TypeError due to invalid decorator usage
