
import pytest
from string_utils.manipulation import decompress, __StringCompressor
from string_utils.validation import InvalidInputError

# Test valid base64-encoded and zlib-compressed input with default encoding (utf-8)

# Test valid base64-encoded and zlib-compressed input with specified encoding

# Test invalid input type (should raise InvalidInputError)
def test_invalid_input_type():
    with pytest.raises(InvalidInputError):
        decompress(None)

# Test empty input string (should raise InvalidInputError)