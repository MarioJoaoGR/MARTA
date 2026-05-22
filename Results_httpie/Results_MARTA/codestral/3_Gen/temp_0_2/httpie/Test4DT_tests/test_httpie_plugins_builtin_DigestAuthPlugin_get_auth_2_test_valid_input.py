
import unittest
from unittest.mock import patch
import requests
from httpie.plugins.builtin import DigestAuthPlugin

class TestDigestAuthPlugin(unittest.TestCase):
    def setUp(self):
        self.plugin = DigestAuthPlugin()
    
    @patch('requests.auth.HTTPDigestAuth')
    def test_get_auth_valid_input(self, mock_http_digest_auth):
        username = "user"
        password = "pass"
        
        # Call the method under test
        auth_obj = self.plugin.get_auth(username, password)
        
        # Assert that the correct arguments were passed to HTTPDigestAuth
        mock_http_digest_auth.assert_called_once_with(username, password)
        
        # Assert that the method returns the expected result
        self.assertEqual(auth_obj, mock_http_digest_auth.return_value)
