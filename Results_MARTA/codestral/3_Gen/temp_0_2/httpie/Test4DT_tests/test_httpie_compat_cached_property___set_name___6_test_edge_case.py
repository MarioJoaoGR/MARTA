
import pytest
from httpie.compat import cached_property

class TestCachedProperty:
    def test_edge_case(self):
        class MyClass:
            def __init__(self):
                self._name = None
            
            @cached_property
            def name(self):
                return "example"
        
        my_instance = MyClass()
        assert my_instance.name == "example"
