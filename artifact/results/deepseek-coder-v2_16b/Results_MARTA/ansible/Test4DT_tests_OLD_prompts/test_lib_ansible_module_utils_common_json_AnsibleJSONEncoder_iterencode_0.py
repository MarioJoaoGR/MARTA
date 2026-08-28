
import json
from ansible.module_utils.common.json import AnsibleJSONEncoder
import pytest
from unittest.mock import patch, MagicMock

# Test default configuration without preprocessing or vault conversion

# Test preprocessing unsafe data during encoding
def test_preprocess_unsafe():
    encoder = AnsibleJSONEncoder(preprocess_unsafe=True)
    sample_data = {
        'key': 'value',
        'unsafe': "This might be considered unsafe."
    }
    with patch('json.dumps') as mock_dumps:
        json.dumps(sample_data, cls=encoder, indent=4)
        assert encoder._preprocess_unsafe
        mock_dumps.assert_called_once_with(sample_data, cls=encoder, indent=4)

# Test conversion of vault-protected data to plain text during encoding
def test_vault_to_text():
    encoder = AnsibleJSONEncoder(vault_to_text=True)
    sample_data = {
        'key': 'value',
        'encrypted': {'__ENCRYPTED__': True, '__CIPHERTEXT__': b'vaulted data'}
    }
    with patch('json.dumps') as mock_dumps:
        json.dumps(sample_data, cls=encoder, indent=4)
        assert encoder._vault_to_text
        mock_dumps.assert_called_once_with(sample_data, cls=encoder, indent=4)

# Test both preprocessing unsafe data and converting vault-protected data to plain text during encoding
def test_both_preprocess_and_vault():
    encoder = AnsibleJSONEncoder(preprocess_unsafe=True, vault_to_text=True)
    sample_data = {
        'key': 'value',
        'unsafe': "This might be considered unsafe.",
        'encrypted': {'__ENCRYPTED__': True, '__CIPHERTEXT__': b'vaulted data'}
    }
    with patch('json.dumps') as mock_dumps:
        json.dumps(sample_data, cls=encoder, indent=4)
        assert encoder._preprocess_unsafe
        assert encoder._vault_to_text
        mock_dumps.assert_called_once_with(sample_data, cls=encoder, indent=4)