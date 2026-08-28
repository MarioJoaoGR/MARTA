
import pytest
from ansible.parsing.ajson import AnsibleJSONDecoder

# Example JSON string with vault-encrypted data
json_str = '{"username": "user", "password": "$ANSIBLE_VAULT;1.1;AES256;EncryptedData"}'

def test_ansible_json_decoder():
    decoder = AnsibleJSONDecoder()
    decoded_data = decoder.decode(json_str)
    
    # Assert that the password field is not decrypted in the output
    assert 'password' in decoded_data
    assert decoded_data['password'] == '$ANSIBLE_VAULT;1.1;AES256;EncryptedData'

# Test case for handling vault-encrypted data correctly
def test_ansible_json_decoder_with_vault():
    decoder = AnsibleJSONDecoder()
    decoder._vaults['default'] = 'some_vault_secret'  # Mocking the vault secret
    
    decoded_data = decoder.decode(json_str)
    
    # Assert that the password field is decrypted in the output
    assert 'password' in decoded_data
    assert decoded_data['password'] != '$ANSIBLE_VAULT;1.1;AES256;EncryptedData'  # This should be different after decryption

# Test case for handling unsafe content correctly
def test_ansible_json_decoder_with_unsafe():
    decoder = AnsibleJSONDecoder()
    
    json_str_unsafe = '{"username": "user", "password": "$ANSIBLE_VAULT;1.1;AES256;EncryptedData", "__ansible_unsafe": "sensitive_info"}'
    decoded_data = decoder.decode(json_str_unsafe)
    
    # Assert that the unsafe content is wrapped correctly
    assert '__ansible_unsafe' in decoded_data
    assert decoded_data['__ansible_unsafe'] == 'sensitive_info'  # This should be wrapped as expected

# Test case for handling multiple key-value pairs correctly
def test_ansible_json_decoder_multiple_pairs():
    decoder = AnsibleJSONDecoder()
    
    json_str_multi = '{"username": "user", "password": "$ANSIBLE_VAULT;1.1;AES256;EncryptedData", "__ansible_unsafe": "sensitive_info", "__ansible_vault": "some_vault"}'
    decoded_data = decoder.decode(json_str_multi)
    
    # Assert that all keys are processed correctly
    assert 'username' in decoded_data
    assert 'password' in decoded_data
    assert '__ansible_unsafe' in decoded_data
    assert '__ansible_vault' in decoded_data
