
import pytest
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

@pytest.fixture(scope="module")
def darwin_hardware():
    return DarwinHardware()


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_darwin_DarwinHardware_get_cpu_facts_0.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
__________________ ERROR at setup of test_get_cpu_facts_intel __________________

    @pytest.fixture(scope="module")
    def darwin_hardware():
>       return DarwinHardware()
E       TypeError: Hardware.__init__() missing 1 required positional argument: 'module'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_darwin_DarwinHardware_get_cpu_facts_0.py:7: TypeError
_________________ ERROR at setup of test_get_cpu_facts_powerpc _________________

    @pytest.fixture(scope="module")
    def darwin_hardware():
>       return DarwinHardware()
E       TypeError: Hardware.__init__() missing 1 required positional argument: 'module'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_darwin_DarwinHardware_get_cpu_facts_0.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_darwin_DarwinHardware_get_cpu_facts_0.py::test_get_cpu_facts_intel
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_darwin_DarwinHardware_get_cpu_facts_0.py::test_get_cpu_facts_powerpc
============================== 2 errors in 0.35s ===============================
"""