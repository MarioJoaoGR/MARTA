
import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

# Test rpartition with a simple separator
def test_rpartition_simple():
    ciphertext = "hello world"
    vault_obj = None  # Assuming Vault object is set by calling code
    ansible_vault_obj = AnsibleVaultEncryptedUnicode(ciphertext)
    result = ansible_vault_obj.rpartition(' ')
    assert result == ('hello', ' ', 'world')

# Test rpartition with a separator not in the string
def test_rpartition_no_separator():
    ciphertext = "helloworld"
    vault_obj = None  # Assuming Vault object is set by calling code
    ansible_vault_obj = AnsibleVaultEncryptedUnicode(ciphertext)
    result = ansible_vault_obj.rpartition(' ')