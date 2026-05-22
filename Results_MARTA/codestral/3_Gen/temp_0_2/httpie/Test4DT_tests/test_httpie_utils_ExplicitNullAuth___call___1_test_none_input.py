
import unittest
from unittest.mock import patch
from httpie.utils import ExplicitNullAuth

class TestExplicitNullAuth(unittest.TestCase):
    def test_none_input(self):
        # Create an instance of ExplicitNullAuth
        null_auth = ExplicitNullAuth()
        
        # Mock the request object to be passed to __call__ method
        mock_request = unittest.mock.Mock()
        
        # Call the __call__ method and check if it returns the same mocked request
        result = null_auth(mock_request)
        self.assertIs(result, mock_request)
