
import unittest
from unittest.mock import patch
from httpie.compat import cached_property

class MyClass:
    def get_absolute_url(self):
        return "http://example.com"
    
    url = cached_property(get_absolute_url)

class TestHttpieCompatCachedPropertyInit(unittest.TestCase):
    @patch('httpie.compat.cached_property')
    def test_edge_case(self, mock_cached_property):
        # Arrange
        obj = MyClass()
        
        # Act
        result = obj.url
        
        # Assert
        self.assertEqual(result, "http://example.com")
