
import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleParserError


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base_FieldAttributeBase__load_module_defaults_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________________ test_valid_module_defaults __________________________

    def test_valid_module_defaults():
        field_attribute = FieldAttributeBase()
        result = field_attribute._load_module_defaults(name='ping', value={'ping': "{{ ping_defaults }}"})
    
        assert isinstance(result, list), "Expected a list of dictionaries"
        assert len(result) == 1, "Expected one dictionary in the list"
>       assert 'ansible.legacy.ping' in result[0], "Expected fully qualified action name"
E       AssertionError: Expected fully qualified action name
E       assert 'ansible.legacy.ping' in {'ansible.builtin.ping': '{{ ping_defaults }}'}

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base_FieldAttributeBase__load_module_defaults_0.py:12: AssertionError
_________________________ test_invalid_module_defaults _________________________

    def test_invalid_module_defaults():
        field_attribute = FieldAttributeBase()
>       with pytest.raises(AnsibleParserError):
E       Failed: DID NOT RAISE <class 'ansible.errors.AnsibleParserError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base_FieldAttributeBase__load_module_defaults_0.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base_FieldAttributeBase__load_module_defaults_0.py::test_valid_module_defaults
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_base_FieldAttributeBase__load_module_defaults_0.py::test_invalid_module_defaults
============================== 2 failed in 0.59s ===============================
"""