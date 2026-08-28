
import pytest
from ansible.module_utils.facts.packages import PkgMgr

# Test for list_installed method when no packages are installed

# Test for list_installed method when the implementation is not provided
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_list_installed_2.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________________ test_list_installed_empty ___________________________

    def test_list_installed_empty():
>       pkg_mgr = PkgMgr()
E       TypeError: Can't instantiate abstract class PkgMgr with abstract methods get_package_details, is_available, list_installed

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_list_installed_2.py:7: TypeError
_____________________ test_list_installed_not_implemented ______________________

    def test_list_installed_not_implemented():
        with pytest.raises(NotImplementedError):
>           pkg_mgr = PkgMgr()
E           TypeError: Can't instantiate abstract class PkgMgr with abstract methods get_package_details, is_available, list_installed

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_list_installed_2.py:13: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_list_installed_2.py::test_list_installed_empty
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_packages_PkgMgr_list_installed_2.py::test_list_installed_not_implemented
============================== 2 failed in 0.72s ===============================
"""