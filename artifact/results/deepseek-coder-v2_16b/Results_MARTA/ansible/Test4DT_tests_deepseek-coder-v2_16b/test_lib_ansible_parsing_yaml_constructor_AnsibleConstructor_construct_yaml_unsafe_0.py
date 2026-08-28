
import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.vault import VaultLib

# Test default initialization without file name or vault secrets
def test_default_initialization():
    constructor = AnsibleConstructor()
    assert constructor._ansible_file_name is None
    assert constructor.vault_secrets == []
    assert 'default' in constructor._vaults
    assert isinstance(constructor._vaults['default'], VaultLib)

# Test initialization with a file name and vault secrets
def test_initialization_with_file_and_vaults():
    constructor = AnsibleConstructor(file_name="ansible.cfg", vault_secrets=["secret1", "secret2"])
    assert constructor._ansible_file_name == "ansible.cfg"
    assert constructor.vault_secrets == ["secret1", "secret2"]
    assert 'default' in constructor._vaults
    assert isinstance(constructor._vaults['default'], VaultLib)

# Test initialization without file name or vault secrets