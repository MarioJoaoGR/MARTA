
import pytest
from httpie.uploads import ChunkedUploadStream
from unittest.mock import patch, MagicMock

def test_valid_inputs():
    # Create a mock callback function
    def mock_callback(chunk):
        pass

    # Create a mock iterable stream
    mock_stream = [b'part1', b'part2', b'part3']

    # Create an instance of ChunkedUploadStream with the mock data and callback
    uploader = ChunkedUploadStream(mock_stream, mock_callback)

    # Iterate over the stream to simulate processing each chunk
    for i, chunk in enumerate(uploader):
        assert chunk == mock_stream[i]
