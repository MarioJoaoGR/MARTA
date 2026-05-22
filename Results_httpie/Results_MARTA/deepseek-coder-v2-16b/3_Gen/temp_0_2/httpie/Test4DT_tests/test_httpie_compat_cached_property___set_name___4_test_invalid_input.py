
import pytest
from httpie.compat import cached_property

def test_invalid_input():
    class MyClass:
        def get_absolute_url(self):
            return "http://example.com"
    
        url = cached_property(get_absolute_url)
    
    obj = MyClass()
    with pytest.raises(TypeError):
        # This should raise a TypeError because the name argument is deprecated and not used in the implementation
        class DeprecatedClass:
            def __set_name__(self, owner, name):
                pass
        
        url = cached_property(MyClass.get_absolute_url, name="deprecated")
