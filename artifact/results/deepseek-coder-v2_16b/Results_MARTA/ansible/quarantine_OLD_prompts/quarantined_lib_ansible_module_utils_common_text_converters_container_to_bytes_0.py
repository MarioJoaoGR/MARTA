
import pytest
from unittest.mock import patch
from ansible.module_utils.common.text.converters import to_bytes

def container_to_bytes(d, encoding='utf-8', errors='surrogate_or_strict'):
    if isinstance(d, str):
        return to_bytes(d, encoding=encoding, errors=errors)
    elif isinstance(d, dict):
        return {container_to_bytes(k, encoding, errors): container_to_bytes(v, encoding, errors) for k, v in d.items()}
    elif isinstance(d, list):
        return [container_to_bytes(item, encoding, errors) for item in d]
    elif isinstance(d, tuple):
        return tuple(container_to_bytes(item, encoding, errors) for item in d)
    else:
        return d



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_converters_container_to_bytes_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_valid_dictionary _____________________________

    def test_valid_dictionary():
        d = {'key1': 'value1', 'key2': [1, 2, 3]}
        with patch('ansible.module_utils.common.text.converters.to_bytes', return_value={b'key1': b'value1', b'key2': [b'1', b'2', b'3']}):
            result = container_to_bytes(d)
>           assert result == {b'key1': b'value1', b'key2': [b'1', b'2', b'3']}
E           AssertionError: assert {b'key1': b'v...2': [1, 2, 3]} == {b'key1': b'v..., b'2', b'3']}
E             
E             Omitting 1 identical items, use -vv to show
E             Differing items:
E             {b'key2': [1, 2, 3]} != {b'key2': [b'1', b'2', b'3']}
E             Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_converters_container_to_bytes_0.py:22: AssertionError
_____________________________ test_edge_none_input _____________________________

    def test_edge_none_input():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_converters_container_to_bytes_0.py:25: Failed
_________________________ test_invalid_encoding_error __________________________

    def test_invalid_encoding_error():
        d = 'Hello, World!'
        with patch('ansible.module_utils.common.text.converters.to_bytes', side_effect=UnicodeEncodeError):
>           with pytest.raises(UnicodeEncodeError):
E           Failed: DID NOT RAISE <class 'UnicodeEncodeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_converters_container_to_bytes_0.py:31: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_converters_container_to_bytes_0.py::test_valid_dictionary
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_converters_container_to_bytes_0.py::test_edge_none_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_text_converters_container_to_bytes_0.py::test_invalid_encoding_error
============================== 3 failed in 0.29s ===============================
"""