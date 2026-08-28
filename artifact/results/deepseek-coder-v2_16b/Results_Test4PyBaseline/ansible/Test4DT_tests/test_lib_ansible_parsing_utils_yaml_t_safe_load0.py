# Module: ansible.parsing.utils.yaml
import pytest
from ansible.parsing.utils.yaml import _safe_load
import yaml

# Test cases for _safe_load function

def test_load_local_yaml_file():
    with open('example.yaml', 'r') as f:
        data = _safe_load(f)
    assert isinstance(data, dict), "Expected a dictionary but got something else."

def test_load_string_containing_yaml():
    yaml_content = "key: value"
    data = _safe_load(yaml_content)
    assert data == {'key': 'value'}, f"Expected {{'key': 'value'}} but got {data}"

def test_load_encrypted_yaml_with_vault_secrets():
    encrypted_yaml = "!vault | $encrypted_value"
    vault_secrets = {"encrypted_value": "decrypted_password"}
    data = _safe_load(encrypted_yaml, vault_secrets=vault_secrets)
    assert data == {'key': 'value'}, f"Expected {{'key': 'value'}} but got {data}"

# Additional test cases for edge cases and potential failures
def test_load_invalid_yaml():
    invalid_yaml = "not yaml content"
    with pytest.raises(yaml.parser.ParserError):
        _safe_load(invalid_yaml)

def test_load_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        with open('nonexistent.yaml', 'r') as f:
            _safe_load(f)

def test_load_empty_string():
    empty_string = ""
    with pytest.raises(yaml.scanner.ScannerError):
        _safe_load(empty_string)
