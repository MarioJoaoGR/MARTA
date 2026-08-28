
import pytest
from ansible.galaxy.token import GalaxyToken



def test_get_method_with_token():
    token_value = "your-galaxy-token"
    galaxy_token = GalaxyToken(token=token_value)
    retrieved_token = galaxy_token.get()
    assert retrieved_token == token_value