
import unittest
from httpie.models import HTTPMessage
from typing import Iterable

class TestHTTPMessageIterLines(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaises(NotImplementedError):
            msg = HTTPMessage({})  # Assuming an empty dictionary is passed as orig
            for line, _ in msg.iter_lines(chunk_size=10):
                pass
