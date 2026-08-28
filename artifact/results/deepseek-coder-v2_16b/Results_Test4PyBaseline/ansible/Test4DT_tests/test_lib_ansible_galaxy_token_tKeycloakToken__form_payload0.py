
from ansible.galaxy.token import KeycloakToken

def test_minimal_parameters():
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/', validate_certs=True)
    assert token.client_id == 'cloud-services'

def test_all_parameters_provided():
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/', validate_certs=True, client_id='custom_client_id')