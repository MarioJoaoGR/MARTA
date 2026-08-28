
import pytest
from ansible.plugins.filter import mathstuff

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_mathstuff_difference_2.py F [100%]

=================================== FAILURES ===================================
_________________________ test_error_case_non_hashable _________________________

    def test_error_case_non_hashable():
        environment = {'var': 'value'}
        a = ['a', 1]
        b = {'b': 2}
    
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_mathstuff_difference_2.py:10: Failed
----------------------------- Captured stderr call -----------------------------
[WARNING]: Falling back to Ansible unique filter as Jinja2 one failed: 'dict'
object has no attribute 'is_async'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_mathstuff_difference_2.py::test_error_case_non_hashable
============================== 1 failed in 0.74s ===============================
"""