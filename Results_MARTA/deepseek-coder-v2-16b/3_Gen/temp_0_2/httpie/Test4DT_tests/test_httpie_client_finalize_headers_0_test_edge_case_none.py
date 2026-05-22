
import unittest
from httpie.client import finalize_headers, HTTPHeadersDict
from unittest.mock import patch

class TestFinalizeHeaders(unittest.TestCase):
    
    @patch('httpie.client.HTTPHeadersDict')
    def test_edge_case_none(self, MockHTTPHeadersDict):
        # Arrange
        headers = MockHTTPHeadersDict()
        headers.items.return_value = [('Content-Type', 'application/json'), ('Set-Cookie', 'cookie1=value1;')]
        
        expected_headers = MockHTTPHeadersDict()
        expected_headers.add = lambda name, value: None  # We don't care about the return value here
        
        # Act
        finalized_headers = finalize_headers(headers)
        
        # Assert
        self.assertEqual(finalized_headers, expected_headers)
