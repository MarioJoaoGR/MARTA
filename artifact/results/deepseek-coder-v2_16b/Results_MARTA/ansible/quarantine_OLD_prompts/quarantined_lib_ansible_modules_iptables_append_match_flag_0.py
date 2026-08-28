
import pytest
from ansible.modules.iptables import append_match_flag



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_iptables_append_match_flag_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________ test_valid_case_negate_not_negatable _____________________

    def test_valid_case_negate_not_negatable():
        rule = []
        append_match_flag(rule, 'negate', 'DENY', False)
>       assert rule == ['!', 'DENY']
E       AssertionError: assert [] == ['!', 'DENY']
E         
E         Right contains 2 more items, first extra item: '!'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_iptables_append_match_flag_0.py:8: AssertionError
________________________ test_error_case_invalid_param _________________________

    def test_error_case_invalid_param():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_iptables_append_match_flag_0.py:11: Failed
_________________ test_error_case_negatable_false_with_negate __________________

    def test_error_case_negatable_false_with_negate():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_iptables_append_match_flag_0.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_iptables_append_match_flag_0.py::test_valid_case_negate_not_negatable
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_iptables_append_match_flag_0.py::test_error_case_invalid_param
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_modules_iptables_append_match_flag_0.py::test_error_case_negatable_false_with_negate
============================== 3 failed in 0.22s ===============================
"""