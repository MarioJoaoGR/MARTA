
import pytest
from ansible.playbook.role.requirement import RoleRequirement



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_role_requirement_RoleRequirement___init___0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_repo_url_to_role_name __________________________

    def test_repo_url_to_role_name():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_role_requirement_RoleRequirement___init___0.py:6: Failed
________________________ test_role_yaml_parse_old_style ________________________

    def test_role_yaml_parse_old_style():
        role = "example/role-name:1.0"  # Old style specification
        parsed_role = RoleRequirement.role_yaml_parse(role)
>       assert parsed_role == {'name': 'role-name', 'src': 'example/role-name', 'version': '1.0'}
E       AssertionError: assert {'name': 'exa...ersion': None} == {'name': 'rol...rsion': '1.0'}
E         
E         Differing items:
E         {'version': None} != {'version': '1.0'}
E         {'name': 'example/role-name:1.0'} != {'name': 'role-name'}
E         {'src': 'example/role-name:1.0'} != {'src': 'example/role-name'}
E         Left contains 1 more item:
E         {'scm': None}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_role_requirement_RoleRequirement___init___0.py:12: AssertionError
________________________ test_role_yaml_parse_new_style ________________________

    def test_role_yaml_parse_new_style():
        role = {"name": "role-name", "src": "https://github.com/example/role-name.git", "version": "1.0"}  # New style specification
        parsed_role = RoleRequirement.role_yaml_parse(role)
>       assert parsed_role == {'name': 'role-name', 'src': 'https://github.com/example/role-name.git', 'version': '1.0'}
E       AssertionError: assert {'name': 'rol...rsion': '1.0'} == {'name': 'rol...rsion': '1.0'}
E         
E         Omitting 3 identical items, use -vv to show
E         Left contains 1 more item:
E         {'scm': 'git'}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_role_requirement_RoleRequirement___init___0.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_role_requirement_RoleRequirement___init___0.py::test_repo_url_to_role_name
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_role_requirement_RoleRequirement___init___0.py::test_role_yaml_parse_old_style
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_role_requirement_RoleRequirement___init___0.py::test_role_yaml_parse_new_style
============================== 3 failed in 0.43s ===============================
"""