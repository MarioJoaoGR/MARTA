
import pytest
from ansible.parsing.yaml.constructor import AnsibleConstructor

# Test initialization with default settings
def test_default_initialization():
    constructor = AnsibleConstructor()
    assert constructor._ansible_file_name is None
    assert constructor.vault_secrets == []