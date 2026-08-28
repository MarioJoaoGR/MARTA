
import pytest
from ansible.galaxy.api import GalaxyAPI
import os

@pytest.fixture(scope="module")
def api_client():
    return GalaxyAPI('custom_galaxy', 'specialUser', 'https://custom-server.com', no_cache=True, priority=1.0)


def test_clearing_response_cache():
    api_client = GalaxyAPI('clear_cache_galaxy', 'clearUser', 'https://clear-server.com', clear_response_cache=True)
    assert not os.path.exists(api_client._b_cache_path), "Cache file should have been cleared but it still exists"