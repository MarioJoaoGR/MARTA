
import pytest
from unittest.mock import patch, MagicMock
from httpie.uploads import ChunkedMultipartUploadStream
from requests_toolbelt import MultipartEncoder
import threading

def test_valid_inputs():
    # Create a mock MultipartEncoder instance
    encoder = MagicMock(spec=MultipartEncoder)
    encoder.read.return_value = b'chunk1'  # Mock the read method to return 'chunk1'
    
    # Create an event
    event = threading.Event()
    
    # Initialize the ChunkedMultipartUploadStream with the mock encoder and event
    upload_stream = ChunkedMultipartUploadStream(encoder, event)
    
    # Use the upload_stream as needed for your application
    chunks = []
    for chunk in upload_stream:
        chunks.append(chunk)
        if len(chunks) == 2:  # Ensure we get at least two chunks
            break
    
    assert len(chunks) == 2, "Expected exactly two chunks"
    assert all(isinstance(c, bytes) for c in chunks), "All chunks should be of type bytes"
    assert b'chunk1' in chunks, "Chunk 'chunk1' should be present in the chunks"
