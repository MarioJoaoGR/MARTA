
import unittest
from httpie.plugins.builtin import BasicAuthPlugin
from requests.auth import HTTPBasicAuth

class TestBasicAuthPlugin(unittest.TestCase):
    def setUp(self):
        self.plugin = BasicAuthPlugin()
    
    def test_get_auth(self):
        username = "testuser"
        password = "testpass"
        auth = self.plugin.get_auth(username, password)
        self.assertIsInstance(auth, HTTPBasicAuth)
        self.assertEqual(auth.username, username)
        self.assertEqual(auth.password, password)
