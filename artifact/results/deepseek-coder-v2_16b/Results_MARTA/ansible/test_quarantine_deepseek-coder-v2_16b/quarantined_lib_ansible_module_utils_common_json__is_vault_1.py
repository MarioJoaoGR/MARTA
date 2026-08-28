
import pytest
from ansible.module_utils.common.json import _is_vault

@pytest.mark.parametrize("data, expected", [
    ({'key': 'value', '__ENCRYPTED__': True}, True),
    ({'key': 'value'}, False),
    (None, False)
])
def test_is_vault(data, expected):
    result = _is_vault(data)
    assert result == expected
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_json__is_vault_1.py F [ 33%]
..                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_is_vault[data0-True] ___________________________

data = {'__ENCRYPTED__': True, 'key': 'value'}, expected = True

    @pytest.mark.parametrize("data, expected", [
        ({'key': 'value', '__ENCRYPTED__': True}, True),
        ({'key': 'value'}, False),
        (None, False)
    ])
    def test_is_vault(data, expected):
        result = _is_vault(data)
>       assert result == expected
E       assert False == True

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_json__is_vault_1.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_json__is_vault_1.py::test_is_vault[data0-True]
========================= 1 failed, 2 passed in 0.66s ==========================
"""