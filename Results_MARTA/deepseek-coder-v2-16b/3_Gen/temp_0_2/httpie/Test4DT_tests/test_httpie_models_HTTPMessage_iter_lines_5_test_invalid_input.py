
import unittest
from httpie.models import HTTPMessage
from unittest.mock import patch, MagicMock

class TestHTTPMessageIterLines(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaises(NotImplementedError):
            msg = HTTPMessage({'body': 'invalid'})  # Invalid input to trigger NotImplementedError
            for line in msg.iter_lines(chunk_size=10):
                pass
