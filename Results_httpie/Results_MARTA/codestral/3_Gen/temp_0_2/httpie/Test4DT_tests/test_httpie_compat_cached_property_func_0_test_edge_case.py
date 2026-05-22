
import pytest
from unittest.mock import patch
from httpie.compat import cached_property

class MyClass:
    @cached_property
    def expensive_calculation(self):
        return 42

def test_edge_case():
    with patch('httpie.compat.cached_property.__init__', lambda self, func, name=None: None):
        obj = MyClass()
        assert obj.expensive_calculation == 42
