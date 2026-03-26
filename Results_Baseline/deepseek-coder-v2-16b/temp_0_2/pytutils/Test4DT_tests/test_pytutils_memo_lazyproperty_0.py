
# Module: pytutils.memo
# Import the lazyproperty function from the pytutils.memo module
from pytutils.memo import lazyproperty

import pytest

# Example class to test the lazyproperty decorator
class MyClass:
    def __init__(self, x):
        self.x = x
    
    @lazyproperty
    def expensive_calculation(self):
        print('Calculating...')
        return self.x ** 2

# Test cases for the lazyproperty decorator
def test_lazyproperty_as_decorator():
    obj = MyClass(5)
    # First access: the calculation is performed and result stored
    assert obj.expensive_calculation == 25, "First access should perform the calculation"
    
    # Subsequent accesses: the cached value is returned without recalculation