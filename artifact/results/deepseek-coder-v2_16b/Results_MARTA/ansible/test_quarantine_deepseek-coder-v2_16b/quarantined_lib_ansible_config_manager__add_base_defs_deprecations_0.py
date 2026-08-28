
import pytest
from ansible.config.manager import _add_base_defs_deprecations


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager__add_base_defs_deprecations_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________ test_valid_input_with_deprecations ______________________

    def test_valid_input_with_deprecations():
        base_defs = {
            'ini': {'deprecated_key': {'deprecated': True}},
            'env': {'ANSIBLE_DEPRECATED': {'deprecated': True}},
            'vars': {'var_with_deprecation': {'deprecated': True}}
        }
        _add_base_defs_deprecations(base_defs)
>       assert 'collection_name' in base_defs['ini']['deprecated_key']['deprecated']
E       TypeError: argument of type 'bool' is not iterable

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager__add_base_defs_deprecations_0.py:12: TypeError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        base_defs = []
        with pytest.raises(TypeError):
>           _add_base_defs_deprecations(base_defs)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager__add_base_defs_deprecations_0.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

base_defs = []

    def _add_base_defs_deprecations(base_defs):
        '''Add deprecation source 'ansible.builtin' to deprecations in base.yml'''
        def process(entry):
            if 'deprecated' in entry:
                entry['deprecated']['collection_name'] = 'ansible.builtin'
    
>       for dummy, data in base_defs.items():
E       AttributeError: 'list' object has no attribute 'items'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/config/manager.py:269: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager__add_base_defs_deprecations_0.py::test_valid_input_with_deprecations
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager__add_base_defs_deprecations_0.py::test_invalid_input
============================== 2 failed in 0.50s ===============================
"""