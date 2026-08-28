
import base64
import zlib
from string_utils.manipulation import __StringCompressor
from string_utils.errors import InvalidInputError


def test_invalid_input_non_string():
    compressed_string = None
    try:
        __StringCompressor.decompress(compressed_string)
    except InvalidInputError as e:
        assert str(e) == 'Expected "str", received "NoneType"'

def test_invalid_base64_encoding():
    compressed_string = 'invalid-base64-string'
    try:
        __StringCompressor.decompress(compressed_string)
    except base64.binascii.Error as e:
        assert str(e) == 'Invalid base64-encoded string: number of data characters (21) cannot be 1 more than a multiple of 4'

