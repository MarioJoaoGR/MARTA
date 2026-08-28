
import pytest
from ansible.vars.manager import VarsWithSources

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_manager_VarsWithSources___contains___0.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        vars_with_sources = VarsWithSources({'var1': 'source1', 'var2': 'source2'})
        with pytest.raises(KeyError):
>           assert 'var3' in vars_with_sources
E           AssertionError: assert 'var3' in <ansible.vars.manager.VarsWithSources object at 0x7f6565f1dae0>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_manager_VarsWithSources___contains___0.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_manager_VarsWithSources___contains___0.py::test_invalid_input
============================== 1 failed in 0.53s ===============================
"""