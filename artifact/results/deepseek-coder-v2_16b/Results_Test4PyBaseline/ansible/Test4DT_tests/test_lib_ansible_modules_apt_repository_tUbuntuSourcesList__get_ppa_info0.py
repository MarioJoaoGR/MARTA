# Module: ansible.modules.apt_repository
import pytest
from unittest.mock import patch, MagicMock
import ansible.module_utils.basic as basic
from ubuntu_sources_list import UbuntuSourcesList
import distro  # Assuming this is available in your environment
import json

# Mock the necessary functions and classes for testing
@patch('ubuntu_sources_list._get_ppa_info')
@patch('ansible.module_utils.basic.fetch_url')
def test_UbuntuSourcesList_init(mock_fetch_url, mock_get_ppa_info):
    # Mock the fetch_url return value
    mock_fetch_url.return_value = (MagicMock(), {'status': 200})
    
    # Mock the get_ppa_info return value
    mock_get_ppa_info.return_value = {}

    # Create a mock AnsibleModule object with necessary parameters
    module = type('AnsibleModule', (), {'params': {}})()

    # Define a callback function to handle adding PPA signing keys
    def add_ppa_signing_keys(owner, ppa):
        pass  # Your code to add PPA signing keys here

    # Initialize the UbuntuSourcesList class with the module and callback function
    ubuntu_sources = UbuntuSourcesList(module, add_ppa_signing_keys)
    
    assert ubuntu_sources.module == module
    assert ubuntu_sources.add_ppa_signing_keys_callback == add_ppa_signing_keys
    assert isinstance(ubuntu_sources.codename, str)

# Test _get_ppa_info method
@patch('ansible.module_utils.basic.fetch_url')
def test_UbuntuSourcesList__get_ppa_info(mock_fetch_url):
    # Mock the fetch_url return value for a successful request
    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps({})
    mock_fetch_url.return_value = (mock_response, {'status': 200})

    # Create a mock UbuntuSourcesList instance with a module object
    ubuntu_sources = UbuntuSourcesList(type('AnsibleModule', (), {'params': {}})())
    
    # Call the _get_ppa_info method
    owner_name = 'owner'
    ppa_name = 'ppa'
    ppa_info = ubuntu_sources._get_ppa_info(owner_name, ppa_name)
    
    assert isinstance(ppa_info, dict)
    mock_fetch_url.assert_called_with(ubuntu_sources.module, f"https://launchpad.net/api/1.0/~{owner_name}/+archive/{ppa_name}", headers={'Accept': 'application/json'})

# Test _get_ppa_info method with a failed request
@patch('ansible.module_utils.basic.fetch_url')
def test_UbuntuSourcesList__get_ppa_info_failure(mock_fetch_url):
    # Mock the fetch_url return value for a failed request
    mock_fetch_url.return_value = (MagicMock(), {'status': 404})

    # Create a mock UbuntuSourcesList instance with a module object
    ubuntu_sources = UbuntuSourcesList(type('AnsibleModule', (), {'params': {}})())
    
    # Call the _get_ppa_info method and expect it to fail
    owner_name = 'owner'
    ppa_name = 'ppa'
    with pytest.raises(SystemExit):
        ubuntu_sources._get_ppa_info(owner_name, ppa_name)
    
    mock_fetch_url.assert_called_with(ubuntu_sources.module, f"https://launchpad.net/api/1.0/~{owner_name}/+archive/{ppa_name}", headers={'Accept': 'application/json'})
