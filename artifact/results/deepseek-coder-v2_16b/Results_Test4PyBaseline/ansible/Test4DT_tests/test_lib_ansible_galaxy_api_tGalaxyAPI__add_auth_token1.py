
import pytest
from ansible.galaxy.api import GalaxyAPI
from ansible.errors import AnsibleError

# Test adding an authorization header when one is already present
def test_add_auth_token_header_already_present():
    api_client = GalaxyAPI(galaxy='main', name='ansible-api', url='https://galaxy.ansible.com')
    headers = {'Authorization': 'Bearer old_token'}
    api_client._add_auth_token(headers, 'http://example.com')
    assert 'Authorization' in headers
    assert headers['Authorization'] == 'Bearer old_token'

# Test raising an error when no token is provided and it is required
def test_raise_error_when_no_token_provided():
    api_client = GalaxyAPI(galaxy='main', name='ansible-api', url='https://galaxy.ansible.com')
    headers = {}
    with pytest.raises(AnsibleError) as excinfo:
        api_client._add_auth_token(headers, 'http://example.com', required=True)