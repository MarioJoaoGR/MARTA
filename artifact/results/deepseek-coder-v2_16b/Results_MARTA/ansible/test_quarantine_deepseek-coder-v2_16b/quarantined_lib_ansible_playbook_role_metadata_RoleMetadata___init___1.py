
import pytest
from ansible.playbook.role.metadata import RoleMetadata


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_role_metadata_RoleMetadata___init___1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_default_values ______________________________

    def test_default_values():
        role_meta = RoleMetadata()
        assert hasattr(role_meta, '_allow_duplicates'), "RoleMetadata instance should have a _allow_duplicates attribute"
>       assert role_meta._allow_duplicates == False, "_allow_duplicates should default to False"

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_role_metadata_RoleMetadata___init___1.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.playbook.attribute.FieldAttribute object at 0x7fee5d96caf0>
other = False

    def __eq__(self, other):
>       return other.priority == self.priority
E       AttributeError: 'bool' object has no attribute 'priority'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/attribute.py:98: AttributeError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_role_metadata_RoleMetadata___init___1.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_role_metadata_RoleMetadata___init___1.py::test_default_values
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_role_metadata_RoleMetadata___init___1.py::test_invalid_input
============================== 2 failed in 0.83s ===============================
"""