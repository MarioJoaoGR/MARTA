
import pytest
from ansible.vars.reserved import get_reserved_names


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_get_reserved_names_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________ test_edge_case_no_include_private _______________________

    def test_edge_case_no_include_private():
        reserved_names = get_reserved_names(include_private=False)
        assert 'action' in reserved_names
        assert 'local_action' in reserved_names
>       assert 'with_' not in reserved_names
E       AssertionError: assert 'with_' not in {'action', 'always', 'any_errors_fatal', 'args', 'async_val', 'become', ...}

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_get_reserved_names_1.py:9: AssertionError
___________________________ test_invalid_input_none ____________________________

    def test_invalid_input_none():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_get_reserved_names_1.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_get_reserved_names_1.py::test_edge_case_no_include_private
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_get_reserved_names_1.py::test_invalid_input_none
============================== 2 failed in 0.97s ===============================
"""