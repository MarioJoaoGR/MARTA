
import pytest
from ansible.module_utils.common.validation import check_type_jsonarg


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_type_jsonarg_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_type _______________________________

    def test_invalid_type():
        value = 12345
        with pytest.raises(TypeError) as excinfo:
            check_type_jsonarg(value)
>       assert str(excinfo.value) == f"{type(value).__name__} cannot be converted to a json string"
E       assert "<class 'int'...a json string" == 'int cannot b...a json string'
E         
E         - int cannot be converted to a json string
E         + <class 'int'> cannot be converted to a json string
E         ? ++++++++   ++

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_type_jsonarg_0.py:9: AssertionError
_______________________________ test_none_input ________________________________

    def test_none_input():
        value = None
        with pytest.raises(TypeError) as excinfo:
            check_type_jsonarg(value)
>       assert str(excinfo.value) == f"{type(value).__name__} cannot be converted to a json string"
E       assert "<class 'None...a json string" == 'NoneType can...a json string'
E         
E         - NoneType cannot be converted to a json string
E         + <class 'NoneType'> cannot be converted to a json string
E         ? ++++++++        ++

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_type_jsonarg_0.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_type_jsonarg_0.py::test_invalid_type
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_validation_check_type_jsonarg_0.py::test_none_input
============================== 2 failed in 0.31s ===============================
"""