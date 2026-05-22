
import unittest
from unittest.mock import patch
from httpie.compat import cached_property

class TestCachedProperty(unittest.TestCase):
    def test_set_name(self):
        class MyClass:
            @cached_property
            def url(self):
                return "http://example.com"
        
        obj = MyClass()
        self.assertEqual(obj.url, "http://example.com")
