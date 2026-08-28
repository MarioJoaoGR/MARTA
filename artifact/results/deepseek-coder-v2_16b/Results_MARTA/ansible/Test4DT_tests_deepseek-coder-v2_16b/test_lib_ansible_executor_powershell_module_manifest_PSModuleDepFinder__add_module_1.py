
import pytest
from ansible.executor.powershell.module_manifest import PSModuleDepFinder
from ansible.errors import AnsibleError

def test_add_valid_module():
    finder = PSModuleDepFinder()
    with pytest.raises(AnsibleError):
        finder._add_module('Ansible.ModuleUtils.SomeUtil', '.psm1', 'Ansible.ModuleUtils.SomeUtil', False)

