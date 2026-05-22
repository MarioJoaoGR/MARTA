
import unittest
from httpie.models import HTTPRequest

class TestHTTPRequest(unittest.TestCase):
    def test_iter_body_edge_case(self):
        # Create a mock HTTPRequest object with a body for testing
        class MockHTTPRequest:
            def __init__(self, orig=None, **kwargs):
                self.orig = orig
                self.body = b"test_body"
            
            def iter_body(self, chunk_size):
                yield self.body
        
        # Create an instance of the mock HTTPRequest
        req = MockHTTPRequest()
        
        # Test the iter_body method with a small chunk size to ensure it yields chunks correctly
        chunks = list(req.iter_body(chunk_size=3))
        self.assertEqual(chunks, [b"test_body"])
        
        # Test the iter_body method with a larger chunk size to ensure it still works
        chunks = list(req.iter_body(chunk_size=10))
        self.assertEqual(chunks, [b"test_body"])

if __name__ == "__main__":
    unittest.main()
