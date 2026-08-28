
import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode


def test_vaultsecret_with_initial_data():
    ciphertext = b'some_encrypted_data'
    vault_secret = AnsibleVaultEncryptedUnicode(ciphertext=ciphertext)
    assert hasattr(vault_secret, 'vault'), "Vault attribute not set"
    assert vault_secret._ciphertext == ciphertext, "Ciphertext data should match the provided value"