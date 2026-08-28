
import pytest
from ansible.executor.powershell.module_manifest import _slurp
import os
from ansible.errors import AnsibleError


def test_invalid_input():
    invalid_path = '/path/to/nonexistent_file.txt'
    with pytest.raises(AnsibleError):
        _slurp(invalid_path)