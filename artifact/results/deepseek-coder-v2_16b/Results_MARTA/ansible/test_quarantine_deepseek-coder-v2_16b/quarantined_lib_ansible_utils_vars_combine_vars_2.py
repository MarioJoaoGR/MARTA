
import pytest
from ansible.utils.vars import combine_vars


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_vars_combine_vars_2.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________ test_combine_vars_default_merge ________________________

    def test_combine_vars_default_merge():
        # Define two dictionaries to be merged
        dict1 = {'a': 1, 'b': {'c': 2}}
        dict2 = {'b': {'d': 3}, 'e': 4}
    
        # Call the function with default merge behavior
        result = combine_vars(dict1, dict2)
    
>       assert result == {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
E       AssertionError: assert {'a': 1, 'b':...': 3}, 'e': 4} == {'a': 1, 'b':...': 3}, 'e': 4}
E         
E         Omitting 2 identical items, use -vv to show
E         Differing items:
E         {'b': {'d': 3}} != {'b': {'c': 2, 'd': 3}}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_vars_combine_vars_2.py:13: AssertionError
____________________________ test_combine_vars_none ____________________________

    def test_combine_vars_none():
        # Define two dictionaries where the default behavior should be used (merge if C.DEFAULT_HASH_BEHAVIOUR is 'merge')
        dict1 = {'a': 1, 'b': {'c': 2}}
        dict2 = {'b': {'d': 3}, 'e': 4}
    
        # Call the function without specifying merge behavior
        result = combine_vars(dict1, dict2)
    
>       assert result == {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
E       AssertionError: assert {'a': 1, 'b':...': 3}, 'e': 4} == {'a': 1, 'b':...': 3}, 'e': 4}
E         
E         Omitting 2 identical items, use -vv to show
E         Differing items:
E         {'b': {'d': 3}} != {'b': {'c': 2, 'd': 3}}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_vars_combine_vars_2.py:23: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_vars_combine_vars_2.py::test_combine_vars_default_merge
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_vars_combine_vars_2.py::test_combine_vars_none
============================== 2 failed in 0.78s ===============================
"""