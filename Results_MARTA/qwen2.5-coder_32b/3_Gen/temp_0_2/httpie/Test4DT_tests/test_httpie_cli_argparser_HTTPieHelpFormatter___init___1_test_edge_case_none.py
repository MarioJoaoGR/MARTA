
import unittest
from httpie.cli.argparser import HTTPieHelpFormatter

class TestHTTPieHelpFormatter(unittest.TestCase):
    def test_edge_case_none(self):
        with self.assertRaises(TypeError):
            formatter = HTTPieHelpFormatter()
