# Module: ansible.module_utils.common.collections
import pytest
from ansible.module_utils.common.collections import is_string

# Test cases for the is_string function
def test_is_string_standard_str():
    assert is_string("Hello, World!") == True  # Standard string should return True

def test_is_string_bytes():
    assert is_string(b"Hello, World!") == True  # Bytes object should return True

def test_is_string_list():
    assert is_string([1, 2, 3]) == False  # List should return False

def test_is_string_dict():
    assert is_string({"key": "value"}) == False  # Dictionary should return False

# Additional test cases to cover edge cases and potential failures
def test_is_string_none():
    assert is_string(None) == False  # None should return False

def test_is_string_int():
    assert is_string(123) == False  # Integer should return False

def test_is_string_float():
    assert is_string(123.45) == False  # Float should return False

# Test case for AnsibleVaultEncryptedUnicode (assuming it behaves like a string-like object)
def test_is_string_AnsibleVaultEncryptedUnicode():
    class MockVaultObject:
        __ENCRYPTED__ = True
    
    assert is_string(MockVaultObject()) == True  # Mock Vault object should return True if it has the attribute '__ENCRYPTED__'
