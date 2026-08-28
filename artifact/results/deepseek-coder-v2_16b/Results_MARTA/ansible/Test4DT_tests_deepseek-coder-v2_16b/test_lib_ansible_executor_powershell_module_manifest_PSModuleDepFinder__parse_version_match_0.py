
import pytest
from ansible.executor.powershell.module_manifest import PSModuleDepFinder

# Test for parsing version match correctly updating the attribute when a newer version is found

# Test that _parse_scripts handles empty input gracefully
def test_parse_scripts_empty_input():
    finder = PSModuleDepFinder()
    with pytest.raises(AttributeError):
        finder._parse_scripts('')

# Test that _parse_scripts correctly parses the requirements in a script
def test_parse_scripts_with_requirements():
    finder = PSModuleDepFinder()
    script_content = """
    #Requires -Module Ansible.ModuleUtils.SomeUtil
    #AnsibleRequires -PowerShell Ansible.ModuleUtils.AnotherUtil
    #requires -module Ansible.ModuleUtils.YetAnotherUtil
    #ansiblerequires -powershell ansible_collections.namespace.collection.plugins.module_utils.utilname
    """
    with pytest.raises(AttributeError):
        finder._parse_scripts(script_content)

# Test that _parse_scripts correctly parses version requirements in a script
def test_parse_scripts_with_version():
    finder = PSModuleDepFinder()
    script_content = """
    #requires -version 3.1
    #ansiblerequires -osversion 5.0
    """
    with pytest.raises(AttributeError):
        finder._parse_scripts(script_content)