
import pytest
from unittest.mock import patch, MagicMock
from httpie.models import HTTPRequest

def test_edge_case_none():
    # Create a mock HTTPRequest object with a body attribute
    mock_request = MagicMock()
    mock_request.body = b"test_data"
    
    # Instantiate the HTTPRequest class with the mock request
    http_request = HTTPRequest(orig=mock_request)
    
    # Create an iterator over the body of the mock request
    chunk_size = 5
    chunks = []
    for chunk in http_request.iter_body(chunk_size):
        chunks.append(chunk)
    
    # Assert that the chunks are equal to the original body split by the chunk size
    assert b''.join(chunks) == mock_request.body
