# Module: ansible.parsing.ajson
import json
from ansible_vault import AnsibleJSONDecoder
import pytest

# Example JSON string with vault-encrypted data
json_str = '{"username": "user", "password": "$ANSIBLE_VAULT;1.1;AES256;EncryptedData"}'

def test_basic_usage():
    decoder = AnsibleJSONDecoder()
    decoded_data = decoder.decode(json_str)
    assert 'username' in decoded_data
    assert decoded_data['username'] == 'user'
    # The password should be encrypted and not decrypted here, so it should not be present in the output
    assert 'password' not in decoded_data

def test_with_specific_vault_configuration():
    secrets = {'password': 'secret'}
    AnsibleJSONDecoder.set_secrets(secrets)
    decoder = AnsibleJSONDecoder()
    decoded_data = decoder.decode(json_str)
    assert 'username' in decoded_data
    assert decoded_data['username'] == 'user'
    # The password should be decrypted using the specific vault configuration
    assert decoded_data['password'] == 'secret'

def test_with_custom_vaults():
    secrets = {
        'vault1': {'password': 'secret1'},
        'vault2': {'password': 'secret2'}
    }
    AnsibleJSONDecoder.set_secrets(secrets)
    decoder = AnsibleJSONDecoder()
    # Example JSON string with vault-encrypted data for a specific vault
    json_str_custom = '{"username": "user", "password": "$ANSIBLE_VAULT;vault1;AES256;EncryptedData"}'
    decoded_data = decoder.decode(json_str_custom)
    assert 'username' in decoded_data
    assert decoded_data['username'] == 'user'
    # The password should be decrypted using the specified vault
    assert decoded_data['password'] == 'secret1'

# Additional edge cases can be added to cover more scenarios, such as handling different vault configurations and encrypted data formats.
