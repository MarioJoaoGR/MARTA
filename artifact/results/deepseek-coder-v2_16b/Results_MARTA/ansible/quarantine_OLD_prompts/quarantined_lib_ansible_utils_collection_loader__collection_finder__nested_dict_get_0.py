
import pytest
from ansible.utils.collection_loader._collection_finder import _nested_dict_get


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__nested_dict_get_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_error_case ________________________________

    def test_error_case():
        data = [{'a': {'b': {'c': 1}}}]
>       assert _nested_dict_get(data, ['a', 'b', 'c']) is None

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__nested_dict_get_0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

root_dict = [{'a': {'b': {'c': 1}}}], key_list = ['a', 'b', 'c']

    def _nested_dict_get(root_dict, key_list):
        cur_value = root_dict
        for key in key_list:
>           cur_value = cur_value.get(key)
E           AttributeError: 'list' object has no attribute 'get'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/collection_loader/_collection_finder.py:1017: AttributeError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
            data = "not a dictionary"
>           _nested_dict_get(data, ['a', 'b', 'c'])

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__nested_dict_get_0.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

root_dict = 'not a dictionary', key_list = ['a', 'b', 'c']

    def _nested_dict_get(root_dict, key_list):
        cur_value = root_dict
        for key in key_list:
>           cur_value = cur_value.get(key)
E           AttributeError: 'str' object has no attribute 'get'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/collection_loader/_collection_finder.py:1017: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__nested_dict_get_0.py::test_error_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_collection_loader__collection_finder__nested_dict_get_0.py::test_invalid_input
============================== 2 failed in 0.39s ===============================
"""