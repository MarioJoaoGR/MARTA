
import pytest
from ansible.galaxy.token import GalaxyToken

def test_none_input():
    galaxy_token = GalaxyToken(None)
    assert galaxy_token.get() is None, f"Expected None but got {galaxy_token.get()}"
