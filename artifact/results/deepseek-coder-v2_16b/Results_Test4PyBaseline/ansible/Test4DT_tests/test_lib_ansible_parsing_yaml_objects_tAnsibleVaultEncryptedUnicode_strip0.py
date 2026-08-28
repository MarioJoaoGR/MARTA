
# Module: ansible.parsing.yaml.objects
# test_ansible_vault_encrypted_unicode.py
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
import pytest

@pytest.fixture
def vault():
    # Create a mock Vault object for testing
    class MockVault:
        def decrypt(self, ciphertext):
            return b'decrypted_data'  # Replace with actual decryption logic if needed

    return MockVault()

@pytest.fixture
def encrypted_unicode(vault):
    # Create an instance of AnsibleVaultEncryptedUnicode for testing
    ciphertext = b'encrypted_data'
    vault_obj = AnsibleVaultEncryptedUnicode(ciphertext)
    vault_obj.vault = vault  # Set the Vault object for decryption
    return vault_obj

def test_init():
    """Test initialization of AnsibleVaultEncryptedUnicode"""
    ciphertext = b'encrypted_data'
    ansible_vault_obj = AnsibleVaultEncryptedUnicode(ciphertext)
    assert hasattr(ansible_vault_obj, 'vault')
    assert isinstance(ansible_vault_obj._ciphertext, bytes)
    assert ansible_vault_obj._ciphertext == b'encrypted_data'

def test_strip(encrypted_unicode):
    """Test the strip method of AnsibleVaultEncryptedUnicode"""
    # Assuming self.data is already decrypted in the actual implementation
    encrypted_unicode.data = b'  stripped data   '
    assert encrypted_unicode.strip() == b'stripped data'
    assert encrypted_unicode.strip(chars=b' ') == b'stripped data'

def test_decrypt_on_access(encrypted_unicode):
    """Test that the ciphertext is decrypted when accessing .data"""
    # Create a mock Vault object for testing
    class MockVault:
        def decrypt(self, ciphertext):
            return b'decrypted_data'  # Replace with actual decryption logic if needed

    vault = MockVault()
    ciphertext = b'encrypted_data'
    ansible_vault_obj = AnsibleVaultEncryptedUnicode(ciphertext)
    ansible_vault_obj.vault = vault  # Set the Vault object for decryption
    
    with pytest.raises(AttributeError):
        assert ansible_vault_obj.data  # Accessing .data should trigger decryption
