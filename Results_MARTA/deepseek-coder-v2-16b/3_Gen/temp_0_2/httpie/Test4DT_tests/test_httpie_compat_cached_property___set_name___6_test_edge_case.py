
import unittest
from httpie.compat import cached_property as compat_cached_property

class TestCachedProperty(unittest.TestCase):
    def test_set_name(self):
        class MyClass:
            @compat_cached_property
            def url(self):
                return "http://example.com"
        
        obj = MyClass()
        self.assertEqual(obj.url, "http://example.com")
