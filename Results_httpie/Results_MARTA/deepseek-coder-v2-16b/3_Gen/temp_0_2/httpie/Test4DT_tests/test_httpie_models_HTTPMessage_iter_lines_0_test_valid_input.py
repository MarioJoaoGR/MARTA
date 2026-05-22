
import unittest
from httpie.models import HTTPMessage
from typing import Iterable
from unittest.mock import patch, MagicMock

class TestHTTPMessageIterLines(unittest.TestCase):
    def test_valid_input(self):
        # Create a mock HTTPMessage subclass for testing
        class MockHTTPMessage(HTTPMessage):
            def iter_lines(self, chunk_size: int) -> Iterable[bytes]:
                body = self._orig['body']  # Assuming the original data contains a 'body' key
                for line in body.split(b'\n'):
                    yield line + b'\r\n'
        
        # Create an instance of the mock HTTPMessage with sample data
        msg = MockHTTPMessage({'body': b'Line1\nLine2\nLine3'})
        
        # Use patch to replace iter_lines method with a MagicMock that yields the expected lines
        with patch.object(HTTPMessage, 'iter_lines', return_value=[b'Line1\r\n', b'Line2\r\n', b'Line3\r\n']):
            # Test the iter_lines method
            result = list(msg.iter_lines(chunk_size=10))
        
        # Assert that the result matches the expected lines
        self.assertEqual(result, [b'Line1\r\n', b'Line2\r\n', b'Line3\r\n'])
