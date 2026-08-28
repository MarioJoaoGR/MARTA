
import pytest
from ansible.plugins.connection.psrp import read_gen
import os
import base64
import hashlib

# Define a simple function to create a temporary file with given content
def create_temp_file(content):
    temp_file = 'temp_binary_file'
    with open(temp_file, 'wb') as f:
        f.write(content)
    return temp_file

# Test scenarios
@pytest.fixture
def valid_case():
    # Setup a valid binary file for testing
    content = b'\x01\x02\x03\x04' * 1024  # Small binary file
    temp_file = create_temp_file(content)
    yield temp_file, len(content), hashlib.sha1(), None, "host", "in_path", "out_path"
    os.remove(temp_file)

@pytest.fixture
def edge_case():
    # Setup an empty file for testing
    temp_file = create_temp_file(b'')
    yield temp_file, 1024, hashlib.sha1(), None, "host", "in_path", "out_path"
    os.remove(temp_file)

@pytest.fixture
def invalid_input():
    # Setup a non-existent file for testing
    yield 'non_existent_file', 1024, hashlib.sha1(), None, "host", "in_path", "out_path"

# Test functions
def test_valid_case(valid_case):
    b_in_path, buffer_size, sha1_hash, display, _, in_path, out_path = valid_case
    gen = read_gen()
    encoded_chunks = list(gen)
    
    assert len(encoded_chunks) > 0, "Expected at least one encoded chunk"
    for chunk in encoded_chunks:
        assert isinstance(chunk, list), "Each chunk should be a list"
        assert len(chunk) == 1, "Each chunk should contain exactly one base64-encoded string"
        b64_data = base64.b64decode(chunk[0])
        assert len(b64_data) <= buffer_size, f"Decoded chunk size {len(b64_data)} exceeds buffer size {buffer_size}"
    
    # Verify SHA1 hash
    expected_sha1 = hashlib.sha1(content).hexdigest()
    assert sha1_hash.hexdigest() == expected_sha1, "SHA1 hash does not match the content of the file"

def test_edge_case(edge_case):
    b_in_path, buffer_size, sha1_hash, display, _, in_path, out_path = edge_case
    gen = read_gen()
    encoded_chunks = list(gen)
    
    assert len(encoded_chunks) == 0 or len(encoded_chunks[0]) == 1, "Expected either an empty chunk or a single base64-encoded string"
    
    if encoded_chunks:
        b64_data = base64.b64decode(encoded_chunks[0][0])
        assert len(b64_data) <= buffer_size, f"Decoded chunk size {len(b64_data)} exceeds buffer size {buffer_size}"
    
    # For an empty file, the SHA1 hash should be 0 (empty string)
    assert sha1_hash.hexdigest() == "da39a3ee5e6b4b0d3255bfef95601890afd80709", "SHA1 hash of an empty file should be 0"

def test_invalid_input(invalid_input):
    b_in_path, buffer_size, sha1_hash, display, _, in_path, out_path = invalid_input
    
    with pytest.raises(FileNotFoundError):
        gen = read_gen()
        list(gen)
