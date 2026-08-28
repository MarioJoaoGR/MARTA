
import pytest
from ansible.module_utils.facts.packages import PkgMgr




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_get_package_details_1.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
________________________ test_get_package_details_basic ________________________

    def test_get_package_details_basic():
>       pkg_mgr = PkgMgr()
E       TypeError: Can't instantiate abstract class PkgMgr with abstract methods get_package_details, is_available, list_installed

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_get_package_details_1.py:6: TypeError
____________________ test_get_package_details_with_version _____________________

    def test_get_package_details_with_version():
>       pkg_mgr = PkgMgr()
E       TypeError: Can't instantiate abstract class PkgMgr with abstract methods get_package_details, is_available, list_installed

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_get_package_details_1.py:12: TypeError
___________________ test_get_package_details_no_dependencies ___________________

    def test_get_package_details_no_dependencies():
>       pkg_mgr = PkgMgr()
E       TypeError: Can't instantiate abstract class PkgMgr with abstract methods get_package_details, is_available, list_installed

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_get_package_details_1.py:19: TypeError
__________________ test_get_package_details_with_dependencies __________________

    def test_get_package_details_with_dependencies():
>       pkg_mgr = PkgMgr()
E       TypeError: Can't instantiate abstract class PkgMgr with abstract methods get_package_details, is_available, list_installed

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_get_package_details_1.py:26: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_get_package_details_1.py::test_get_package_details_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_get_package_details_1.py::test_get_package_details_with_version
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_get_package_details_1.py::test_get_package_details_no_dependencies
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_get_package_details_1.py::test_get_package_details_with_dependencies
============================== 4 failed in 0.73s ===============================
"""