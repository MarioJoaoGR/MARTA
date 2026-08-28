
import pytest
from unittest.mock import patch, MagicMock
import zlib
import base64

class __StringCompressor:
    @classmethod
    def compress(cls, input_string: str, encoding: str = 'utf-8', compression_level: int = 9) -> str:
        cls.__require_valid_input_and_encoding(input_string, encoding)

        if not isinstance(compression_level, int) or compression_level < 0 or compression_level > 9:
            raise ValueError('Invalid compression_level: it must be an "int" between 0 and 9')

        original_bytes = input_string.encode(encoding)
        compressed_bytes = zlib.compress(original_bytes, compression_level)
        encoded_bytes = base64.urlsafe_b64encode(compressed_bytes)
        output = encoded_bytes.decode(encoding)

        return output

    @staticmethod
    def __require_valid_input_and_encoding(input_string, encoding):
        if not isinstance(input_string, str):
            raise ValueError("Invalid input: input_string must be a string")
        if not isinstance(encoding, str) or not encoding:
            raise ValueError("Invalid encoding: encoding must be a non-empty string")

# Test cases
def test_valid_input():
    with patch('zlib.compress', return_value=b'compressed'):
        with patch('base64.urlsafe_b64encode', return_value=b'encoded'):
            result = __StringCompressor.compress("example text")
            assert result == "encoded"

def test_edge_case_none():
    with pytest.raises(ValueError):
        __StringCompressor.compress(None)

def test_invalid_input():
    with pytest.raises(ValueError):
        __StringCompressor.compress("example text", compression_level=-1)
