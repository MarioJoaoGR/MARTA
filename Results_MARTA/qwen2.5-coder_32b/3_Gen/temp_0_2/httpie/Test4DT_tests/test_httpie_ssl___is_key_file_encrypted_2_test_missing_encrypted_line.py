
import pytest
from unittest.mock import patch
from httpie.ssl_ import _is_key_file_encrypted

@pytest.fixture
def create_temp_key_file():
    # Create a temporary key file for testing
    with open('/tmp/test_key_file.txt', 'w') as f:
        f.write("Some content without ENCRYPTED")
    yield '/tmp/test_key_file.txt'
    # Clean up the temporary file after the test
    import os
    os.remove('/tmp/test_key_file.txt')

def test_missing_encrypted_line(create_temp_key_file):
    with patch('httpie.ssl_.open', create=False) as mock_open:
        # Mock the file content to not contain "ENCRYPTED"
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.readlines.return_value = ["Line 1", "Line 2"]
        
        assert not _is_key_file_encrypted(create_temp_key_file), "Expected the key file to be unencrypted"
