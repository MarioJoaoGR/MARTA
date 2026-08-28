
import pytest
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture(scope="module")
def api_client():
    return GalaxyAPI('exampleGalaxy', 'exampleClient', 'https://galaxy.ansible.com')

def test_valid_input(api_client):
    results = api_client.search_roles(search='webserver')
    assert isinstance(results, dict), "Expected a dictionary response"
    assert 'data' in results, "Expected 'data' key in the response"
    assert len(results['data']) > 0, "Expected non-empty data in the response"

def test_edge_case(api_client):
    # Test with None and empty values
    results = api_client.search_roles(search=None)
    assert isinstance(results, dict), "Expected a dictionary response"
    assert 'data' not in results, "Expected no data key when search is None"
    
    results = api_client.search_roles(search='')
    assert isinstance(results, dict), "Expected a dictionary response"
    assert 'data' not in results, "Expected no data key when search is empty"

def test_invalid_input(api_client):
    with pytest.raises(TypeError) as excinfo:
        api_client.search_roles()  # Missing required argument 'search'
    assert "'search'" in str(excinfo.value), "Expected a TypeError indicating missing 'search' argument"
