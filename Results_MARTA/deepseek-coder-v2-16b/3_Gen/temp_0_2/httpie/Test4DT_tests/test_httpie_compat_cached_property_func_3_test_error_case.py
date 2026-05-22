
import pytest
from unittest.mock import patch
from httpie.compat import cached_property

class MyClass:
    @cached_property
    def expensive_calculation(self):
        raise TypeError('Expected error')

def test_error_case():
    with patch('httpie.compat.cached_property.__init__', return_value=None):
        obj = MyClass()
        with pytest.raises(TypeError) as excinfo:
            print(obj.expensive_calculation)
    assert str(excinfo.value) == 'Expected error'
