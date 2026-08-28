
import pytest
from unittest.mock import patch
from ansible.executor.powershell.module_manifest import PSModuleDepFinder, AnsibleError

def test_valid_input():
    finder = PSModuleDepFinder()
    with patch('ansible.executor.powershell.module_manifest._slurp', return_value=b'mocked data'):
        with pytest.raises(AnsibleError) as excinfo:
            finder._add_module('Ansible.ModuleUtils.SomeUtil', '.psm1', 'Ansible.ModuleUtils.SomeUtil', False)
    assert str(excinfo.value) == "Could not find imported module support code for 'Ansible.ModuleUtils.SomeUtil'"
