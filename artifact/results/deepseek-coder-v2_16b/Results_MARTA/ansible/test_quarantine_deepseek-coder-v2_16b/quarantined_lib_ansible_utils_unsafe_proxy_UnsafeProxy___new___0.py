
import pytest
from ansible.utils.unsafe_proxy import UnsafeProxy


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_unsafe_proxy_UnsafeProxy___new___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
>       with pytest.raises(TypeError) as excinfo:
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_unsafe_proxy_UnsafeProxy___new___0.py:6: Failed
----------------------------- Captured stderr call -----------------------------
[DEPRECATION WARNING]: UnsafeProxy is being deprecated. Use wrap_var or 
AnsibleUnsafeBytes/AnsibleUnsafeText directly instead. This feature will be 
removed from ansible-core in version 2.13. Deprecation warnings can be disabled
 by setting deprecation_warnings=False in ansible.cfg.
___________________________ test_invalid_input_type ____________________________

    def test_invalid_input_type():
>       with pytest.raises(TypeError) as excinfo:
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_unsafe_proxy_UnsafeProxy___new___0.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_unsafe_proxy_UnsafeProxy___new___0.py::test_none_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_unsafe_proxy_UnsafeProxy___new___0.py::test_invalid_input_type
============================== 2 failed in 0.40s ===============================
"""