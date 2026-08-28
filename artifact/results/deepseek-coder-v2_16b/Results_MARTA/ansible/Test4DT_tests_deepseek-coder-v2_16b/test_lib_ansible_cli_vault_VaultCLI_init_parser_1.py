
import pytest
from ansible.cli.vault import VaultCLI

def test_VaultCLI_init_with_empty_args():
    """
    Test that VaultCLI raises a ValueError when initialized with an empty list of args.
    """
    with pytest.raises(ValueError) as excinfo:
        vault_cli = VaultCLI(args=[])  # No args provided
    assert str(excinfo.value) == 'A non-empty list for args is required'

def test_VaultCLI_init_with_valid_args():
    """
    Test that VaultCLI can be initialized with a valid list of args.
    """
    vault_cli = VaultCLI(args=['--some-arg', 'value'])  # Assuming some args are passed to the class constructor.
    assert isinstance(vault_cli, VaultCLI)
