
import pytest
from unittest.mock import patch, MagicMock
from httpie.models import HTTPResponse

def test_iter_lines():
    # Create a mock HTTPResponse object
    mock_response = MagicMock()
    mock_response.iter_lines.return_value = ["line1", "line2", "line3"]
    
    # Create an instance of HTTPResponse with the mocked response
    http_response = HTTPResponse(orig=mock_response)
    
    # Call the iter_lines method
    result = list(http_response.iter_lines(chunk_size=1024))
    
    # Assert that the result is as expected
    assert result == [("line1", b'\n'), ("line2", b'\n'), ("line3", b'\n')]
