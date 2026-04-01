
import pytest
from string_utils.manipulation import decompress

def test_invalid_encoding():
    with pytest.raises(ValueError):
        decompress("example", "invalid-encoding")
