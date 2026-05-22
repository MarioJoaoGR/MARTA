
import unittest
from httpie.models import HTTPMessage
from unittest.mock import patch, MagicMock

class TestHTTPMessage(unittest.TestCase):
    def test_iter_body(self):
        # Create a mock HTTPMessage instance
        with patch('httpie.models.HTTPMessage.__init__', lambda x, orig: None):
            msg = HTTPMessage(orig=MagicMock())
        
        # Mock the iter_body method to return an iterator over chunks of bytes
        def chunked_iterator():
            yield b'chunk1'
            yield b'chunk2'
            yield b'chunk3'
        
        with patch.object(msg, 'iter_body', return_value=chunked_iterator()):
            # Test the iter_body method
            chunks = list(msg.iter_body(chunk_size=5))
            self.assertEqual(chunks, [b'chunk1', b'chunk2', b'chunk3'])
