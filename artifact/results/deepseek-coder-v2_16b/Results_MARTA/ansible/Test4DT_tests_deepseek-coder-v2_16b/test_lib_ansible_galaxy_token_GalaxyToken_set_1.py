
import pytest
from ansible.galaxy.token import GalaxyToken

def test_set_method():
    galaxy_token = GalaxyToken()
    token = "test_token"
    galaxy_token.set(token)
    assert galaxy_token._token == token
    assert galaxy_token.get() == token
