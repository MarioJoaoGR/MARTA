
import pytest
from unittest.mock import patch, MagicMock
from httpie.models import HTTPMessage

def test_iter_body_error_case():
    # Create a mock instance of HTTPMessage for testing
    msg = HTTPMessage(orig=MagicMock())
    
    with pytest.raises(NotImplementedError):
        list(msg.iter_body(chunk_size=-1))
