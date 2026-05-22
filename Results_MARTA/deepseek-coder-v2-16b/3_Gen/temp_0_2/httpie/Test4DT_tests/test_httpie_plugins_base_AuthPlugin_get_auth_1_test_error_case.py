
import pytest
from unittest.mock import patch, MagicMock
from httpie.plugins.base import AuthPlugin

class CustomAuth(AuthPlugin):
    def get_auth(self, username: str = None, password: str = None):
        raise NotImplementedError()

def test_error_case():
    with pytest.raises(NotImplementedError):
        auth = CustomAuth()
        auth.get_auth()
