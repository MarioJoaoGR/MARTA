
import os
from unittest.mock import patch, MagicMock
import pytest
from ansible.errors import AnsibleError
from ansible.executor.powershell.module_manifest import _slurp


def test_invalid_input():
    with patch('os.path.exists', return_value=False):
        with pytest.raises(AnsibleError) as excinfo:
            _slurp('/path/to/file.txt')
        assert str(excinfo.value) == "imported module support code does not exist at /path/to/file.txt"