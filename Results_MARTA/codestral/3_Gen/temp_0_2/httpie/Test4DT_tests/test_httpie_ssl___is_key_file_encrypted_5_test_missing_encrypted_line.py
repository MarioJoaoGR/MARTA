
import pytest
from httpie.ssl_ import _is_key_file_encrypted

@pytest.fixture
def create_temp_key_file():
    # Create a temporary key file for testing
    with open('/tmp/test_key_file.txt', 'w') as f:
        f.write("This is a test key file.")
    yield '/tmp/test_key_file.txt'
    # Clean up the temporary file after the test
    import os
    os.remove('/tmp/test_key_file.txt')

def test_missing_encrypted_line(create_temp_key_file):
    assert not _is_key_file_encrypted(create_temp_key_file), "Expected the key file to be unencrypted"
