
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.base import AuthPlugin

class TestAuthPlugin:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.plugin = AuthPlugin()

    def test_get_auth_invalid_input(self):
        with pytest.raises(NotImplementedError):
            self.plugin.get_auth('invalid', 'input')
