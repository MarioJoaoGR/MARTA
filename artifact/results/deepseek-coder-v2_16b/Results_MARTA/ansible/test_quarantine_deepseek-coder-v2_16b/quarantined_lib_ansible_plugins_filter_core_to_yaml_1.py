
import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import to_yaml
import yaml


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_yaml_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_valid_case_basic _____________________________

    def test_valid_case_basic():
        input_data = {'key': 'value'}
        expected_output = yaml.dump(input_data)
        result = to_yaml(input_data)
>       assert result == expected_output, f"Expected {expected_output}, but got {result}"
E       AssertionError: Expected key: value
E         , but got {key: value}
E         
E       assert '{key: value}\n' == 'key: value\n'
E         
E         - key: value
E         + {key: value}
E         ? +          +

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_yaml_1.py:11: AssertionError
_______________________ test_invalid_case_error_handling _______________________

    def test_invalid_case_error_handling():
        input_data = "['invalid', 'input']"
>       with pytest.raises(AnsibleFilterError):
E       Failed: DID NOT RAISE <class 'ansible.errors.AnsibleFilterError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_yaml_1.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_yaml_1.py::test_valid_case_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_to_yaml_1.py::test_invalid_case_error_handling
============================== 2 failed in 0.90s ===============================
"""