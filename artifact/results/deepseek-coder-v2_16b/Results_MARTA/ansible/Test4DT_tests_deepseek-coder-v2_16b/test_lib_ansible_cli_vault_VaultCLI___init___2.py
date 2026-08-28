
import pytest
from ansible.cli.vault import VaultCLI

def test_VaultCLI_initialization_with_empty_args():
    # Test initialization of VaultCLI with empty args list
    with pytest.raises(ValueError) as excinfo:
        vault_cli = VaultCLI(args=[])
    assert str(excinfo.value) == 'A non-empty list for args is required'

def test_VaultCLI_initialization_with_non_empty_args():
    # Test initialization of VaultCLI with a non-empty args list
    vault_cli = VaultCLI(args=['--some-arg', 'value'])
    assert isinstance(vault_cli, VaultCLI)
