
import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.compat import get_all_facts as compat_get_all_facts

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_compat_get_all_facts_0.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        module = MagicMock()
        module.params = {'gather_subset': None}
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_compat_get_all_facts_0.py:10: Failed
----------------------------- Captured stderr call -----------------------------
ValueError('not enough values to unpack (expected 3, got 0)')
ValueError('not enough values to unpack (expected 3, got 0)')
ValueError('not enough values to unpack (expected 3, got 0)')
ValueError('not enough values to unpack (expected 3, got 0)')
ValueError('not enough values to unpack (expected 3, got 0)')
KeyError('ansible_os_family')
ValueError('not enough values to unpack (expected 3, got 0)')
ValueError('not enough values to unpack (expected 3, got 0)')
ValueError('not enough values to unpack (expected 3, got 0)')
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_compat_get_all_facts_0.py::test_edge_cases
============================== 1 failed in 0.38s ===============================
"""