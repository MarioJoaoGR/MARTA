
import pytest
from ansible.cli.vault import VaultCLI
from ansible.errors import AnsibleOptionsError

@pytest.fixture
def setup_vaultcli():
    return VaultCLI(['@file.yml'])

def test_init_with_args(setup_vaultcli):
    assert isinstance(setup_vaultcli, VaultCLI)