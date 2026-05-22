
import pytest
from httpie.encoding import detect_encoding, UTF8, TOO_SMALL_SEQUENCE
from unittest.mock import patch

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test that an invalid input raises a TypeError
        detect_encoding(None)  # Passing None as content which is not allowed by the function signature
