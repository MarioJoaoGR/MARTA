
import pytest
from httpie.compat import cached_property

class MyClass:
    def get_absolute_url(self):
        return "http://example.com"
    
    url = cached_property(get_absolute_url)

def test_invalid_input():
    my_instance = MyClass()
    with pytest.raises(TypeError):
        my_instance.url = cached_property(my_instance.get_absolute_url, name="new_name")
