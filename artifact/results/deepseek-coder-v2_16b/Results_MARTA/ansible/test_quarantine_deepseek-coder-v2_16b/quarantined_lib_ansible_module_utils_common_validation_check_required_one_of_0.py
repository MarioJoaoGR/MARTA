
import pytest
from ansible.module_utils.common.validation import check_required_one_of

def count_terms(term, parameters):
    return sum([1 for t in term if t in parameters])


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_one_of_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_missing_terms ______________________________

    def test_missing_terms():
        terms = [["param1", "param2"], ["foo", "bar"]]
        parameters = {"param1": 1, "foo": 3}
    
>       with pytest.raises(TypeError) as excinfo:
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_one_of_0.py:12: Failed
______________________________ test_nested_terms _______________________________

    def test_nested_terms():
        terms = [["nested1", "nested2"], ["foo", "bar"]]
        parameters = {"parent": {"nested1": 1, "nested2": None}}
    
        with pytest.raises(TypeError) as excinfo:
            check_required_one_of(terms, parameters, options_context=["parent"])
    
>       assert str(excinfo.value) == 'one of the following is required: nested1, nested2 found in terms -> parent'
E       AssertionError: assert 'one of the f...und in parent' == 'one of the f...rms -> parent'
E         
E         Skipping 50 identical leading characters in diff, use -v to show
E         -  found in terms -> parent
E         ?          ---------
E         +  found in parent

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_one_of_0.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_one_of_0.py::test_missing_terms
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_one_of_0.py::test_nested_terms
============================== 2 failed in 0.32s ===============================
"""