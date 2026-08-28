
import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

# Test initialization with ciphertext string in Python 2

# Test initialization with ciphertext byte string in Python 3

# Test the isdecimal method in Python 2
def test_isdecimal_in_python2():
    encrypted_data = "12345"  # Example string with decimal digits (Python 2)
    ansible_vault_obj = AnsibleVaultEncryptedUnicode(encrypted_data)
    assert ansible_vault_obj.isdecimal() is True

# Test the isdecimal method in Python 3
def test_isdecimal_in_python3():
    encrypted_data = b"12345"  # Example bytes with decimal digits (Python 3)
    ansible_vault_obj = AnsibleVaultEncryptedUnicode(encrypted_data)
    assert ansible_vault_obj.isdecimal() is True