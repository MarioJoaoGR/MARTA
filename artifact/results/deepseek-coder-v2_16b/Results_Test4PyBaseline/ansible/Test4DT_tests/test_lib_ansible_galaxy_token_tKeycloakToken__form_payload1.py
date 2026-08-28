
from ansible.galaxy.token import KeycloakToken

def test_form_payload_minimal():
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/', validate_certs=True)
    assert token._form_payload() == 'grant_type=refresh_token&client_id=cloud-services&refresh_token=your_refresh_token'

def test_form_payload_with_custom_client_id():
    token = KeycloakToken(access_token='your_refresh_token', auth_url='https://sso.redhat.com/auth/', validate_certs=True, client_id='custom_client_id')
    assert token._form_payload() == 'grant_type=refresh_token&client_id=custom_client_id&refresh_token=your_refresh_token'
