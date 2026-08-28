
import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
import sys
if sys.version_info >= (3, 0):
    from unittest.mock import patch
else:
    from unittest.mock import patch

@pytest.fixture(scope="module")
def vault_encrypted_unicode():
    encrypted_data = b'some_encrypted_data'
    ansible_vault_obj = AnsibleVaultEncryptedUnicode(encrypted_data)
    yield ansible_vault_obj

def test_init_ansible_vault_encrypted_unicode(vault_encrypted_unicode):
    assert vault_encrypted_unicode._ciphertext == b'some_encrypted_data'
    assert vault_encrypted_unicode.vault is None

