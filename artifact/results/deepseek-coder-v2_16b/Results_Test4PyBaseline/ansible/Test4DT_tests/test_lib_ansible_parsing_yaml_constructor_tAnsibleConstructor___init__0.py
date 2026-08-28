# Module: ansible.parsing.yaml.constructor
import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor

# Test default initialization of AnsibleConstructor
def test_default_initialization():
    constructor = AnsibleConstructor()
    assert hasattr(constructor, '_ansible_file_name') is False
    assert isinstance(constructor.vault_secrets, list) and not constructor.vault_secrets
    assert 'default' in constructor._vaults
    assert isinstance(constructor._vaults['default'], VaultLib)

# Test initialization with vault secrets
def test_initialization_with_vault_secrets():
    constructor = AnsibleConstructor(vault_secrets=['secret1', 'secret2'])
    assert hasattr(constructor, '_ansible_file_name') is False
    assert isinstance(constructor.vault_secrets, list) and constructor.vault_secrets == ['secret1', 'secret2']
    assert 'default' in constructor._vaults
    assert isinstance(constructor._vaults['default'], VaultLib)
    assert constructor._vaults['default'].secrets == ['secret1', 'secret2']

# Test initialization with a specific file name (not used, should be ignored)
def test_initialization_with_specific_file_name():
    constructor = AnsibleConstructor(file_name='specific_config_file.yml')
    assert hasattr(constructor, '_ansible_file_name') is False
    assert isinstance(constructor.vault_secrets, list) and not constructor.vault_secrets
    assert 'default' in constructor._vaults
    assert isinstance(constructor._vaults['default'], VaultLib)
