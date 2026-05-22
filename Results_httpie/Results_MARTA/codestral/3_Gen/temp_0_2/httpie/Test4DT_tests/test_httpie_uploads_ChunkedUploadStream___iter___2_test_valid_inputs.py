
import unittest
from httpie.uploads import ChunkedUploadStream
from typing import Iterable, Callable, Optional, Union
import threading

class TestChunkedUploadStream(unittest.TestCase):
    def test_valid_inputs(self):
        # Mock data and callback function
        mock_data = [b'part1', b'part2', b'part3']
        
        def mock_callback(chunk: bytes) -> None:
            pass  # No action needed for the mock callback

        # Create an instance of ChunkedUploadStream with valid inputs
        uploader = ChunkedUploadStream(mock_data, mock_callback)

        # Iterate over the stream and check if it yields chunks correctly
        chunk_iter = iter(uploader)
        for i, expected_chunk in enumerate(mock_data):
            with self.subTest(i=i):
                chunk = next(chunk_iter)
                self.assertEqual(chunk, expected_chunk)

    def test_with_event(self):
        # Mock data and callback function
        mock_data = [b'part1', b'part2', b'part3']
        
        def mock_callback(chunk: bytes) -> None:
            pass  # No action needed for the mock callback

        # Create an event to control iteration
        event = threading.Event()

        # Create an instance of ChunkedUploadStream with valid inputs and event
        uploader = ChunkedUploadStream(mock_data, mock_callback, event)

        # Iterate over the stream and check if it yields chunks correctly
        chunk_iter = iter(uploader)
        for i, expected_chunk in enumerate(mock_data):
            with self.subTest(i=i):
                chunk = next(chunk_iter)
                self.assertEqual(chunk, expected_chunk)
                # Set the event to signal processing of the chunk
                event.set()
