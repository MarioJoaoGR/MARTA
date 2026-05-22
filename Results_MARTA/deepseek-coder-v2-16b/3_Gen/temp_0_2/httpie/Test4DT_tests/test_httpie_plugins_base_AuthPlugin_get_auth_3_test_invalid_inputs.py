
import pytest
from unittest.mock import patch
from httpie.plugins.base import AuthPlugin

class TestAuthPlugin:
    def test_get_auth_invalid_input(self):
        plugin = AuthPlugin()
        with pytest.raises(NotImplementedError):
            plugin.get_auth('invalid', 'input')
