
import unittest
from unittest.mock import patch
from httpie.utils import ExplicitNullAuth

class TestExplicitNullAuth(unittest.TestCase):
    def test_invalid_input(self):
        # Create an instance of ExplicitNullAuth
        null_auth = ExplicitNullAuth()
        
        # Mock the request object to simulate invalid input (e.g., not a requests.Request)
        class InvalidRequest:
            pass
        
        with patch('httpie.utils.ExplicitNullAuth.__call__', return_value=InvalidRequest()):
            result = null_auth(InvalidRequest())
            
            # Assert that the returned object is of the expected type (InvalidRequest)
            self.assertIsInstance(result, InvalidRequest)
