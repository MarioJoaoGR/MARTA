
import unittest
from httpie.models import HTTPMessage
from typing import Iterable

class TestHTTPMessageIterLines(unittest.TestCase):
    def test_edge_case(self):
        class MyHTTPMessage(HTTPMessage):
            def iter_lines(self, chunk_size: int) -> Iterable[bytes]:
                body = self._orig['body']  # Assuming the original data contains a 'body' key
                for line in body.split(b'\n'):
                    yield line + b'\r\n'
        
        msg = MyHTTPMessage({'body': b'Line1\nLine2\nLine3'})
        lines = list(msg.iter_lines(chunk_size=10))
        self.assertEqual([b'Line1\r\n', b'Line2\r\n', b'Line3\r\n'], lines)
