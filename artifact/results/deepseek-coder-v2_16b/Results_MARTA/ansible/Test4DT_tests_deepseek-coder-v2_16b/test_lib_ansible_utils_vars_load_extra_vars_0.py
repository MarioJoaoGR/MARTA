
import pytest
from ansible.utils.vars import load_extra_vars
from ansible.errors import AnsibleOptionsError
from ansible.parsing.dataloader import DataLoader

# Scenario 1: Test standard input with valid YAML and JSON files
def test_valid_input_happy_path():
    loader = DataLoader()
    context = {
        'CLIARGS': {'extra_vars': ['@/path/to/valid.yaml', '@/path/to/valid.json']}
    }
    with pytest.raises(AnsibleOptionsError):
        load_extra_vars(loader)

# Scenario 2: Test handling invalid format by providing string without '@'
def test_invalid_format():
    loader = DataLoader()
    context = {
        'CLIARGS': {'extra_vars': ['invalid_string']}
    }
    with pytest.raises(AnsibleOptionsError):
        load_extra_vars(loader)

# Scenario 3: Test missing lines to cover in the function implementation
def test_missing_lines_to_cover():
    loader = DataLoader()
    context = {
        'CLIARGS': {'extra_vars': []}
    }
    with pytest.raises(AnsibleOptionsError):
        load_extra_vars(loader)
