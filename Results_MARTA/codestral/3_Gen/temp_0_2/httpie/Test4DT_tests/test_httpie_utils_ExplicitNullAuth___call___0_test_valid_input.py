
import unittest
from unittest.mock import patch
from httpie.utils import ExplicitNullAuth

class TestExplicitNullAuth(unittest.TestCase):
    def test_valid_input(self):
        # Create an instance of ExplicitNullAuth
        null_auth = ExplicitNullAuth()
        
        # Mock a request object
        class MockRequest:
            pass
        
        mock_request = MockRequest()
        
        # Call the __call__ method and check if it returns the same mocked request
        result = null_auth(mock_request)
        self.assertIs(result, mock_request)
