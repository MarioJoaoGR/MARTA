
import pytest
from ansible.cli.vault import VaultCLI

def test_valid_input():
    # Test that VaultCLI can be instantiated with a non-empty list of arguments
    vault_cli = VaultCLI(args=['--some-arg', 'value'])
    assert isinstance(vault_cli, VaultCLI), "VaultCLI instance should be created successfully"

def test_invalid_input():
    # Test that VaultCLI raises an error when instantiated with an empty list of arguments
    with pytest.raises(ValueError) as excinfo:
        VaultCLI(args=[])
    assert str(excinfo.value) == 'A non-empty list for args is required', "Expected ValueError"
