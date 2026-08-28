
import pytest
from unittest.mock import patch
from ansible.config.manager import _add_base_defs_deprecations

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager__add_base_defs_deprecations_0.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        base_defs = {
            'ini': {'deprecated_key': {'deprecated': True}},
            'env': {'ANSIBLE_DEPRECATED': {'deprecated': True}},
            'vars': {'var_with_deprecation': {'deprecated': True}}
        }
    
        with patch('ansible.config.manager._add_base_defs_deprecations', autospec=True) as mock_func:
            _add_base_defs_deprecations(base_defs)
    
>       assert 'collection_name' in base_defs['ini']['deprecated_key']['deprecated']
E       TypeError: argument of type 'bool' is not iterable

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager__add_base_defs_deprecations_0.py:16: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager__add_base_defs_deprecations_0.py::test_valid_input
============================== 1 failed in 0.28s ===============================
"""