
import pytest
from ansible.module_utils.facts.network.hpux import HPUXNetwork

@pytest.fixture(scope="module")
def hpux_network():
    return HPUXNetwork()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_network_hpux_HPUXNetwork_get_default_interfaces_1.py E [100%]

==================================== ERRORS ====================================
________________ ERROR at setup of test_get_default_interfaces _________________

    @pytest.fixture(scope="module")
    def hpux_network():
>       return HPUXNetwork()
E       TypeError: Network.__init__() missing 1 required positional argument: 'module'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_network_hpux_HPUXNetwork_get_default_interfaces_1.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_network_hpux_HPUXNetwork_get_default_interfaces_1.py::test_get_default_interfaces
=============================== 1 error in 0.71s ===============================
"""