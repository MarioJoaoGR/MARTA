
import pytest
from unittest.mock import patch, MagicMock
from httpie.models import HTTPMessage

def test_invalid_input():
    with pytest.raises(NotImplementedError):
        msg = HTTPMessage({})
        for line in msg.iter_lines(chunk_size=10):
            pass
