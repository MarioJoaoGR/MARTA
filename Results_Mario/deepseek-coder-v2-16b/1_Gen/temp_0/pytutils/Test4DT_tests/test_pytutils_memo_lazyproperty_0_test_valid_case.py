
import pytest
from pytutils.memo import lazyproperty

class MyClass:
    @lazyproperty
    def expensive_calculation(self):
        # This computation is expensive and only needed in certain circumstances
        return sum(i**2 for i in range(1000))

def test_valid_case():
    obj = MyClass()
    
    # First call should compute the value
    assert obj.expensive_calculation == sum(i**2 for i in range(1000))
    
    # Subsequent calls should use the cached result
    assert obj.expensive_calculation == sum(i**2 for i in range(1000))
