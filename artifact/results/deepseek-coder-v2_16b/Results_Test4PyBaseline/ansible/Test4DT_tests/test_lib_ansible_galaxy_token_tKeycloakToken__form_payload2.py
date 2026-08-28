
from ansible.galaxy.token import KeycloakToken

def test_minimal_parameters():
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/', validate_certs=True)
    assert token._form_payload() == 'grant_type=refresh_token&client_id=%s&refresh_token=%s' % ('cloud-services', 'your_refresh_token')

def test_all_parameters_provided():
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/', validate_certs=True, client_id='custom_client_id')
    assert token._form_payload() == 'grant_type=refresh_token&client_id=custom_client_id&refresh_token=%s' % ('your_refresh_token')
