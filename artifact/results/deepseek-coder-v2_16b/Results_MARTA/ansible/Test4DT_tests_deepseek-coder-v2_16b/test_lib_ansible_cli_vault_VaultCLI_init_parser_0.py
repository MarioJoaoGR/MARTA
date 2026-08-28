
import pytest
from ansible.cli.vault import VaultCLI

def test_valid_inputs():
    # Test that a valid instance of VaultCLI can be created with non-empty args
    vault_cli = VaultCLI(args=['--some-arg', 'value'])
    assert isinstance(vault_cli, VaultCLI)


