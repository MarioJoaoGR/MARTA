
import base64
import zlib
from string_utils.manipulation import decompress

# Helper function to compress a string for testing purposes
def compress(input_string: str, encoding: str = 'utf-8') -> str:
    input_bytes = input_string.encode(encoding)
    compressed_bytes = zlib.compress(input_bytes)
    return base64.urlsafe_b64encode(compressed_bytes).decode('ascii')

# Test case for valid decompression with default utf-8 encoding
def test_valid_case():
    original_string = 'Hello, World!'
    compressed_string = compress(original_string)
    assert decompress(compressed_string) == original_string

# Test case for valid decompression with specified ascii encoding
def test_valid_case_with_encoding():
    original_string = 'Hello, World!'
    compressed_string = compress(original_string, encoding='ascii')
    assert decompress(compressed_string, encoding='ascii') == original_string

# Test case for empty input string

# Test case for invalid base64 input string
def test_invalid_base64_input_string():
    invalid_compressed_string = 'invalid-base64-string'
    try:
        decompress(invalid_compressed_string)
    except Exception as e:
        assert isinstance(e, (base64.binascii.Error, zlib.error))

# Test case for invalid encoding
def test_invalid_encoding():
    original_string = 'Hello, World!'
    compressed_string = compress(original_string)
    try:
        decompress(compressed_string, encoding='invalid-encoding')
    except LookupError as e:
        assert str(e) == "unknown encoding: invalid-encoding"