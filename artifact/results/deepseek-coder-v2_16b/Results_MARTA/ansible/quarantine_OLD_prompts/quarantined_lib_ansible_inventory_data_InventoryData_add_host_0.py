
import pytest
from unittest.mock import patch, MagicMock
from ansible.inventory.data import InventoryData, Host
from ansible.errors import AnsibleError


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_add_invalid_host _____________________________

    def test_add_invalid_host():
        inventory = InventoryData()
        with pytest.raises(AnsibleError) as e:
            inventory.add_host('')
>       assert str(e.value) == "Invalid empty host name provided: ''"
E       assert 'Invalid empt...me provided: ' == "Invalid empt... provided: ''"
E         
E         - Invalid empty host name provided: ''
E         ?                                   --
E         + Invalid empty host name provided:

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_0.py:11: AssertionError
_________________________ test_add_duplicate_localhost _________________________

    def test_add_duplicate_localhost():
        inventory = InventoryData()
        inventory.add_group('webservers')
        inventory.add_host('local1', group='webservers')
        with patch('ansible.inventory.data.display') as mock_display:
            inventory.add_host('local1')
            assert 'local1' in inventory.hosts
            expected_message = "A duplicate localhost-like entry was found (Host(name='local1')). First found localhost was Host(name='local1')"
>           mock_display.warning.assert_called_with(expected_message)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_0.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='display.warning' id='139985822886080'>
args = ("A duplicate localhost-like entry was found (Host(name='local1')). First found localhost was Host(name='local1')",)
kwargs = {}
expected = 'warning("A duplicate localhost-like entry was found (Host(name=\'local1\')). First found localhost was Host(name=\'local1\')")'
actual = 'not called.'
error_message = 'expected call not found.\nExpected: warning("A duplicate localhost-like entry was found (Host(name=\'local1\')). First found localhost was Host(name=\'local1\')")\nActual: not called.'

    def assert_called_with(self, /, *args, **kwargs):
        """assert that the last call was made with the specified arguments.
    
        Raises an AssertionError if the args and keyword args passed in are
        different to the last call to the mock."""
        if self.call_args is None:
            expected = self._format_mock_call_signature(args, kwargs)
            actual = 'not called.'
            error_message = ('expected call not found.\nExpected: %s\nActual: %s'
                    % (expected, actual))
>           raise AssertionError(error_message)
E           AssertionError: expected call not found.
E           Expected: warning("A duplicate localhost-like entry was found (Host(name='local1')). First found localhost was Host(name='local1')")
E           Actual: not called.

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:920: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_0.py::test_add_invalid_host
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_inventory_data_InventoryData_add_host_0.py::test_add_duplicate_localhost
============================== 2 failed in 0.49s ===============================
"""