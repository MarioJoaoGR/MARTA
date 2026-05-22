
import pytest
from unittest.mock import patch, MagicMock
from httpie.models import HTTPMessage

def test_iter_body_invalid_input():
    with pytest.raises(NotImplementedError):
        msg = HTTPMessage(None)
        msg.iter_body(10)
