
import pytest
import zlib
import base64
from unittest.mock import patch

class __StringCompressor:
    @classmethod
    def compress(cls, input_string: str, encoding: str = 'utf-8', compression_level: int = 9) -> str:
        cls.__require_valid_input_and_encoding(input_string, encoding)

        if not isinstance(compression_level, int) or compression_level < 0 or compression_level > 9:
            raise ValueError('Invalid compression_level: it must be an "int" between 0 and 9')

        # turns input string into a sequence of bytes using provided encoding
        original_bytes = input_string.encode(encoding)

        # compress bytes using zlib library
        compressed_bytes = zlib.compress(original_bytes, compression_level)

        # encode compressed bytes using base64
        # (this ensure that all characters will be available and that the output string can be used safely in any
        # context such URLs)
        encoded_bytes = base64.urlsafe_b64encode(compressed_bytes)

        # finally turns base64 bytes into a string
        output = encoded_bytes.decode(encoding)

        return output

    @staticmethod
    def __require_valid_input_and_encoding(input_string, encoding):
        if not isinstance(input_string, str):
            raise ValueError('Invalid input: it must be a string')
        if not isinstance(encoding, str):
            raise ValueError('Invalid encoding: it must be a string')
        if len(input_string) == 0:
            raise ValueError('Invalid input: the string should not be empty')

def test_invalid_input():
    with pytest.raises(ValueError):
        __StringCompressor.compress("")
    with pytest.raises(ValueError):
        __StringCompressor.compress("example", encoding=123)
    with pytest.raises(ValueError):
        __StringCompressor.compress("example", compression_level=-1)
