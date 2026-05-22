
import pytest
from unittest.mock import patch
from httpie.utils import humanize_bytes

def test_invalid_inputs():
    with pytest.raises(TypeError):
        humanize_bytes("not an integer")  # Test invalid input type
