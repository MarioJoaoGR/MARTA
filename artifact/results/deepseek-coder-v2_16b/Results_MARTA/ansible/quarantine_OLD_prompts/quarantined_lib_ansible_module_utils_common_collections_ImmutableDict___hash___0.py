
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
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_collections_ImmutableDict___hash___0.py F [100%]

=================================== FAILURES ===================================
_________________________ test_immutable_dict_creation _________________________

    def test_immutable_dict_creation():
        immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
        assert isinstance(immutable_dict, ImmutableDict)
        with pytest.raises(AttributeError):
>           immutable_dict['new_key'] = 'new_value'
E           TypeError: 'ImmutableDict' object does not support item assignment

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_collections_ImmutableDict___hash___0.py:9: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_collections_ImmutableDict___hash___0.py::test_immutable_dict_creation
============================== 1 failed in 0.25s ===============================
"""