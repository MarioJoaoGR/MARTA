
import pytest
from ansible.playbook.role.requirement import RoleRequirement
from ansible.errors import AnsibleError


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_role_requirement_RoleRequirement_role_yaml_parse_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_role_dict _____________________________

    def test_valid_role_dict():
        role = {'src': 'galaxy.example,1.0'}
        parsed_role = RoleRequirement.role_yaml_parse(role)
        assert isinstance(parsed_role, dict), "Parsed role should be a dictionary"
        assert 'name' in parsed_role, "Dictionary should contain the name key"
>       assert parsed_role['name'] == 'galaxy.example', "Name should be 'galaxy.example'"
E       AssertionError: Name should be 'galaxy.example'
E       assert 'galaxy.example,1.0' == 'galaxy.example'
E         
E         - galaxy.example
E         + galaxy.example,1.0
E         ?               ++++

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_role_requirement_RoleRequirement_role_yaml_parse_1.py:11: AssertionError
___________________________ test_invalid_role_string ___________________________

    def test_invalid_role_string():
>       with pytest.raises(AnsibleError):
E       Failed: DID NOT RAISE <class 'ansible.errors.AnsibleError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_role_requirement_RoleRequirement_role_yaml_parse_1.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_role_requirement_RoleRequirement_role_yaml_parse_1.py::test_valid_role_dict
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_role_requirement_RoleRequirement_role_yaml_parse_1.py::test_invalid_role_string
============================== 2 failed in 0.83s ===============================
"""