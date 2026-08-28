
import pytest
from ansible.cli.vault import VaultCLI

@pytest.fixture(scope="module")
def vault_cli():
    return VaultCLI(args=['--encrypt', '--vault-id=my_vault_id', 'file_to_encrypt.yml'])

def test_valid_inputs(vault_cli):
    assert isinstance(vault_cli, VaultCLI)
    assert vault_cli.args == ['--encrypt', '--vault-id=my_vault_id', 'file_to_encrypt.yml']
    assert vault_cli.b_vault_pass is None
    assert vault_cli.b_new_vault_pass is None
    assert not vault_cli.encrypt_string_read_stdin
    assert vault_cli.encrypt_secret is None
    assert vault_cli.encrypt_vault_id == 'my_vault_id'
    assert vault_cli.new_encrypt_secret is None
    assert vault_cli.new_encrypt_vault_id is None

def test_edge_cases(capsys):
    with pytest.raises(SystemExit) as e:
        VaultCLI(args=[])
    captured = capsys.readouterr()
    assert "usage" in captured.err
    assert isinstance(e.value, SystemExit)
    assert e.value.code == 2

def test_invalid_inputs():
    with pytest.raises(SystemExit) as e:
        VaultCLI(args=['--invalid-arg'])
    assert "usage" in str(e.value)
    assert isinstance(e.value, SystemExit)
    assert e.value.code == 2
