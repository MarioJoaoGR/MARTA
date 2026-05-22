
import pytest
from unittest.mock import patch, MagicMock
from httpie.models import HTTPMessage

def test_invalid_input():
    with pytest.raises(NotImplementedError):
        msg = HTTPMessage(orig=None)
        for chunk in msg.iter_body(chunk_size=1024):
            pass
