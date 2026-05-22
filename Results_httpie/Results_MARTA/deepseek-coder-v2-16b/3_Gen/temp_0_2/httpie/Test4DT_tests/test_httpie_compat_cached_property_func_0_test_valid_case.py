
import pytest
from unittest.mock import patch
from httpie.compat import cached_property

class MyClass:
    @cached_property
    def expensive_calculation(self):
        return 42

def test_valid_case():
    obj = MyClass()
    with patch('httpie.compat.cached_property.__init__', return_value=None):
        assert obj.expensive_calculation == 42
