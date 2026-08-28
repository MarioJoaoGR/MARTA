
import pytest
import argparse
from ansible.cli.arguments.option_helpers import add_vault_options

def test_add_vault_options_with_multiple_vault_ids():
    parser = argparse.ArgumentParser()
    add_vault_options(parser)
    args = parser.parse_args(['--vault-id', 'id1', '--vault-id', 'id2'])
    assert hasattr(args, 'vault_ids') and args.vault_ids == ['id1', 'id2']

def test_add_vault_options_with_ask_vault_password():
    parser = argparse.ArgumentParser()
    add_vault_options(parser)
    args = parser.parse_args(['--ask-vault-password'])
    assert hasattr(args, 'ask_vault_pass') and args.ask_vault_pass == True
