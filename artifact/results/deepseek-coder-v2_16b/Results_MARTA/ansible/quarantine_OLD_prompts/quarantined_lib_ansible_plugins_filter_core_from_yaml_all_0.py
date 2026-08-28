
import pytest
from ansible.plugins.filter.core import from_yaml_all
import yaml



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_from_yaml_all_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_from_yaml_all_with_string ________________________

    def test_from_yaml_all_with_string():
        yaml_data = "key: value"
        result = from_yaml_all(yaml_data)
>       assert isinstance(result, list), f"Expected a list but got {type(result)}"
E       AssertionError: Expected a list but got <class 'generator'>
E       assert False
E        +  where False = isinstance(<generator object load_all at 0x7f2988ca2500>, list)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_from_yaml_all_0.py:9: AssertionError
_________________________ test_from_yaml_all_with_dict _________________________

    def test_from_yaml_all_with_dict():
        loaded_object = {"another_key": "another_value"}
        result = from_yaml_all(loaded_object)
>       assert isinstance(result, list), f"Expected a list but got {type(result)}"
E       AssertionError: Expected a list but got <class 'dict'>
E       assert False
E        +  where False = isinstance({'another_key': 'another_value'}, list)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_from_yaml_all_0.py:16: AssertionError
_________________________ test_from_yaml_all_with_file _________________________

    def test_from_yaml_all_with_file():
        import os
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, 'data.yml')  # Assuming data.yml exists in the same directory as the script
>       with open(file_path, 'r') as f:
E       FileNotFoundError: [Errno 2] No such file or directory: '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/data.yml'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_from_yaml_all_0.py:24: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_from_yaml_all_0.py::test_from_yaml_all_with_string
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_from_yaml_all_0.py::test_from_yaml_all_with_dict
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_filter_core_from_yaml_all_0.py::test_from_yaml_all_with_file
============================== 3 failed in 0.53s ===============================
"""