
import pytest
from httpie.uploads import ChunkedUploadStream
from collections.abc import Iterable
import io

def test_valid_input():
    # Create a mock file-like object for testing
    mock_stream = io.BytesIO(b'test data')
    
    # Instantiate the ChunkedUploadStream with the mock stream and a callback function that does nothing
    upload_stream = ChunkedUploadStream(stream=mock_stream, callback=lambda x: None)
    
    # Read the chunks from the stream and ensure they are processed correctly
    chunks = []
    for chunk in upload_stream:
        chunks.append(chunk)
    
    assert len(chunks) == 1
    assert chunks[0] == b'test data'

