
import pytest
from pytutils.memo import lazyproperty

class MyClass:
    @lazyproperty
    def expensive_calculation(self):
        # Perform a computationally expensive operation here
        return 42

def test_valid_input():
    obj = MyClass()
    
    # First access should perform the calculation
    assert obj.expensive_calculation == 42
    
    # Subsequent accesses should not perform the calculation again, but use the cached result
    assert obj.expensive_calculation == 42
