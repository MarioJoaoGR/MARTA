
import pytest
from ansible.module_utils.facts.network.linux import LinuxNetwork
import os
import glob
import struct
import socket

@pytest.fixture(scope="function")
def linux_network():
    return LinuxNetwork()



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_network_linux_LinuxNetwork_get_interfaces_info_1.py E [ 33%]
EE                                                                       [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_valid_input ______________________

    @pytest.fixture(scope="function")
    def linux_network():
>       return LinuxNetwork()
E       TypeError: Network.__init__() missing 1 required positional argument: 'module'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_network_linux_LinuxNetwork_get_interfaces_info_1.py:11: TypeError
_______________________ ERROR at setup of test_edge_case _______________________

    @pytest.fixture(scope="function")
    def linux_network():
>       return LinuxNetwork()
E       TypeError: Network.__init__() missing 1 required positional argument: 'module'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_network_linux_LinuxNetwork_get_interfaces_info_1.py:11: TypeError
_____________________ ERROR at setup of test_invalid_input _____________________

    @pytest.fixture(scope="function")
    def linux_network():
>       return LinuxNetwork()
E       TypeError: Network.__init__() missing 1 required positional argument: 'module'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_network_linux_LinuxNetwork_get_interfaces_info_1.py:11: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_network_linux_LinuxNetwork_get_interfaces_info_1.py::test_valid_input
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_network_linux_LinuxNetwork_get_interfaces_info_1.py::test_edge_case
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_network_linux_LinuxNetwork_get_interfaces_info_1.py::test_invalid_input
============================== 3 errors in 0.70s ===============================
"""