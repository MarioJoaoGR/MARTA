
import unittest
from httpie.compat import cached_property

class TestCachedProperty(unittest.TestCase):
    def test_set_name(self):
        class MyClass:
            def get_absolute_url(self):
                return "http://example.com"
            
            url = cached_property(get_absolute_url)
        
        obj = MyClass()
        self.assertEqual(obj.url, "http://example.com")
