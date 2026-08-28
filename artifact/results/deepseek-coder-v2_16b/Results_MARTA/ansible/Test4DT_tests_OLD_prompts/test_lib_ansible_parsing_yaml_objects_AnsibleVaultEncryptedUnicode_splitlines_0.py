
import pytest
from unittest.mock import patch, MagicMock
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode


def test_vault_encrypted_file_path():
    encrypted_file_path = 'path/to/your/encrypted_file.enc'  # Replace with actual file path
    with patch('builtins.open', side_effect=FileNotFoundError("No such file or directory")):
        with pytest.raises(FileNotFoundError):
            with open(encrypted_file_path, 'rb') as f:
                encrypted_data = f.read()
                ansible_vault_obj = AnsibleVaultEncryptedUnicode(encrypted_data)