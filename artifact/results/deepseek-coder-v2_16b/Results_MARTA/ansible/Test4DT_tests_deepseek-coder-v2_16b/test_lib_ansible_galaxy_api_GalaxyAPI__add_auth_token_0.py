
import pytest
from ansible.galaxy.api import GalaxyAPI
from unittest.mock import patch

# Test 1: Valid Input
def test_valid_input():
    # Arrange
    galaxy = 'test_galaxy'
    name = 'test_name'
    url = 'https://test-url.com'
    api_client = GalaxyAPI(galaxy, name, url)
    
    # Act & Assert
    assert api_client.galaxy == galaxy
    assert api_client.name == name
    assert api_client.api_server == url

# Test 2: Missing Token
def test_missing_token():
    # Arrange
    galaxy = 'test_galaxy'
    name = 'test_name'
    url = 'https://test-url.com'
    
    with pytest.raises(Exception) as e:
        GalaxyAPI(galaxy, name, url, required=True)
    
    # Act & Assert
    assert str(e.value) == "No access token or username set. A token can be set with --api-key or at /home/user/.config/ansible/galaxy.yml."

# Test 3: Invalid Input
def test_invalid_input():
    # Arrange & Act
    api_client = GalaxyAPI(None, None, None)
    
    # Assert
    assert api_client is not None
