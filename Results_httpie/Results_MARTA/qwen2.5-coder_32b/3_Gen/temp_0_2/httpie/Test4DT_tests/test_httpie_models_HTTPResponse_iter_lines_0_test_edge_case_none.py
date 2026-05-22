
import unittest
from httpie.models import HTTPResponse
from unittest.mock import patch, MagicMock

class TestHTTPResponseIterLines(unittest.TestCase):
    def test_edge_case_none(self):
        # Create a mock HTTPResponse object
        mock_response = MagicMock()
        
        # Set up the side effect for iter_lines method to return an empty generator
        mock_response.iter_lines = lambda chunk_size: []
        
        # Create an instance of HTTPResponse with the mocked response
        http_response = HTTPResponse(orig=mock_response)
        
        # Call the iter_lines method and check if it returns the expected generator
        result = list(http_response.iter_lines(chunk_size=1024))
        
        # Assert that the result is an empty list, as per the edge case scenario
        self.assertEqual(result, [])
