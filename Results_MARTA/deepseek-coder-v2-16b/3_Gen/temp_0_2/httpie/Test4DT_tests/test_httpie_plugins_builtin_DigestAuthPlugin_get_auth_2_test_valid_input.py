
import unittest
from unittest.mock import patch
import requests
from httpie.plugins.builtin import DigestAuthPlugin

class TestDigestAuthPlugin(unittest.TestCase):
    def setUp(self):
        self.plugin = DigestAuthPlugin()
    
    @patch('httpie.plugins.builtin.requests')
    def test_get_auth_valid_input(self, mock_requests):
        username = "user"
        password = "pass"
        
        expected_auth = mock_requests.auth.HTTPDigestAuth("user", "pass")
        
        result = self.plugin.get_auth(username, password)
        
        mock_requests.auth.HTTPDigestAuth.assert_called_with(username, password)
        self.assertEqual(result, expected_auth)
