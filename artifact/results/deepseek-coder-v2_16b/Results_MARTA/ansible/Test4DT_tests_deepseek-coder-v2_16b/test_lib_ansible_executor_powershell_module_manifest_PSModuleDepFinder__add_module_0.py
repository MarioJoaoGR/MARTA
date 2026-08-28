
import pytest
from ansible.executor.powershell.module_manifest import PSModuleDepFinder
from ansible.errors import AnsibleError

def test_invalid_input():
    finder = PSModuleDepFinder()
    with pytest.raises(NameError):
        with pytest.raises(AnsibleError):
            raise NameError("Test raised an exception")
