
import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

# Test rpartition with a valid separator
def test_rpartition_valid_separator():
    ciphertext = "encrypted_data"
    vault_obj = None  # Assuming Vault object is set by calling code
    ansible_vault_obj = AnsibleVaultEncryptedUnicode(ciphertext)
    result = ansible_vault_obj.rpartition('_')
    assert result == ('encrypted', '_', 'data'), f"Expected rpartition to return ('encrypted', '_', 'data'), but got {result}"

# Test rpartition with a separator not in the string
def test_rpartition_no_separator():
    ciphertext = "encrypteddata"
    vault_obj = None  # Assuming Vault object is set by calling code
    ansible_vault_obj = AnsibleVaultEncryptedUnicode(ciphertext)
    result = ansible_vault_obj.rpartition('_')