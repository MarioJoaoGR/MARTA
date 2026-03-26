
import pytest
from pytutils.memo import lazyproperty

# Define a class with a lazy property
class MyClass:
    @lazyproperty
    def expensive_calculation(self):
        # This computation is expensive and only needed in certain circumstances
        return sum(i**2 for i in range(1000))

def test_lazyproperty():
    obj = MyClass()
    
    # First call should compute the value
    assert obj.expensive_calculation == sum(i**2 for i in range(1000))
    
    # Subsequent calls should use the cached result
    previous_result = obj.expensive_calculation
    assert obj.expensive_calculation == previous_result
