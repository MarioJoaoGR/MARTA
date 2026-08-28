
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
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_get_reserved_names_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________ test_get_reserved_names_default ________________________

    def test_get_reserved_names_default():
        """Test that get_reserved_names returns the correct set of public reserved names by default."""
        expected = {'action', 'local_action'}
>       assert get_reserved_names() == expected
E       AssertionError: assert {'action', 'a...'become', ...} == {'action', 'local_action'}
E         
E         Extra items in the left set:
E         'ignore_errors'
E         'changed_when'
E         'timeout'
E         'delay'
E         'diff'...
E         
E         ...Full output truncated (57 lines hidden), use '-vv' to show

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_get_reserved_names_0.py:8: AssertionError
________________ test_get_reserved_names_include_private_false _________________

    def test_get_reserved_names_include_private_false():
        """Test that get_reserved_names returns only public reserved names when include_private is False."""
        expected = {'action', 'local_action'}
>       assert get_reserved_names(include_private=False) == expected
E       AssertionError: assert {'action', 'a...'become', ...} == {'action', 'local_action'}
E         
E         Extra items in the left set:
E         'ignore_errors'
E         'changed_when'
E         'timeout'
E         'delay'
E         'diff'...
E         
E         ...Full output truncated (57 lines hidden), use '-vv' to show

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_get_reserved_names_0.py:13: AssertionError
_________________ test_get_reserved_names_include_private_true _________________

    def test_get_reserved_names_include_private_true():
        """Test that get_reserved_names returns both public and private reserved names when include_private is True."""
        expected = {'action', 'local_action', 'with_'}
>       assert get_reserved_names(include_private=True) == expected
E       AssertionError: assert {'action', 'a...'become', ...} == {'action', 'l...ion', 'with_'}
E         
E         Extra items in the left set:
E         'ignore_errors'
E         'changed_when'
E         'timeout'
E         'delay'
E         'diff'...
E         
E         ...Full output truncated (56 lines hidden), use '-vv' to show

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_get_reserved_names_0.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_get_reserved_names_0.py::test_get_reserved_names_default
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_get_reserved_names_0.py::test_get_reserved_names_include_private_false
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_vars_reserved_get_reserved_names_0.py::test_get_reserved_names_include_private_true
============================== 3 failed in 0.64s ===============================
"""