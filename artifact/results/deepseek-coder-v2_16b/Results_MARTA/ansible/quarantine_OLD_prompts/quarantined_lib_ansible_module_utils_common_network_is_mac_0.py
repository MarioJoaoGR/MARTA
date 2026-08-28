
import re
import pytest
from unittest.mock import patch

def is_mac(mac_address):
    """
    Validate MAC address for given string
    Args:
        mac_address: string to validate as MAC address

    Returns: (Boolean) True if string is valid MAC address, otherwise False
    """
    mac_addr_regex = re.compile('[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$')
    return bool(mac_addr_regex.match(mac_address.lower()))

# Test cases for valid MAC addresses

# Test case for None input, which should raise a TypeError
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_network_is_mac_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________________ test_valid_mac_addresses ___________________________

    def test_valid_mac_addresses():
        assert is_mac("12:34:56:78:9A:BC") == True
        assert is_mac("12-34-56-78-9A-BC") == True
>       assert is_mac("12.34.56.78.9A.BC") == True
E       AssertionError: assert False == True
E        +  where False = is_mac('12.34.56.78.9A.BC')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_network_is_mac_0.py:21: AssertionError
_______________________________ test_none_input ________________________________

    def test_none_input():
        with pytest.raises(TypeError):
>           is_mac(None)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_network_is_mac_0.py:26: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

mac_address = None

    def is_mac(mac_address):
        """
        Validate MAC address for given string
        Args:
            mac_address: string to validate as MAC address
    
        Returns: (Boolean) True if string is valid MAC address, otherwise False
        """
        mac_addr_regex = re.compile('[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$')
>       return bool(mac_addr_regex.match(mac_address.lower()))
E       AttributeError: 'NoneType' object has no attribute 'lower'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_network_is_mac_0.py:15: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_network_is_mac_0.py::test_valid_mac_addresses
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_network_is_mac_0.py::test_none_input
============================== 2 failed in 0.25s ===============================
"""