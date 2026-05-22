
import unittest
from httpie.compat import cached_property
from unittest.mock import patch, MagicMock

class MyClass:
    def get_absolute_url(self):
        return "http://example.com"
    
    url = cached_property(get_absolute_url)

class TestHttpieCompatCachedPropertyInit(unittest.TestCase):
    @patch('httpie.compat.cached_property.__init__')
    def test_edge_case(self, mock_init):
        obj = MyClass()
        self.assertEqual(obj.url, "http://example.com")
