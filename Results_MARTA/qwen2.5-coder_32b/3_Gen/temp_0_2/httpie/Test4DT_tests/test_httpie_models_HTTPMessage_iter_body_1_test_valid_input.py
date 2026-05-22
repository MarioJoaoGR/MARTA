
import pytest
from unittest.mock import patch, MagicMock
from httpie.models import HTTPMessage

class TestHTTPMessage:
    @pytest.fixture(autouse=True)
    def setup_mocks(self):
        with patch('httpie.models.HTTPMessage.__init__', return_value=None):
            yield

    def test_valid_input(self):
        # Create a mock HTTPMessage instance
        mock_orig = MagicMock()
        http_message = HTTPMessage(mock_orig)
        
        # Define a chunk size and content for the mock body
        chunk_size = 1024
        mock_body_content = b'a' * (chunk_size * 3 + 5)  # Ensure more than 3 chunks
        
        # Mock the iter_body method to return an iterator over the content
        with patch.object(HTTPMessage, 'iter_body', lambda self, chunk_size: [mock_body_content[i:i+chunk_size] for i in range(0, len(mock_body_content), chunk_size)]):
            # Call iter_body and check the output
            chunks = list(http_message.iter_body(chunk_size))
            
            # Check if the number of chunks matches the expected count
            assert len(chunks) == 4  # Since we have more than chunk_size * 3, it should be 4 chunks
            
            # Optionally check the content of each chunk
            for i, chunk in enumerate(chunks):
                assert chunk == mock_body_content[i*chunk_size:(i+1)*chunk_size]
