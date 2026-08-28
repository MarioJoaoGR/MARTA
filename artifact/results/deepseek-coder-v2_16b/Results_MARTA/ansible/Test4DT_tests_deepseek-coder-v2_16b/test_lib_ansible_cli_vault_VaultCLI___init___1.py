
import pytest
from ansible.cli.vault import VaultCLI

def test_init_with_valid_args():
    # Test initialization with valid command-line arguments
    args = ['--some-arg', 'value']
    vault_cli = VaultCLI(args=args)
    assert isinstance(vault_cli, VaultCLI), "Initialization should create an instance of VaultCLI"

def test_init_with_none_args():
    # Test initialization with None arguments
    with pytest.raises(ValueError):
        VaultCLI(args=None)

def test_init_with_empty_list_args():
    # Test initialization with an empty list of arguments
    with pytest.raises(ValueError):
        VaultCLI(args=[])
