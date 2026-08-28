
import pytest
from ansible.galaxy.api import GalaxyAPI
import os

@pytest.fixture(scope="module")
def api_client():
    return GalaxyAPI('specific_galaxy', 'username123', 'https://specific-server.com', clear_response_cache=True)

def test_clearing_cache(api_client):
    assert not os.path.exists(api_client._b_cache_path), f"Cache file {api_client._b_cache_path} should not exist after clearing."
