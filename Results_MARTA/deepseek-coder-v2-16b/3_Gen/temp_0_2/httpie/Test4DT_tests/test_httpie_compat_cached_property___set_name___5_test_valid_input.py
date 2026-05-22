
import unittest
from httpie.compat import cached_property

class MyClass:
    def get_absolute_url(self):
        return "http://example.com"
    
    url = cached_property(get_absolute_url)

class TestMyClass(unittest.TestCase):
    def test_valid_input(self):
        obj = MyClass()
        self.assertEqual(obj.url, "http://example.com")
