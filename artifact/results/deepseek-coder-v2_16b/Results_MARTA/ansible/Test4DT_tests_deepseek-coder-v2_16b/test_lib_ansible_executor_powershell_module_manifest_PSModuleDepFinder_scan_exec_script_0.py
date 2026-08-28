
import pytest
from ansible.executor.powershell.module_manifest import PSModuleDepFinder

@pytest.fixture(scope="function")
def finder():
    return PSModuleDepFinder()

def test_valid_input(finder):
    script_content = """
    #Requires -Module Ansible.ModuleUtils.SomeUtility
    #AnsibleRequires -PowerShell Ansible.ModuleUtils.AnotherUtility
    """
    with pytest.raises(AttributeError):
        finder._parse_scripts(script_content)

def test_edge_case(finder):
    script_content = """
    #Requires -Module Ansible.ModuleUtils.SomeUtility
    #AnsibleRequires -PowerShell Ansible.ModuleUtils.AnotherUtility
    """
    with pytest.raises(AttributeError):
        finder._parse_scripts(script_content)

def test_invalid_input(finder):
    script_content = """
    InvalidContent -Requires Module Ansible.ModuleUtils.SomeUtility
    #AnsibleRequires -PowerShell Ansible.ModuleUtils.AnotherUtility
    """
    with pytest.raises(AttributeError):
        finder._parse_scripts(script_content)
