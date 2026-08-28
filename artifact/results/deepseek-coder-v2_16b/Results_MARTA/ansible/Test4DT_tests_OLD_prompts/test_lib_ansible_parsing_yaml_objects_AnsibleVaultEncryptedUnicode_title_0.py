
import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

def test_init_with_ciphertext():
    ciphertext = b'some_encrypted_data'
    vault_obj = AnsibleVaultEncryptedUnicode(ciphertext)
    assert hasattr(vault_obj, 'vault'), "Expected 'vault' attribute to be set"
    assert vault_obj._ciphertext == ciphertext, "Expected _ciphertext to match the provided ciphertext"
