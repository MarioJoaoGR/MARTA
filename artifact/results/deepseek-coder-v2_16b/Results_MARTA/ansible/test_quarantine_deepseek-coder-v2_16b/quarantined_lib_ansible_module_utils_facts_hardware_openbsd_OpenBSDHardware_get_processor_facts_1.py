
import pytest
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

@pytest.fixture(scope="module")
def sysctl_info():
    return {'hw.model': ['Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz', 'Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz'], 'hw.ncpuonline': '2'}

@pytest.fixture(scope="module")
def hardware_instance(sysctl_info):
    return OpenBSDHardware(sysctl=sysctl_info)


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_openbsd_OpenBSDHardware_get_processor_facts_1.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
_______________ ERROR at setup of test_get_processor_facts_count _______________

sysctl_info = {'hw.model': ['Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz', 'Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz'], 'hw.ncpuonline': '2'}

    @pytest.fixture(scope="module")
    def hardware_instance(sysctl_info):
>       return OpenBSDHardware(sysctl=sysctl_info)
E       TypeError: Hardware.__init__() got an unexpected keyword argument 'sysctl'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_openbsd_OpenBSDHardware_get_processor_facts_1.py:11: TypeError
____________ ERROR at setup of test_get_processor_facts_count_cores ____________

sysctl_info = {'hw.model': ['Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz', 'Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz'], 'hw.ncpuonline': '2'}

    @pytest.fixture(scope="module")
    def hardware_instance(sysctl_info):
>       return OpenBSDHardware(sysctl=sysctl_info)
E       TypeError: Hardware.__init__() got an unexpected keyword argument 'sysctl'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_openbsd_OpenBSDHardware_get_processor_facts_1.py:11: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_openbsd_OpenBSDHardware_get_processor_facts_1.py::test_get_processor_facts_count
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_hardware_openbsd_OpenBSDHardware_get_processor_facts_1.py::test_get_processor_facts_count_cores
============================== 2 errors in 0.71s ===============================
"""