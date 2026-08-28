
import argparse
from unittest.mock import patch, MagicMock
import pytest

def add_vault_options(parser):
    """Add options for loading vault files"""
    parser.add_argument('--vault-id', default=[], dest='vault_ids', action='append', type=str,
                        help='the vault identity to use')
    base_group = parser.add_mutually_exclusive_group()
    base_group.add_argument('--ask-vault-password', '--ask-vault-pass', default=False, dest='ask_vault_pass', action='store_true',
                            help='ask for vault password')
    base_group.add_argument('--vault-password-file', '--vault-pass-file', default=[], dest='vault_password_files',
                            help="vault password file", type=str, action='append')

# Test scenarios
def test_valid_inputs():
    parser = argparse.ArgumentParser()
    add_vault_options(parser)
    with patch('argparse._sys.argv', ['script_name', '--vault-id', 'id1', '--vault-id', 'id2']):
        args = parser.parse_args()
        assert args.vault_ids == ['id1', 'id2']

def test_edge_cases():
    parser = argparse.ArgumentParser()
    add_vault_options(parser)
    with patch('argparse._sys.argv', ['script_name', '--ask-vault-password']):
        args = parser.parse_args()
        assert args.ask_vault_pass is True
    with patch('argparse._sys.argv', ['script_name', '--vault-password-file', 'passwd.txt']):
        args = parser.parse_args()
        assert args.vault_password_files == ['passwd.txt']

def test_invalid_inputs():
    parser = argparse.ArgumentParser()
    add_vault_options(parser)
    with pytest.raises(SystemExit):
        with patch('argparse._sys.argv', ['script_name', '--invalid-option']):
            parser.parse_args()
