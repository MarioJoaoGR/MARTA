
import pytest
from ansible.module_utils.facts.packages import CLIMgr

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_CLIMgr___init___2.py F [100%]

=================================== FAILURES ===================================
__________________________ test_CLIMgr_initialization __________________________

    def test_CLIMgr_initialization():
>       cli_mgr = CLIMgr()
E       TypeError: Can't instantiate abstract class CLIMgr with abstract methods get_package_details, list_installed

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_CLIMgr___init___2.py:6: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_CLIMgr___init___2.py::test_CLIMgr_initialization
============================== 1 failed in 0.72s ===============================
"""