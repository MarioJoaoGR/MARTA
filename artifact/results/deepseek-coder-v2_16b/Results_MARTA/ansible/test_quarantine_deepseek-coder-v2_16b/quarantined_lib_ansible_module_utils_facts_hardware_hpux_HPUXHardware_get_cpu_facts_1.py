
import pytest
from ansible.module_utils.facts.hardware.hpux import HPUXHardware

@pytest.fixture(scope="function")
def hardware():
    return HPUXHardware()


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_hpux_HPUXHardware_get_cpu_facts_1.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
_______________ ERROR at setup of test_get_cpu_facts_ia64_B11_23 _______________

    @pytest.fixture(scope="function")
    def hardware():
>       return HPUXHardware()
E       TypeError: Hardware.__init__() missing 1 required positional argument: 'module'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_hpux_HPUXHardware_get_cpu_facts_1.py:7: TypeError
_______________ ERROR at setup of test_get_cpu_facts_ia64_B11_31 _______________

    @pytest.fixture(scope="function")
    def hardware():
>       return HPUXHardware()
E       TypeError: Hardware.__init__() missing 1 required positional argument: 'module'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_hpux_HPUXHardware_get_cpu_facts_1.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_hpux_HPUXHardware_get_cpu_facts_1.py::test_get_cpu_facts_ia64_B11_23
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_hpux_HPUXHardware_get_cpu_facts_1.py::test_get_cpu_facts_ia64_B11_31
============================== 2 errors in 0.73s ===============================
"""