
import argparse
from httpie.cli.argparser import HTTPieArgumentParser, HTTPieHelpFormatter
import unittest
from unittest.mock import patch

class TestHTTPieArgumentParser(unittest.TestCase):
    @patch('httpie.cli.argparser.HTTPieHelpFormatter')
    def test_valid_inputs(self, MockHTTPieHelpFormatter):
        parser = HTTPieArgumentParser(formatter_class=MockHTTPieHelpFormatter)
        self.assertIsInstance(parser.formatter_class, type(MockHTTPieHelpFormatter))
