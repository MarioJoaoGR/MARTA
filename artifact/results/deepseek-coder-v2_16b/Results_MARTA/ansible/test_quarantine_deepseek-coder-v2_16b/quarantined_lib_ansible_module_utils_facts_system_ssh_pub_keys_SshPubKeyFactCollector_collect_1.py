
import pytest
from lib.ansible.module_utils.facts.system.ssh_pub_keys import SshPubKeyFactCollector


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_ssh_pub_keys_SshPubKeyFactCollector_collect_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        ssh_pub_key_collector = SshPubKeyFactCollector()
        collected_facts = ssh_pub_key_collector.collect()
        assert isinstance(collected_facts, dict), "Collected facts should be a dictionary"
>       assert 'ssh_host_pub_keys' in collected_facts, "Expected key 'ssh_host_pub_keys' not found in collected facts"
E       AssertionError: Expected key 'ssh_host_pub_keys' not found in collected facts
E       assert 'ssh_host_pub_keys' in {}

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_ssh_pub_keys_SshPubKeyFactCollector_collect_1.py:9: AssertionError
________________________________ test_edge_case ________________________________

    def test_edge_case():
        ssh_pub_key_collector = SshPubKeyFactCollector()
>       with pytest.raises(Exception):
E       Failed: DID NOT RAISE <class 'Exception'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_ssh_pub_keys_SshPubKeyFactCollector_collect_1.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_ssh_pub_keys_SshPubKeyFactCollector_collect_1.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_system_ssh_pub_keys_SshPubKeyFactCollector_collect_1.py::test_edge_case
============================== 2 failed in 0.72s ===============================
"""