
import pytest
from unittest.mock import patch, MagicMock
from httpie.compat import cached_property

class MyClass:
    def get_absolute_url(self):
        return 'http://example.com'
    
    url = cached_property(get_absolute_url)

def test_valid_input():
    obj = MyClass()
    assert obj.url == 'http://example.com'
