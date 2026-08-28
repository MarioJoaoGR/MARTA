
import pytest
from unittest.mock import patch
from ansible.executor.powershell.module_manifest import PSModuleDepFinder



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_powershell_module_manifest_PSModuleDepFinder__parse_version_match_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        finder = PSModuleDepFinder()
        script_content = """
        #Requires -Module Ansible.ModuleUtils.SomeUtil
        #AnsibleRequires -PowerShell Ansible.ModuleUtils.AnotherUtil
        #requires -Version 5.1
        #ansiblerequires -osversion 6.2
        """
        with patch('ansible.executor.powershell.module_manifest.re'):
>           finder._parse_scripts(script_content)
E           AttributeError: 'PSModuleDepFinder' object has no attribute '_parse_scripts'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_powershell_module_manifest_PSModuleDepFinder__parse_version_match_0.py:15: AttributeError
__________________________ test_edge_case_none_values __________________________

    def test_edge_case_none_values():
        finder = PSModuleDepFinder()
        script_content = """
        #Requires -Module Ansible.ModuleUtils.SomeUtil
        #AnsibleRequires -PowerShell Ansible.ModuleUtils.AnotherUtil
        #requires -Version 5.1
        #ansiblerequires -osversion 6.2
        """
        with patch('ansible.executor.powershell.module_manifest.re'):
>           finder._parse_scripts(script_content)
E           AttributeError: 'PSModuleDepFinder' object has no attribute '_parse_scripts'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_powershell_module_manifest_PSModuleDepFinder__parse_version_match_0.py:29: AttributeError
______________________ test_invalid_input_error_handling _______________________

    def test_invalid_input_error_handling():
        finder = PSModuleDepFinder()
        script_content = """
        #Requires -InvalidModule InvalidUtil
        #AnsibleRequires -PowerShell InvalidUtil
        #requires -Version InvalidVersion
        #ansiblerequires -osversion InvalidOSVersion
        """
        with patch('ansible.executor.powershell.module_manifest.re'):
            with pytest.raises(ValueError):
>               finder._parse_scripts(script_content)
E               AttributeError: 'PSModuleDepFinder' object has no attribute '_parse_scripts'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_powershell_module_manifest_PSModuleDepFinder__parse_version_match_0.py:44: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_powershell_module_manifest_PSModuleDepFinder__parse_version_match_0.py::test_valid_input_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_powershell_module_manifest_PSModuleDepFinder__parse_version_match_0.py::test_edge_case_none_values
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_powershell_module_manifest_PSModuleDepFinder__parse_version_match_0.py::test_invalid_input_error_handling
============================== 3 failed in 0.34s ===============================
"""