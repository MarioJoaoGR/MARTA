# Module: ansible.module_utils.common.json
import pytest
from ansible.module_utils.common.json import _is_vault

class VaultObject:
    __ENCRYPTED__ = True

def test_is_vault_with_encrypted_attribute():
    vault_object = VaultObject()
    assert _is_vault(vault_object) is True, "Expected _is_vault to return True for an object with __ENCRYPTED__ attribute set to True"

def test_is_vault_without_encrypted_attribute():
    dictionary = {'key': 'value'}
    assert _is_vault(dictionary) is False, "Expected _is_vault to return False for a dictionary without the __ENCRYPTED__ attribute"

def test_is_vault_with_false_encrypted_attribute():
    vault_object = VaultObject()
    vault_object.__ENCRYPTED__ = False
    assert _is_vault(vault_object) is False, "Expected _is_vault to return False for an object with __ENCRYPTED__ attribute set to False"

def test_is_vault_with_missing_attribute():
    value = type('Dummy', (), {})()  # Create a class instance without the __ENCRYPTED__ attribute
    assert _is_vault(value) is False, "Expected _is_vault to return False for an object without the __ENCRYPTED__ attribute"
