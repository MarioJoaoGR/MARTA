
import pytest
from unittest.mock import patch
from ansible.galaxy.token import BasicAuthToken

def test_invalid_inputs():
    with pytest.raises(TypeError):
        BasicAuthToken()  # Should raise TypeError because username is required but not provided

