
import pytest
from ansible.constants import _DeprecatedSequenceConstant


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_constants__DeprecatedSequenceConstant___len___2.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_len_method ________________________________

    def test_len_method():
        deprecated_sequence = _DeprecatedSequenceConstant([1, 2, 3], "This sequence is deprecated.", "2.0")
>       with pytest.raises(DeprecationWarning) as excinfo:
E       Failed: DID NOT RAISE <class 'DeprecationWarning'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_constants__DeprecatedSequenceConstant___len___2.py:7: Failed
----------------------------- Captured stderr call -----------------------------
[DEPRECATION WARNING]: This sequence is deprecated. This feature will be 
removed in version 2.0. Deprecation warnings can be disabled by setting 
deprecation_warnings=False in ansible.cfg.
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_constants__DeprecatedSequenceConstant___len___2.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_constants__DeprecatedSequenceConstant___len___2.py::test_len_method
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_constants__DeprecatedSequenceConstant___len___2.py::test_invalid_inputs
============================== 2 failed in 0.81s ===============================
"""