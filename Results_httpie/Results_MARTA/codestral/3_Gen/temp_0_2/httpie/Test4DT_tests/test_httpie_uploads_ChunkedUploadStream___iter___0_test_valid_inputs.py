
import pytest
from httpie.uploads import ChunkedUploadStream
from unittest.mock import patch, MagicMock

def test_valid_inputs():
    # Create a mock callback function
    def mock_callback(chunk):
        pass  # Do nothing with the chunk for this test

    # Create an iterable source of data
    stream = ['Chunk1', 'Chunk2', 'Chunk3']
    
    # Instantiate the ChunkedUploadStream with the mock callback and event
    uploader = ChunkedUploadStream(stream, mock_callback)

    # Iterate over the chunks to ensure they are yielded correctly
    for i, chunk in enumerate(uploader):
        assert chunk == stream[i]
