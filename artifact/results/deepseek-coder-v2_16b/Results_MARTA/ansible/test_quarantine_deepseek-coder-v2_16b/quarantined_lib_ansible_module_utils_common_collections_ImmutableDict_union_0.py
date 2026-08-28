
import pytest
from ansible.module_utils.common.collections import ImmutableDict


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_collections_ImmutableDict_union_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_union _______________________________

    def test_valid_union():
        immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
        overriding_mapping = {'key3': 'value3'}
        combined_dict = immutable_dict.union(overriding_mapping)
        assert isinstance(combined_dict, ImmutableDict), "Expected a new ImmutableDict instance"
>       assert combined_dict == {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}, "Combined dictionary does not match expected values"
E       AssertionError: Combined dictionary does not match expected values
E       assert ImmutableDict...3': 'value3'}) == {'key1': 'val...y3': 'value3'}
E         
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_collections_ImmutableDict_union_0.py:10: AssertionError
______________________________ test_invalid_union ______________________________

    def test_invalid_union():
        immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_collections_ImmutableDict_union_0.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_collections_ImmutableDict_union_0.py::test_valid_union
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_collections_ImmutableDict_union_0.py::test_invalid_union
============================== 2 failed in 0.67s ===============================
"""