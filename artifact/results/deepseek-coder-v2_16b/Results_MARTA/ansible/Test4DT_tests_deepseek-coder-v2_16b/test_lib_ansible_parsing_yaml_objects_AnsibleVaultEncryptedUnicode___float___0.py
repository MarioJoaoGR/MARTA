
import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode


def test_ansible_vault_encrypted_unicode_to_float():
    encrypted_data = b'some_encrypted_data'  # Example encrypted data in bytes
    ansible_vault_obj = AnsibleVaultEncryptedUnicode(encrypted_data)
    vault_obj = None  # Assuming you have an instance of vaultlib ready to use
    ansible_vault_obj.vault = vault_obj
    with pytest.raises(ValueError, match="could not convert string to float: 'some_encrypted_data'"):
        float(ansible_vault_obj)