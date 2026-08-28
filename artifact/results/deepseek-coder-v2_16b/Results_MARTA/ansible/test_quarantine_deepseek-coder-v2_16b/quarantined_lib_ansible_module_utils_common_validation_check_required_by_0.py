
import pytest
from ansible.module_utils.common.validation import check_required_by



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_by_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_check_required_by_basic _________________________

    def test_check_required_by_basic():
        requirements = {'param1': ['req1', 'req2'], 'param2': 'req3'}
        parameters = {'param1': [1, 2], 'param2': 3, 'req1': 1, 'req2': 2, 'req3': 3}
    
        result = check_required_by(requirements, parameters)
>       assert result == {}
E       AssertionError: assert {'param1': [], 'param2': []} == {}
E         
E         Left contains 2 more items:
E         {'param1': [], 'param2': []}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_by_0.py:10: AssertionError
___________________ test_check_required_by_missing_parameter ___________________

    def test_check_required_by_missing_parameter():
        requirements = {'param1': ['req1', 'req2'], 'param2': 'req3'}
        parameters = {'param1': [1, 2], 'param2': 3}
    
        with pytest.raises(TypeError) as excinfo:
            check_required_by(requirements, parameters)
>       assert str(excinfo.value) == "missing parameter(s) required by 'param1': req1, req2 found in -> param1"
E       assert "missing para...': req1, req2" == 'missing para... in -> param1'
E         
E         Skipping 42 identical leading characters in diff, use -v to show
E         -  req1, req2 found in -> param1
E         +  req1, req2

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_by_0.py:18: AssertionError
_________________ test_check_required_by_with_options_context __________________

    def test_check_required_by_with_options_context():
        requirements = {'param1': ['req1', 'req2'], 'param2': 'req3'}
        parameters = {'param1': [1, 2], 'param2': 3}
    
        with pytest.raises(TypeError) as excinfo:
            check_required_by(requirements, parameters, options_context=['main_spec'])
>       assert str(excinfo.value) == "missing parameter(s) required by 'param1': req1, req2 found in -> main_spec -> param1"
E       AssertionError: assert 'missing para... in main_spec' == 'missing para...pec -> param1'
E         
E         Skipping 53 identical leading characters in diff, use -v to show
E         -  found in -> main_spec -> param1
E         +  found in main_spec

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_by_0.py:26: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_by_0.py::test_check_required_by_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_by_0.py::test_check_required_by_missing_parameter
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_required_by_0.py::test_check_required_by_with_options_context
============================== 3 failed in 0.31s ===============================
"""