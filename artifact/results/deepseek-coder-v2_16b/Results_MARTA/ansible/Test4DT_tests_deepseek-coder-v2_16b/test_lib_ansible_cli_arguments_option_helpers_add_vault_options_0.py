
import argparse
import pytest
from ansible.cli.arguments.option_helpers import add_vault_options


def test_with_vault_id():
    parser = argparse.ArgumentParser()
    add_vault_options(parser)
    
    args = parser.parse_args(['--vault-id', 'id1'])
    assert hasattr(args, 'vault_ids')
    assert args.vault_ids == ['id1']

def test_with_ask_vault_password():
    parser = argparse.ArgumentParser()
    add_vault_options(parser)
    
    args = parser.parse_args(['--ask-vault-password'])
    assert hasattr(args, 'ask_vault_pass')
    assert args.ask_vault_pass == True
