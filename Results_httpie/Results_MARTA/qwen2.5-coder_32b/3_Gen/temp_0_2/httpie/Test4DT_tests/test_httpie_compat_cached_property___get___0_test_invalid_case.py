
import pytest
from unittest.mock import patch
from httpie.compat import cached_property

class MyClass:
    def __init__(self, value):
        self.value = value
    
    @cached_property
    def expensive_calculation(self):
        print("Performing expensive calculation")
        return self.value * 2

def test_invalid_case():
    obj = MyClass(10)
    
    with patch('httpie.compat.cached_property.__get__', return_value=20):
        result = obj.expensive_calculation
    
    assert result == 20, f"Expected 20 but got {result}"
