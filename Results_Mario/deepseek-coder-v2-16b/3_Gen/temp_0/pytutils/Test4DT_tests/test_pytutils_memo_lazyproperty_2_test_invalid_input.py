
import pytest
from pytutils.memo import lazyproperty

def test_invalid_input():
    class MyClass:
        @lazyproperty
        def expensive_calculation(self):
            return sum(i**2 for i in range(1000))
    
    obj = MyClass()
    with pytest.raises(TypeError):  # Since the function expects 'self' as its first argument, passing no arguments should raise a TypeError
        obj.expensive_calculation()
