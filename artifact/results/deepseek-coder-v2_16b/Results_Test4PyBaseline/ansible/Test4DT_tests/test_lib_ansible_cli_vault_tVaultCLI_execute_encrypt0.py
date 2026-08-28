
import pytest
from ansible.cli.vault import VaultCLI

@pytest.fixture
def vault_cli():
    return VaultCLI(['-e', '@file.yml'])

def test_init(vault_cli):
    assert isinstance(vault_cli, VaultCLI)
    assert vault_cli.b_vault_pass is None
    assert vault_cli.b_new_vault_pass is None
    assert not vault_cli.encrypt_string_read_stdin
    assert vault_cli.encrypt_secret is None
    assert vault_cli.encrypt_vault_id is None
    assert vault_cli.new_encrypt_secret is None