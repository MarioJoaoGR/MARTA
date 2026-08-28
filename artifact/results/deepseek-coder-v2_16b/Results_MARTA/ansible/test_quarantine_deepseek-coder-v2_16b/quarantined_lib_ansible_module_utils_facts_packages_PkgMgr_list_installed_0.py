
import pytest
from ansible.module_utils.facts.packages import PkgMgr

# Test for list_installed method

# Test for get_package_details method
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_list_installed_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_list_installed ______________________________

    def test_list_installed():
>       pkg_mgr = PkgMgr()
E       TypeError: Can't instantiate abstract class PkgMgr with abstract methods get_package_details, is_available, list_installed

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_list_installed_0.py:7: TypeError
___________________________ test_get_package_details ___________________________

    def test_get_package_details():
>       pkg_mgr = PkgMgr()
E       TypeError: Can't instantiate abstract class PkgMgr with abstract methods get_package_details, is_available, list_installed

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_list_installed_0.py:13: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_list_installed_0.py::test_list_installed
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_list_installed_0.py::test_get_package_details
============================== 2 failed in 0.35s ===============================
"""