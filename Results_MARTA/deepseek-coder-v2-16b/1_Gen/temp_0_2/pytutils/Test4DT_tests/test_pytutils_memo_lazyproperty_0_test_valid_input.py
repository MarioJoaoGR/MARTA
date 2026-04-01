
import pytest
from pytutils.memo import lazyproperty

class MyClass:
    @lazyproperty
    def expensive_calculation(self):
        print('Calculating...')
        return sum(i**2 for i in range(1000))

def test_valid_input():
    obj = MyClass()
    
    # First access should trigger the calculation
    assert obj.expensive_calculation == sum(i**2 for i in range(1000))
    print('First access:', obj.expensive_calculation)  # Optional: to see the output during test run
    
    # Second access should not trigger the calculation again, as it should be cached
    assert obj.expensive_calculation == sum(i**2 for i in range(1000))
    print('Second access:', obj.expensive_calculation)  # Optional: to see the output during test run
