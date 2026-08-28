
import pytest
from ansible.cli.vault import VaultCLI
import sys
import io

def test_valid_input_happy_path():
    vault_cli = VaultCLI(args=['--some-arg', 'value'])
    vault_cli.encrypt_secret = "my_secret"
    captured_output = io.StringIO()
    sys.stdout = captured_output
    vault_cli.execute_encrypt_string()
    sys.stdout = sys.__stdout__
    assert "Encrypted string:" in captured_output.getvalue()

def test_edge_case_none_input():
    vault_cli = VaultCLI(args=[])
    vault_cli.encrypt_string_read_stdin = True
    captured_output = io.StringIO()
    sys.stdout = captured_output
    with pytest.raises(SystemExit) as e:
        vault_cli.execute_encrypt_string()
    assert "stdin was empty, not encrypting" in str(e.value)
    sys.stdout = sys.__stdout__

def test_invalid_input_error_handling():
    vault_cli = VaultCLI(args=['--some-arg', ''])
    captured_output = io.StringIO()
    sys.stdout = captured_output
    with pytest.raises(SystemExit) as e:
        vault_cli.execute_encrypt_string()
    assert "The plaintext provided from the command line args was empty, not encrypting" in str(e.value)
    sys.stdout = sys.__stdout__
