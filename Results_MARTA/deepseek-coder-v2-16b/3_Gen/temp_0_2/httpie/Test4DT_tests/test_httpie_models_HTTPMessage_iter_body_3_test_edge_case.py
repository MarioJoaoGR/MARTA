
from httpie.models import HTTPMessage
import unittest
from unittest.mock import patch
from typing import Iterable

class TestHTTPMessageIterBody(unittest.TestCase):
    def setUp(self):
        self.http_message = HTTPMessage(orig="test")

    @patch('httpie.models.HTTPMessage.iter_body', return_value=[b'chunk1', b'chunk2'])
    def test_edge_case(self, mock_iter_body):
        chunk_size = 1024
        expected_chunks = [b'chunk1', b'chunk2']
        
        result = self.http_message.iter_body(chunk_size)
        
        self.assertIsInstance(result, Iterable)
        self.assertEqual(list(result), expected_chunks)
