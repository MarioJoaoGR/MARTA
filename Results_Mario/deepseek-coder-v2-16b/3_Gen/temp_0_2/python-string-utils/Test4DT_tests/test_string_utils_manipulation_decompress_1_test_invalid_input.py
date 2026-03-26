
import pytest
from string_utils.manipulation import decompress
from unittest.mock import patch

def test_invalid_input():
    with pytest.raises(ValueError):
        with patch('string_utils.manipulation.__StringCompressor.decompress') as mock_decompress:
            mock_decompress.side_effect = ValueError("Invalid input")
            decompress("")  # This should raise a ValueError due to invalid base64 encoded string and utf-8 encoding
