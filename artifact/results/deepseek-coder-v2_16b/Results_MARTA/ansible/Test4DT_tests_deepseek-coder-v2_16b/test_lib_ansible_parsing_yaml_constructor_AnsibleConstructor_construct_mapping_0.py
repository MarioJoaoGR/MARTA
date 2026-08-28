
import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor
from ansible.parsing.vault import VaultLib

def test_init_with_file_name_and_vault_secrets():
    constructor = AnsibleConstructor(file_name="ansible.cfg", vault_secrets=["secret1", "secret2"])
    assert constructor._ansible_file_name == "ansible.cfg"
    assert len(constructor._vaults) == 1
    assert "default" in constructor._vaults
    assert isinstance(constructor._vaults["default"], VaultLib)


