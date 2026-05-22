
import pytest
from unittest.mock import patch
from httpie.compat import cached_property

class MyClass:
    @cached_property
    def expensive_calculation(self):
        return 42

def test_valid_case():
    obj = MyClass()
    
    with patch('httpie.compat.cached_property') as mock_cached_property:
        # Mock the cached property to ensure it is called and returns a specific value
        mock_cached_property.return_value.__get__ = lambda _, instance: 42
        
        assert obj.expensive_calculation == 42
