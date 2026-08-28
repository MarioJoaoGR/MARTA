
import pytest
from ansible.module_utils.common.validation import check_mutually_exclusive

def count_terms(terms, parameters):
    return sum([1 for term in terms if term in parameters])



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_mutually_exclusive_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_valid_input_basic ____________________________

    def test_valid_input_basic():
        terms = [['param1', 'param2'], ['param3']]
        parameters = {'param1': 1, 'param2': 2, 'param3': 3}
>       result = check_mutually_exclusive(terms, parameters)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_mutually_exclusive_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

terms = [['param1', 'param2'], ['param3']]
parameters = {'param1': 1, 'param2': 2, 'param3': 3}, options_context = None

    def check_mutually_exclusive(terms, parameters, options_context=None):
        """Check mutually exclusive terms against argument parameters
    
        Accepts a single list or list of lists that are groups of terms that should be
        mutually exclusive with one another
    
        :arg terms: List of mutually exclusive parameters
        :arg parameters: Dictionary of parameters
        :kwarg options_context: List of strings of parent key names if ``terms`` are
            in a sub spec.
    
        :returns: Empty list or raises :class:`TypeError` if the check fails.
        """
    
        results = []
        if terms is None:
            return results
    
        for check in terms:
            count = count_terms(check, parameters)
            if count > 1:
                results.append(check)
    
        if results:
            full_list = ['|'.join(check) for check in results]
            msg = "parameters are mutually exclusive: %s" % ', '.join(full_list)
            if options_context:
                msg = "{0} found in {1}".format(msg, " -> ".join(options_context))
>           raise TypeError(to_native(msg))
E           TypeError: parameters are mutually exclusive: param1|param2

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/common/validation.py:98: TypeError
__________________________ test_error_input_conflict ___________________________

    def test_error_input_conflict():
        terms = ['param1', 'param1']
        parameters = {'param1': 1, 'param2': 2}
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_mutually_exclusive_0.py:17: Failed
________________________ test_error_input_missing_lines ________________________

    def test_error_input_missing_lines():
        terms = None
        parameters = {'param1': 1, 'param2': 2}
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_mutually_exclusive_0.py:23: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_mutually_exclusive_0.py::test_valid_input_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_mutually_exclusive_0.py::test_error_input_conflict
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_mutually_exclusive_0.py::test_error_input_missing_lines
============================== 3 failed in 0.31s ===============================
"""