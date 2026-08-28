
import pytest
from ansible.galaxy.api import GalaxyAPI
import os

@pytest.fixture(scope="module")
def valid_inputs():
    return GalaxyAPI('exampleGalaxy', 'exampleClient', 'https://galaxy.ansible.com')

@pytest.fixture(scope="module")
def edge_cases():
    return GalaxyAPI(None, None, None)

@pytest.fixture(scope="module")
def invalid_inputs():
    try:
        return GalaxyAPI('exampleGalaxy', '', 'https://galaxy.ansible.com')
    except ValueError as e:
        print(e)

def test_valid_inputs(valid_inputs):
    assert valid_inputs.galaxy == 'exampleGalaxy'
    assert valid_inputs.name == 'exampleClient'
    assert valid_inputs.api_server == 'https://galaxy.ansible.com'

def test_edge_cases(edge_cases):
    assert edge_cases.galaxy is None
    assert edge_cases.name is None
    assert edge_cases.api_server is None

def test_invalid_inputs():
    with pytest.raises(ValueError) as excinfo:
        GalaxyAPI('exampleGalaxy', '', 'https://galaxy.ansible.com')
    assert "Invalid input" in str(excinfo.value)
