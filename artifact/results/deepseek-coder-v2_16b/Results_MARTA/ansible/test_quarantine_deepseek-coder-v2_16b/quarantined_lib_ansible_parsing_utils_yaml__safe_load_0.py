
import pytest
import yaml
from ansible.parsing.utils.yaml import _safe_load


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_utils_yaml__safe_load_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_missing_lines_to_cover __________________________

    def test_missing_lines_to_cover():
        # Test that a missing YAML stream raises a YAMLError
>       with pytest.raises(yaml.YAMLError):
E       Failed: DID NOT RAISE <class 'yaml.error.YAMLError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_utils_yaml__safe_load_0.py:8: Failed
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test that invalid YAML input raises a YAMLError
        yaml_data = """
        key: value
        list:
          - item1
          - item2
        """
>       with pytest.raises(yaml.YAMLError):
E       Failed: DID NOT RAISE <class 'yaml.error.YAMLError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_utils_yaml__safe_load_0.py:19: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_utils_yaml__safe_load_0.py::test_missing_lines_to_cover
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_parsing_utils_yaml__safe_load_0.py::test_invalid_input
============================== 2 failed in 0.33s ===============================
"""