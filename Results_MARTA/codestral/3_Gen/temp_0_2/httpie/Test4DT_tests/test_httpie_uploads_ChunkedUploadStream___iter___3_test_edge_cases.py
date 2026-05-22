
import unittest
from httpie.uploads import ChunkedUploadStream
from typing import Iterable, Callable, Optional, Union
import threading

class TestChunkedUploadStream(unittest.TestCase):
    def test_edge_cases(self):
        class MockIterable:
            def __init__(self, data):
                self.data = data
            
            def __iter__(self):
                return iter(self.data)
        
        def mock_callback(chunk):
            pass  # Placeholder for the callback function
        
        data = [b'part1', b'part2', b'part3']
        stream = MockIterable(data)
        event = threading.Event()
        
        uploader = ChunkedUploadStream(stream, mock_callback, event)
        
        for i, chunk in enumerate(uploader):
            self.assertEqual(chunk, data[i])
