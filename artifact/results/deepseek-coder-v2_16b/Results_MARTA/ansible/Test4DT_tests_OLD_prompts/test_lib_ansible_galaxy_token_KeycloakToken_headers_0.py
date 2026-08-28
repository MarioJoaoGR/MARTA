
import pytest
from unittest.mock import patch
from ansible.galaxy.token import KeycloakToken



def test_invalid_inputs():
    with pytest.raises(ValueError):
        with patch('ansible.galaxy.token.KeycloakToken.__init__', side_effect=ValueError):
            KeycloakToken()