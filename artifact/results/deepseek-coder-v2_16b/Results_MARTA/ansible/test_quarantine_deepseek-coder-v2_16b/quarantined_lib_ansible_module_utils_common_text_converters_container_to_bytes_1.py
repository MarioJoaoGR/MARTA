
import pytest
from ansible.module_utils.common.text.converters import container_to_bytes


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_converters_container_to_bytes_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_case_dict _____________________________

    def test_valid_case_dict():
        d = {'key1': 'value1', 'key2': [1, 2, 3]}
        expected_output = {b'key1': b'value1', b'key2': [b'1', b'2', b'3']}
>       assert container_to_bytes(d) == expected_output
E       AssertionError: assert {b'key1': b'v...2': [1, 2, 3]} == {b'key1': b'v..., b'2', b'3']}
E         
E         Omitting 1 identical items, use -vv to show
E         Differing items:
E         {b'key2': [1, 2, 3]} != {b'key2': [b'1', b'2', b'3']}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_converters_container_to_bytes_1.py:8: AssertionError
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_converters_container_to_bytes_1.py:11: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_converters_container_to_bytes_1.py::test_valid_case_dict
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_converters_container_to_bytes_1.py::test_edge_case_none
============================== 2 failed in 0.65s ===============================
"""