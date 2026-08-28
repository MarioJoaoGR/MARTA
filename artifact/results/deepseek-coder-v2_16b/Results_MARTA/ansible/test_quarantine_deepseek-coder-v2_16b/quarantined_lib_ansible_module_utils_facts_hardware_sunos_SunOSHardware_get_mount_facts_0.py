
import pytest
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture(scope="module")
def sunos_hardware():
    return SunOSHardware()


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_sunos_SunOSHardware_get_mount_facts_0.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
_______ ERROR at setup of test_get_mount_facts_returns_correct_structure _______

    @pytest.fixture(scope="module")
    def sunos_hardware():
>       return SunOSHardware()
E       TypeError: Hardware.__init__() missing 1 required positional argument: 'module'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_sunos_SunOSHardware_get_mount_facts_0.py:7: TypeError
______ ERROR at setup of test_get_mount_facts_returns_correct_mount_info _______

    @pytest.fixture(scope="module")
    def sunos_hardware():
>       return SunOSHardware()
E       TypeError: Hardware.__init__() missing 1 required positional argument: 'module'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_sunos_SunOSHardware_get_mount_facts_0.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_sunos_SunOSHardware_get_mount_facts_0.py::test_get_mount_facts_returns_correct_structure
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_sunos_SunOSHardware_get_mount_facts_0.py::test_get_mount_facts_returns_correct_mount_info
============================== 2 errors in 0.36s ===============================
"""