
import unittest
from httpie.models import HTTPMessage
from typing import Iterable

class TestHTTPMessageIterLines(unittest.TestCase):
    def test_edge_case_none(self):
        with self.assertRaises(NotImplementedError):
            msg = HTTPMessage(None)
            for line, _ in msg.iter_lines(chunk_size=10):
                pass
