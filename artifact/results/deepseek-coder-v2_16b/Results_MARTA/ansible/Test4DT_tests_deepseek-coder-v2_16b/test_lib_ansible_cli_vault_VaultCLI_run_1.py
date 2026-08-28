
import pytest
from ansible.cli.vault import VaultCLI
from unittest.mock import patch

def test_valid_inputs_happy_path():
    vault_cli = VaultCLI(args=['--action', 'encrypt', '--vault-id', 'my_vault_id', '-e', '@file.yml'])
    
    with patch('sys.stdout', new=[]):  # Redirect stdout to an empty list to avoid printing help message
        with pytest.raises(SystemExit) as excinfo:
            vault_cli.run()
        
        assert excinfo.value.code == 2  # Check if the SystemExit code is 2, indicating a parsing error
