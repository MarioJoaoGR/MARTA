# Module: ansible.parsing.yaml.constructor
import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor

# Test default initialization of AnsibleConstructor
def test_default_initialization():
    constructor = AnsibleConstructor()
    assert hasattr(constructor, '_ansible_file_name')
    assert constructor._ansible_file_name is None
    assert hasattr(constructor, 'vault_secrets')
    assert isinstance(constructor.vault_secrets, list)
    assert len(constructor.vault_secrets) == 0
    assert hasattr(constructor, '_vaults')
    assert isinstance(constructor._vaults, dict)
    assert 'default' in constructor._vaults
    assert isinstance(constructor._vaults['default'], VaultLib)

# Test initialization with vault secrets
def test_initialization_with_vault_secrets():
    constructor = AnsibleConstructor(vault_secrets=['secret1', 'secret2'])
    assert hasattr(constructor, '_ansible_file_name')
    assert constructor._ansible_file_name is None
    assert hasattr(constructor, 'vault_secrets')
    assert isinstance(constructor.vault_secrets, list)
    assert len(constructor.vault_secrets) == 2
    assert constructor.vault_secrets == ['secret1', 'secret2']
    assert hasattr(constructor, '_vaults')
    assert isinstance(constructor._vaults, dict)
    assert 'default' in constructor._vaults
    assert isinstance(constructor._vaults['default'], VaultLib)
    assert constructor._vaults['default'].secrets == ['secret1', 'secret2']

# Test initialization with file name
def test_initialization_with_file_name():
    constructor = AnsibleConstructor(file_name='config.yml')
    assert hasattr(constructor, '_ansible_file_name')
    assert constructor._ansible_file_name == 'config.yml'
    assert hasattr(constructor, 'vault_secrets')
    assert isinstance(constructor.vault_secrets, list)
    assert len(constructor.vault_secrets) == 0
    assert hasattr(constructor, '_vaults')
    assert isinstance(constructor._vaults, dict)
    assert 'default' in constructor._vaults
    assert isinstance(constructor._vaults['default'], VaultLib)

# Test initialization with both file name and vault secrets
def test_initialization_with_both():
    constructor = AnsibleConstructor(file_name='config.yml', vault_secrets=['secret1', 'secret2'])
    assert hasattr(constructor, '_ansible_file_name')
    assert constructor._ansible_file_name == 'config.yml'
    assert hasattr(constructor, 'vault_secrets')
    assert isinstance(constructor.vault_secrets, list)
    assert len(constructor.vault_secrets) == 2
    assert constructor.vault_secrets == ['secret1', 'secret2']
    assert hasattr(constructor, '_vaults')
    assert isinstance(constructor._vaults, dict)
    assert 'default' in constructor._vaults
    assert isinstance(constructor._vaults['default'], VaultLib)
    assert constructor._vaults['default'].secrets == ['secret1', 'secret2']
